import re
import requests
import time
from bs4 import BeautifulSoup

"""
PLEASE NOTE:
Question A-2 for test 1001 from Link 1 does not work because it relies on an image file.
You can either skip this question or test yourself online here:
http://passcomptia.com/comptia-a-220-1001/comptia-a-220-1001-question-a-2/

Also, the program runs slowly by necessity (see time.sleep on line 60).
This is intentional in order to avoid hitting the limit of requests per minute.

STILL TO BE DONE:
- add 900 series questions (save to separate files)
- set up link2 (currently being blocked by website, needs work-around)
"""

sources = {
	"link1": "http://passcomptia.com/",
	"link2": "https://www.examcompass.com/"
}

def clean_html(raw_html):
	cleanr = re.compile("<.*?>")
	clean_text = re.sub(cleanr, '', raw_html)
	return clean_text

def collect_link1_links(url):
	soup = BeautifulSoup(requests.get(url).text, "html.parser") # entire HTML of page
	links = soup.findAll("a")
	hrefs = []
	for link in links:
		if "220-1001-question" in str(link) or "220-1002-question" in str(link):
			hrefs.append(sources["link1"] + link.get("href"))
	return hrefs

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

def collect_link2_links(url):
	pass

def scrape_link2(url):
	pass

def scrape(url):
	if sources["link1"] in url:
		scrape_link1(url)
	if sources["link2"] in url:
		scrape_link2(url)

def save(data):
	if "1001" in data["question_id"]:
		with open("1001_questions.txt", "a") as f:
			f.write(data["question_id"] + "\n")
			f.write(data["question"] + "\n")
			for option in data["answer_options"]:
				f.write(option + "\n")
			f.write("\n\n")
		with open("1001_answer_key.txt", "a") as f:
			f.write(data["question_id"] + "\n")
			f.write(data["correct_answer"] + "\n\n")

	if "1002" in data["question_id"]:
		with open("1002_questions.txt", "a") as f:
			f.write(data["question_id"] + "\n")
			f.write(data["question"] + "\n")
			for option in data["answer_options"]:
				f.write(option + "\n")
			f.write("\n\n")
		with open("1002_answer_key.txt", "a") as f:
			f.write(data["question_id"] + "\n")
			f.write(data["correct_answer"] + "\n\n")

def run_app():
	print("Working... this may take a few minutes.")
	scrape("http://passcomptia.com/comptia-a-220-1001/")
	scrape("http://passcomptia.com/comptia-a-220-1002/")
	print("All done!")

run_app()

###