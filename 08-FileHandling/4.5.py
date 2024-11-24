import emails
with open("email.txt", 'r') as file:
    email=file.read()
emails.email_sender(email)
emails.email_recipent(email)
emails.email_subject(email)
emails.email_body(email)