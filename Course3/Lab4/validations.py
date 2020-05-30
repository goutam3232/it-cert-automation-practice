#!/usr/bin/env python3

import re
def validate_user(username, minlen):
    """Checks if the recieved username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

def rearrange_name(name):
	result = re.search(r"^(\[\w .]\)*), (\[\w .]*)$", name)
	if result is None:
		return name 
	return "{} {}".format(result[2], result[1])


        
	if len(username) < minlen:
    		return False
	if not re.match('^[a-z0-9._]*$',username):
        	return False
     # Usernames can't begin with a number
	
	if username [0].isnumeric():
        	return False
       	return True

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False
