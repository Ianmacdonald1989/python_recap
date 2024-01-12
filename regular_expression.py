#LIST FOR REGULAR EXPRESSION 

import re

names = ["Finn Bindeballe",
         "Geir Anders Berge",
         "HappyCodingRobot",
         "Ron Crombridge",
         "Sohil"]

#find first and last name only

regex = '^\w+ \w+$'
for name in names:
    result = re.search(regex, name)
    if result:
        print(name)

## search for word character sequence starting with c and their value start anfd end 
        
# regex = 'C\w*'
# for name in names:
#     match = re.search(regex, name)
#     if match: 
#         print(name)
#         print(match.start())
#         print(match.end())


# ## finding the characters of c their value 
# regex = 'C\w*'
# for name in names:
#     match = re.search(regex, name)
#     if match: 
#         print(name)
#         print(match.span())
#         print(match.group())


#new list for regular expression 

# import re

# names = ["Brian Daugette", 
#         "Veronica Superconica",
#         "Tony Gasparovic",
#         "Patrick German",
#         "m!sha"]

#test for first name and last name
# regex = '^(\w+)\s+(\w+)$'
# for name in names: 
#     match = re.search(regex, name)
#     if match:
#         print(name)
#         print(match.group(1))
#         print(match.group(2))

#extended test for first name 
# regex = '^(?P<fn>\w+)\s+(?P<ln>\w+)$'
# for name in names: 
#     match = re.search(regex, name)
#     if match:
#         print(name)
#         print(match.group(1))
#         print(match.group(2))

#detect last name 

# regex = '^[a-zA-Z!]+$'
# for name in names:
#     if re.search(regex, name):
#         print(name)


#findall function 
# regex = '^[a-z]+'
# for name in names:
#     matches = re.findall(regex, name)
#     if matches:
#         print(matches)

#find interger 
# regex = '^[a-z]+'
# for name in names:
#     matches = re.finditer(regex, name)
#     for match in matches:
#         print(match)


#new list of search

# import re
#
# values = ["https://www.socratica.com",
#           "http://www.socratica.org",
#           "file://test.this.path",
#           "com.socratica.www_http://"]

#other function 

#test if string starts with http or https 
# regex = "https?"
# for value in values:
#     if re.match(regex, value):
#         print(value)

#test for full match 
# regex = "https?:\\w{3}.\w+.(org|com)"
# for value in values:
#     if re.fullmatch(regex, value):
#         print(value)









