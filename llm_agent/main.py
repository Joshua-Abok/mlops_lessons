from langchain.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

output = search.invoke('joshua abok')
print(output)