from dotenv import load_dotenv, find_dotenv

from langchain.prompts import PromptTemplate
from langchain import hub 
from langchain.agents import Tool, AgentExecutor, initialize_agent, create_react_agent
from langchain.tools import DuckDuckGoSearchRun, WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper
from langchain_openai import ChatOpenAI

load_dotenv(find_dotenv(), override=True)

llm = ChatOpenAI(model_name='gpt-4-turbo-preview', temperature=0)

template = '''
Answer the following questions as best as you can. 
Questions: {q}
'''

prompt_template = PromptTemplate.from_template(template)
prompt  = hub.pull("hwchase17/react")
# print(type(prompt))
# print(prompt.input_variables)


# TOOLS 
# Wikipedia tool 
api_wrapper = WikipediaAPIWrapper()
wikipedia = WikipediaQueryRun(api_wrapper=api_wrapper)
wikipedia_tool = Tool(
    name='Wikipedia', 
    func=wikipedia.run, 
    description='Useful when you need to look up a topic on Wikipedia. '
)


# DuckDuckGo Search Tool 
search = DuckDuckGoSearchRun()
duckduckgo_tool = Tool(
    name='DuckDuckGo Search', 
    func=search.run, 
    description='Useful when need to perform an internet search to find information that another tool can\'t provide'
)


tools = [wikipedia_tool, duckduckgo_tool]

agent = create_react_agent(llm, tools, prompt)   #combines the llm, tools & prompt 
                                                 # to create a react agent 
# setup AgentExecutor to run the agent  
agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    verbose=True, 
    handle_parsing_errors=True, 
    max_iterations=10
)    


question = 'search wikipedia for references in machine learning framework'

output = agent_executor.invoke({
    'input': prompt_template.format(q=question)
}
)