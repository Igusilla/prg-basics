import re

def email_sender(file):
    condition = 'From.+<([a-zA-Z\.]*@[a-zA-Z]*\.[a-zA-Z]*)>'
    email_s=re.search(condition, file)
    print(email_s[1])

def email_recipent(file):
    condition = 'To.+<([a-zA-Z\.]*@[a-zA-Z]*\.[a-zA-Z]*)>'
    email_r=re.search(condition, file)
    print(email_r[1])

def email_subject(file):
    condition = 'Subject: (.+)'
    email_s=re.search(condition, file)
    print(email_s[1])

def email_body(file):
    condition = "\r?\n\r?\n([.\r?\n]*)"
    email_b=re.search(condition, file)
    print(email_b[1])