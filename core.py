import requests
import json
from docx import Document
from docx.shared import Inches
import abstractScraper as asc
import os 
import asyncio
#https://core.ac.uk:443/api-v2/search/machine?page=1&pageSize=10&apiKey=kyWUlBMmDFvqZ8fXeoIc2p07CObtYz9r




def downloadPDF(title, url):
    newTitle = ''
    print("In Download PDF")
    
    print("title " + title)
    for i in title:
        if(i == ' '):
            newTitle += '_'
        else:
            newTitle += i
    print("#")
    print(title)
    print("#")
    os.system('curl --connect-timeout 10 ' + url + ' -o ' + newTitle + '.pdf')
    return newTitle + '.pdf'


def getSearchTerm():
    print('Enter search term: \n')
    inputSearch = input()
    search =  inputSearch.split(' ')
    space = '%20'
    searchTerm = ''
    for i in search:
        searchTerm = searchTerm + i + space
    return searchTerm, inputSearch

def getData(searchTerm):
    API_key = 'kyWUlBMmDFvqZ8fXeoIc2p07CObtYz9r'
    Site = 'https://core.ac.uk:443/api-v2/search/'
    pageNum = 1
    pageSize = 35 #Value between 10 and 100
    fullSite = Site + searchTerm + '?page=' + str(pageNum) + '&pageSize=' + str(pageSize) + '&apiKey=' + API_key

    #print(fullSite)
    r = requests.get(fullSite)
    data = json.loads(r.text)["data"]
    print(data)
    return data


def makeDocument(data, searchTerm):
    document = Document()
    document.add_heading('Search Results For ' + searchTerm, 0)
    foundAbstract = False

   
    for i in range(0, len(data)):
        print(data[i])
        try:
            #print(data[i]['_source']['title'])
            document.add_heading(data[i]['_source']['title'])
        except KeyError:
            print("No Title Found")
        try:
            #print(data[i]['_source']['authors'])
            authors = ''
            for j in data[i]['_source']['authors']:
                authors = authors + j + ",    "
            document.add_paragraph(authors)
        except KeyError:
            print("No Authors Found")
        try:
            #print(data[i]['_source']['journal'])
            document.add_paragraph(data[i]['_source']['journal'])
        except KeyError:
            print("No Journal Found")
        try:
            #print(data[i]['_source']['datePublished'])
            document.add_paragraph(data[i]['_source']['datePublished'])
        except KeyError:
            print("No Date Published Found")
        try:
            #(data[i]['_source']['description'])
            if(len(data[i]['_source']['description']) > 400):
                foundAbstract = True
                print("Found Abstract")
                document.add_paragraph(data[i]['_source']['description'])
            else:
                print("Abstract Not Found")
                #Download PDF and get abstract
                correctURL = ''
                for j in data[i]['_source']['urls']:
                    
                    print(j)
                    if (j[-4:] == '.pdf'):
                        correctURL = j

                if(data[i]['_source']['fullTextIdentifier'][-4:] == '.pdf'):
                    correctURL = data[i]['_source']['fullTextIdentifier']
                
                print("Correct URL: " + correctURL)
                print(data[i]['_source']['fullTextIdentifier'])
                path = downloadPDF(data[i]['_source']['title'], correctURL)
                asc.getAbstract(path)
                document.add_paragraph(asc.getAbstract(path))
        except KeyError:
            print("Description Not Found")
        except TypeError:
            print("Type Error on " + data[i]['_source']['title'])
        except FileNotFoundError:
            print("File Not Found Error on " + data[i]['_source']['title'])
        try:
            #print(data[i]['_source']['urls'][0])
            downloadPDF(data[i]['_source']['title'], data[i]['_source']['url'][0])
            for j in data[i]['_source']['urls']:
                document.add_paragraph(j)
        except KeyError:
            print("URL's Not Found")
        print("-----")
        print("-----")
        print("-----")


    document.save('output.docx')

    
def main():
    searchTerm, inputSearch = getSearchTerm()
    data = getData(searchTerm)
    makeDocument(data, inputSearch)

main()
