# cd ~/git/chrissycracker/
# python script.py


import urllib.request
from bs4 import BeautifulSoup
import csv
from random import randint

def fn_wordassociated(subject):
	with open('associations.csv','r') as infile:
		reader = csv.DictReader(infile)
		data = {}
		for row in reader:
			for header, value in row.items():
				try:
					data[header].append(value)
				except KeyError:
					data[header] = [value]
		if data['subject'].count(subject) > 0:
			return(True)
		else:
			return(False)

def fn_associate(subject):
	if fn_wordassociated(subject) == False:
		with urllib.request.urlopen('http://wordassociation.org/words/' + subject) as f:
			html = f.read()
		soup = BeautifulSoup(html, 'html.parser')
		linksto = soup.find(summary="links to '" + subject + "'")
		linksto_array = [subject]
		for i in range(0,5):
			linksto_array.append(linksto.find_all("a")[i].get_text())
		with open('associations.csv', 'a') as outfile:
			wr = csv.writer(outfile)
			wr.writerow(linksto_array)
		print('Added:',subject)


def fn_pickrandomrow():
	rint = randint(0,len(open('associations.csv','r').readlines()))
	with open('associations.csv','r') as infile:
		reader = csv.DictReader(infile)
		for i, row in enumerate(reader):
			if i == rint:
				print('====================')
				print(row['subject'].upper())
				print('====================')
				return(row)
				break

def fn_pickspecificrow(word):
	with open('associations.csv','r') as infile:
		reader = csv.DictReader(infile)
		for row in reader:
			if row['subject'] == word:
				print('====================')
				print(row['subject'].upper())
				print('====================')
				return(row)
				break

def fn_getassociations(associations):
	for assoc in ['one','two','three','four','five']:
		with open('associations.csv','r') as infile:
			reader = csv.DictReader(infile)
			print('--------------------')
			print(associations[assoc].upper())
			print('--------------------')
			for row in reader:
				if row['subject'] != associations['subject'] and associations[assoc] in row.values() and associations[assoc] != row['subject']: print(row['subject'])


fn_getassociations(fn_pickrandomrow())

# subject = 'fruit'
# fn_associate(subject)
# fn_getassociations(fn_pickspecificrow(subject))

