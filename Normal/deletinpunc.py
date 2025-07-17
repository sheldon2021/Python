# so lets delete punctuations in a sentence 
# first we use the method of strip which will allow us to delete punctuations at start and end only 


text = "!Hello World"

new = text.strip('!')

print(new)

# You have to assign it to new because strings are immutable and it creates a new string hence assign new one to new
# # 
# another method of removing punctuations is importing string or importing re(regex) these methods are used 
# when the punctuations exist in middle of the sentence and not at start or end 


import string


text = "Hello, World! This is Earth :)"


newtex = text.translate(str.maketrans('','',string.punctuation))

print(newtex)

# or another method is using import re


import re

text = "Hello, World! This is Earth :)"

news = re.sub(r'[^\w\s]','',text) 

print(news)


