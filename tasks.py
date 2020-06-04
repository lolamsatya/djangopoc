# import os
# import django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'faqcrawler.settings')
# django.setup()
# import requests
# from bs4 import BeautifulSoup
# from faq_api.models import FrequentlyAskedQuestions

from souputils import getSoup
from faq_api.models import FrequentlyAskedQuestions

# print("creating data for faq's")
# base_site = "https://eternitymarketing.com/faq"
# response = requests.get(base_site)
# html = response.content
# soup = BeautifulSoup(html, 'lxml')
# with open('faq_LXML_Parser.html', 'wb') as file:
#     file.write(soup.prettify('utf-8'))
import hashlib

base_site = "https://eternitymarketing.com/faq"
soup = getSoup(base_site)
que= soup.find_all('button',{'class':'faq-button reset'})
questions = []
for q in que:
    questions.append(q.text)
	
ans = soup.find_all('div',{'class':'faq-panel'})
answers = []
for a in ans:
    answers.append(a.find('p').text)

for i in range(0,len(questions)):
    m = hashlib.sha256()
    m.update(questions[i].encode('utf-8'))
    shaid = m.digest()
    faq, created = FrequentlyAskedQuestions.objects.get_or_create(shaid = shaid)
    faq.question = questions[i]
    faq.answer = answers[i]
    faq.save()
  
    # FrequentlyAskedQuestions.objects.create(
    #     question = questions[i],
    #     answer = answers[i],
    #     )