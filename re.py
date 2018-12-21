import re
def is_valid_email(addr):
    a=re.match('^\w+\@[a-zA-Z]+.com$',addr)
    if a:
        print(a.group(0))
        return True
    return False

is_valid_email("9532481@qq.com")
