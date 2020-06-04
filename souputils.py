import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'faqcrawler.settings')
django.setup()
import requests
from bs4 import BeautifulSoup
from faq_api.models import FrequentlyAskedQuestions

def getSoup(base_site):
    print("creating data for faq's")
    response = requests.get(base_site)
    html = response.content
    soup = BeautifulSoup(html, 'lxml')
    with open('faq_LXML_Parser.html', 'wb') as file:
        file.write(soup.prettify('utf-8'))
    return soup

# base_site = "https://eternitymarketing.com/faq"
# soup = getSoup(base_site)
# que= soup.find_all('button',{'class':'faq-button reset'})
# questions = []
# for q in que:
#     questions.append(q.text)
	
# ans = soup.find_all('div',{'class':'faq-panel'})
# answers = []
# for a in ans:
#     answers.append(a.find('p').text)

# for i in range(0,len(questions)):
#     FrequentlyAskedQuestions.objects.create(
#         question = questions[i],
#         answer = answers[i],
#         )