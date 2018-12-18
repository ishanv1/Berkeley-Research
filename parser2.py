from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import codecs
import re
import xlsxwriter
import glob

frequencies = {}
fullist = {}

def text_from_html(file, body):
    soup = BeautifulSoup(body, 'html.parser')
    primary_detail = soup.findAll('i') #gets all items with i tag
    for item in primary_detail:
      if item.text:
        for word in re.sub("[^\w]", " ",  item.text).split(): #get list of words out of string
            fullist[word] = file
            if word in frequencies.keys():
                frequencies[word] += 1
            else:
                frequencies[word] = 1

path = 'bovary/folios/*.html'
files = glob.glob(path)
for file in files:
    html = codecs.open(file,'r').read()
    text_from_html(file, html)

workbook = xlsxwriter.Workbook('additions.xlsx')
worksheet = workbook.add_worksheet()
worksheet2 = workbook.add_worksheet()

row = 0
col = 0

for key in frequencies.keys():
    row += 1
    worksheet.write(row, col, key)
    worksheet.write(row, col + 1, frequencies[key])

for key in fullist.keys():
    row += 1
    worksheet2.write(row, col, key)
    worksheet2.write(row, col + 1, fullist[key])

workbook.close()
