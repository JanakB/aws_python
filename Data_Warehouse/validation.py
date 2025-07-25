from ast import pattern
import re
def check_mail(pattern,email):
    x=re.search(pattern,email)
    if(x):
        print("true")
    else:
        print("false")
check_mail("hi","hi")
check_mail("hi","hello")
pattern="^[a-z]{1,12}[@][a-z]{1,8}[.][com|org|net]$"
check_mail(pattern,"1@2.com")
check_mail(pattern,"a@b.com")