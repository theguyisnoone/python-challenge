result=""#create empty string
raw="g fmnc wms bgblr rpylqjyrc gr zw fylb.rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
for t in raw:
    if t>='a' and t<='z':
        result += chr(((ord(t)+2)-ord('a'))%26+ord('a'))
    else:
        result += t #非字符

print(result)

table=str.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab' )
key=raw.translate(table)
print(key)

a="abcdefghijklmnopqrstuvwxyz,. '()" #.'' ！！！
b="cdefghijklmnopqrstuvwxyzab,. '()"
sol3="".join([dict(zip(a, b))[x] for x in raw])
print(sol3)
# print("".join([dict(zip(a,b))[x] for x in raw]))


print('map'.translate(table))
