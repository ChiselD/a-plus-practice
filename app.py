import re
import requests
import time
from bs4 import BeautifulSoup

"""
PLEASE NOTE:
Question A-2 for test 1001 from Link 1 does not work because it relies on an image file.
You can either skip this question or test yourself online here:
http://passcomptia.com/comptia-a-220-1001/comptia-a-220-1001-question-a-2/

Also, the program runs slowly by necessity (see time.sleep calls).
This is intentional in order to avoid hitting the limit of requests per minute, 
which would block the web scraper from accessing the respective webpage.

STILL TO BE DONE:
- add 900 series questions (save to separate files)
- add https://www.quickstart.com/practice-test-comptia-a-220-1001.html
- add https://www.quickstart.com/practice-test-comptia-a-220-1002.html
- add https://quizlet.com/389272712/comptia-a-core-1-220-1001-practice-test-questions-flash-cards/
- add https://www.certlibrary.com/exam/220-1001
- add https://www.certlibrary.com/exam/220-1002
- add https://www.edusum.com/comptia/comptia-a-plus-220-1001-certification-sample-questions
- add https://www.edusum.com/comptia/comptia-a-plus-220-1002-certification-sample-questions

"""

sources = {
	"link1": "http://passcomptia.com/",
	"link2": "https://certification.comptia.org/",
}


def clean_html(raw_html):
	cleanr = re.compile("<.*?>")
	clean_text = re.sub(cleanr, '', raw_html)
	return clean_text


def save(data):
	test_num = 0
	if "1001" in data["question_id"]:
		test_num = "1001"
	elif "1002" in data["question_id"]:
		test_num = "1002"
	# elif "901" in data["question_id"]:
	# 	test_num = "901"
	# elif "902" in data["question_id"]:
	# 	test_num = "902"

	q_file_name = test_num + "_questions.txt"
	a_file_name = test_num + "_answer_key.txt"

	with open(q_file_name, "a") as f:
		f.write(data["question_id"] + "\n")
		f.write(data["question"] + "\n")
		for option in data["answer_options"]:
			f.write(option + "\n")
		f.write("\n\n")
	with open(a_file_name, "a") as f:
		f.write(data["question_id"] + "\n")
		f.write(data["correct_answer"] + "\n\n")


def collect_link1_links(url):
	soup = BeautifulSoup(requests.get(url).text, "html.parser")
	links = soup.findAll("a")
	hrefs1000 = []
	for link in links:
		if "220-1001-question" in str(link) or "220-1002-question" in str(link):
			hrefs1000.append(sources["link1"] + link.get("href"))
	return hrefs1000


def scrape_link1(url):
	all_question_urls = collect_link1_links(url)

	for url in all_question_urls:
		try:
			soup = BeautifulSoup(requests.get(url).text, "html.parser")

			question_block = soup.find(class_="entry-content")
			question_id = clean_html(str(soup.find(class_="entry-title")))
			print(f"Saving question {question_id}...")
			question = clean_html(str(question_block.p.b))
			answer_options = str(question_block.p.find_next_sibling()).split("<br/>")
			answer_options_list = [clean_html(option) for option in answer_options]
			correct_answer = clean_html(str(question_block.span.b))

			data_item = {
				"question_id": question_id,
				"question": question,
				"answer_options": answer_options_list,
				"correct_answer": correct_answer
			}
			save(data_item)
			time.sleep(2)
			
		except AttributeError:
			continue


def scrape_link2(url):
	if "1001" in url:
		print("This is a 1001 test.")
		id_prefix = "1001"
	if "1002" in url:
		print("This is a 1002 test.")
		id_prefix = "1002"

	soup = BeautifulSoup(requests.get(url).text, "html.parser")
	
	question_block = soup.findAll(class_="sfContentBlock")[0]
	answer_block = soup.findAll(class_="sfContentBlock")[1]
	question_content = [clean_html(str(x)) for x in question_block if str(x).startswith("<p>")]
	answer_content = [clean_html(str(x)) for x in answer_block if str(x).startswith("<p>")]

	location = 0
	questions = []

	for n in range(0, len(question_content)//2):
		questions.append([question_content[location], question_content[location+1]])
		location = location + 2

	for item in questions:
		question_split = [item[0].split("\n", 1)[0], item[0].split("\n", 1)[1]]
		question_id = question_split[0][9:]
		print(f"Saving question {question_id}...")
		question_id_string = f"Test {id_prefix}: Question {question_id}"
		question = question_split[1]
		answer_options_list = item[1].split("\n")
		correct_answer = answer_content[questions.index(item)]

		data_item = {
			"question_id": question_id_string,
			"question": question,
			"answer_options": answer_options_list,
			"correct_answer": correct_answer
		}

		save(data_item)
		time.sleep(2)


def scrape(url):
	if sources["link1"] in url:
		print("Link 1 link detected.")
		scrape_link1(url)
	if sources["link2"] in url:
		print("Link 2 link detected.")
		scrape_link2(url)


def run_app():
	print("Working... this may take a few minutes.")

	# Link 1 links
	scrape("http://passcomptia.com/comptia-a-220-1001/")
	scrape("http://passcomptia.com/comptia-a-220-1002/")

	# Link 2 links
	# scrape("https://certification.comptia.org/training/resources/practice-tests/comptia-a-1001-practice-questions")
	# scrape("https://certification.comptia.org/training/resources/practice-tests/comptia-a-1002-practice-questions")

	print("All done!")


run_app()

###