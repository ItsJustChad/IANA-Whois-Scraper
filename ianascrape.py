#!/usr/bin/python
#Author: @ItIsJustChad
#Last Updated: 26 April 2017

from bs4 import BeautifulSoup
import urllib2
import csv
import re

#define variables
ianaListURL = 'http://www.iana.org/domains/root/db'
ianaLatin = re.compile(r'([a-zA-Z0-9\-]+)\.html')
ianaWhois = re.compile(r'WHOIS Server:\s*(.+)')
ianaOrgURL = 'http://www.iana.org'

#setup writer
whoisCSV = open("whoisserverlist.csv","wb")
lineWriter = csv.writer(whoisCSV)

#load the list
ianaListSoup = BeautifulSoup(urllib2.urlopen(ianaListURL),'lxml')
ianaTable = ianaListSoup.find('tbody')

for link in ianaTable.findAll('a'):
        ianaTLDURL = link.get('href')
        ianaTLDLatin = re.search(ianaLatin,ianaTLDURL)
	tldName = link.text[1:].encode('utf-8')
	print "Processing %s" % tldName
	ianaTLDSoup = BeautifulSoup(urllib2.urlopen(ianaOrgURL+ianaTLDURL),'lxml')
	whoisServer = re.search(ianaWhois,ianaTLDSoup.getText())

	if whoisServer is not None:
		print tldName, ianaTLDLatin.group(1), whoisServer.group(1)
		lineWriter.writerow((tldName,ianaTLDLatin.group(1),whoisServer.group(1)))

	else:
		print tldName, ianaTLDLatin.group(1)
		lineWriter.writerow((tldName,ianaTLDLatin.group(1)))

tldCSV.close()
