import requests
from bs4 import BeautifulSoup

"""
LINK 1: how data structure should look
[
	{
		"question": "A systems administrator is configuring a server to host several virtual machines. The administrator configures the server and is ready to begin provisioning the virtual machines. Which of the following features should the administrator utilize to complete the task?",
		"answer_options": {
			"A": "Hypervisor",
			"B": "Disk management",
			"C": "Terminal services",
			"D": "Device Manager",
			"E": "Virtual LAN"
		},
		"correct_answer": ["A"]
	}, {
		"question": "A user accidentally spills liquid on a laptop. The user wants the device to be fixed and would like to know how much it will cost. Which of the following steps should the technician take NEXT to verify if the device is repairable before committing to a price? (Choose two.)",
		"answer_options": {
			"A": "Remove the case and organize the parts.",
			"B": "Document the screw locations.",
			"C": "Search the Internet for repair tutorials.",
			"D": "Consult colleagues for advice.",
			"E": "Place the device in rice for a few days."
		},
		"correct_answer": ["A", "B"]
	}
]
"""

data = {
	"link1": "http://passcomptia.com/",
	"link2": "https://www.test-questions.com/",
	"link3": "https://www.examcompass.com/"
}

def scrape(url): # this function never varies
	if data["link1"] in url:
		print("That's a LINK 1 page!")
		return scrape_link1(url)
	if data["link2"] in url:
		print("That's a LINK 2 page!")
		return scrape_link2(url)
	if data["link3"] in url:
		print("That's a LINK 3 page!")
		return scrape_link3(url)

def scrape_link1(url):
	soup = BeautifulSoup(requests.get(url).text, "html.parser") # entire HTML of page
	links = soup.findAll("a")
	hrefs_1001 = []
	hrefs_1002 = []
	for link in links:
		if "comptia-a-220-1001/comptia-a-220-1001-question" in str(link):
			hrefs_1001.append(data["link1"] + link.get("href"))
		if "comptia-a-220-1002/comptia-a-220-1002-question" in str(link):
			hrefs_1002.append(data["link1"] + link.get("href"))

def scrape_link2(url):
	pass

def scrape_link3(url):
	pass

def clean(data): # this function never varies
	pass

def save(data): # this function never varies
	pass

# TESTING CODE
scrape("http://passcomptia.com/comptia-a-220-1001/")
# scrape("https://www.test-questions.com/comptia-a-plus-exam-questions-01.php")
# scrape("https://www.examcompass.com/comptia-a-plus-certification-practice-test-1-exam-220-1001")

###