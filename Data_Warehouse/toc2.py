import re 
a="we are learning toc lab and this is toc_lab"
print(re.findall("toc_lab",a))
print(re.findall("toc",a))

print(re.sub("toc","dsa",a))

print(re.sub("\s","-",a))

print(re.split("\s",a))
subject="toclab"
subject=["toc","dbms","ai"]
print(re.split("\and",a))
txt="the rain in spain"
x=re.search("^The.*spain$",txt)
print(x)
