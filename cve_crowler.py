# coding:utf-8
import requests
import re
from bs4 import BeautifulSoup

print("Please type CVE Number e.g. CVE-2016-10227")
cve = str(input())
#url = 'https://nvd.nist.gov/vuln/detail/CVE-2016-10227'
url = 'https://nvd.nist.gov/vuln/detail/'+cve
response = requests.get(url)
response.encoding = response.apparent_encoding
#print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')

#for i in soup.select("strong"):
#    print(i.getText())
#    for j in soup.select("span"):
#        print(j.getText())

print(soup.find_all("p", attrs={"data-testid":re.compile("^vlun")}))
