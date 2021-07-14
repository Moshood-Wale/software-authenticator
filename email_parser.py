
# Regex Pattern module imported
import re

# A function that parses an email
def email_parser(email) :
    
    # Both keys seperates the username and domain name respectively
    keys = ['username', 'domain']
    
    # email_input validation    
    pattern = re.compile(r"(^[a-z]+[a-z+]+[a-z0-9]+@[a-z][a-z0-9]+\.com$)")

    # Ckecks characters in the mail
    confirm_email = pattern.search(email)

    if confirm_email:
        
        split_email = re.split("@", email)
        
        dictionary = {k:v for (k,v) in zip(keys, split_email)}
        
        return dictionary
    
    else:
        
        return None

print(email_parser("jane+doe@yahoo.com"))

