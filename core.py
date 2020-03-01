import requests
import json
from docx import Document
from docx.shared import Inches
#https://core.ac.uk:443/api-v2/search/machine?page=1&pageSize=10&apiKey=kyWUlBMmDFvqZ8fXeoIc2p07CObtYz9r

document = Document()

API_key = 'kyWUlBMmDFvqZ8fXeoIc2p07CObtYz9r'
Site = 'https://core.ac.uk:443/api-v2/search/'
search = ''
space = '%20'
pageNum = 1
pageSize = 100 #Value between 10 and 100

print('Enter search term: \n')
inputSearch = input()
search =  inputSearch.split(' ')
searchTerm = ''
for i in search:
    searchTerm = searchTerm + i + space

fullSite = Site + searchTerm + '?page=' + str(pageNum) + '&pageSize=' + str(pageSize) + '&apiKey=' + API_key

print(fullSite)
r = requests.get(fullSite)

#l = json.loads(r.text)["data"][2]

document.add_heading('Search Results For ' + inputSearch, 0)
data = json.loads(r.text)["data"]

for i in range(0, len(data)):
    try:
        print(data[i]['_source']['title'])
        document.add_heading(data[i]['_source']['title'])
    except KeyError:
        print("No Title Found")
    try:
        print(data[i]['_source']['authors'])
        authors = ''
        for j in data[i]['_source']['authors']:
            authors = authors + j + ",    "
        document.add_paragraph(authors)
    except KeyError:
        print("No Authors Found")
    try:
        print(data[i]['_source']['journal'])
        document.add_paragraph(data[i]['_source']['journal'])
    except KeyError:
        print("No Journal Found")
    try:
        print(data[i]['_source']['datePublished'])
        document.add_paragraph(data[i]['_source']['datePublished'])
    except KeyError:
        print("No Date Published Found")
    try:
        print(data[i]['_source']['description'])
        document.add_paragraph(data[i]['_source']['description'])
    except KeyError:
        print("Description Not Found")
    try:
        print(data[i]['_source']['urls'])
        for j in data[i]['_source']['urls']:
            document.add_paragraph(j)
    except KeyError:
        print("URL's Not Found")
    print("-----")
    print("-----")
    print("-----")


document.save('output.docx')

