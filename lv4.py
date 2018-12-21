from urllib.request import urlopen
import re
uri="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"

num=str(16044/2)


pa=re.compile("and the next nothing is (\d+)")
#
while True:
    content = urlopen(uri % num).read().decode('utf-8')
    print(content)
    match = pa.search(content)
    if match == None:
        break
    num = match.group(1)
