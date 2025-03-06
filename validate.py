import re

email = input("What's your email? ").strip()

username, domain = email.split("@")

if re.search("@",email):
    print("Valid")
else:
    print("Invalid")