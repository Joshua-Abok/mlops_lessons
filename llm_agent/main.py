from langchain.tools import DuckDuckGoSearchRun
from langchain.tools import DuckDuckGoSearchResults
import re 

# search = DuckDuckGoSearchRun()

# output = search.invoke('joshua abok')
# print(output)

search = DuckDuckGoSearchResults()
output = search.run("Joshua abok")
# print(output)

#  user friendly output
# -> use regular exp. to etract the snippet, link & the title 
# define a pattern 
pattern = r'snippet: (.*?), title: (.*?), link: (.*?)\],'

# call findall function to find all matches of the pattern in the string 
matches = re.findall(pattern, output, re.DOTALL)

for snippet, title, link in matches: 
    print(f'Snippet: {snippet}\nTitle: {title}\nLink: {link}\n')
    print('-' * 50)
