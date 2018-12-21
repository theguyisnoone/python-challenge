import urllib.request
import re
html=urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()

pa=re.compile(r'[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+')

ma=pa.findall(html)

for c in ma:
    print(c,end="")
