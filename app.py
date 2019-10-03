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
	link1: "http://passcomptia.com/",
	link2: "https://www.test-questions.com/comptia-a-plus-exam-questions-01.php",
	link3: "https://www.examcompass.com/comptia/a-plus-certification/free-a-plus-practice-tests"
}

def scrape(url): # this function does not vary
	pass

def clean(data): # this function does not vary
	pass

def save(data): # this function does not vary
	pass

###