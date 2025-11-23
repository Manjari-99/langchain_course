import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()


def main():
    print("Hello from langchain-course!")
    information = "Leo Messi is the greatest footballer of all time. He is from Argentina. He started off in Barcelona "
    summary_template = "from the given information {information} I want you to create :" \
    "1. a short summary" \
    "2. Two interesting facts"

    summary_prompt_template = PromptTemplate(input_variables=["information"], template= summary_template)

    llm = ChatOpenAI(model="gpt-5", temperature=0)

    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information": information})

    print(response.content)

if __name__ == "__main__":
    main()
