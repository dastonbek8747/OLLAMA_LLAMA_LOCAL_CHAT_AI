from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM


def main():
    model = OllamaLLM(model="llama3.2")

    template = """
You are a coding assistant. The user will describe a coding task and a target programming language.
Your job is to write correct and clean code in that language.

User Request:
------------
{question}
------------
Please write the code and explain briefly if necessary.
"""

    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    while True:
        print("\n===============================")
        question = input("SAVOL  : ")
        if question.strip().lower() in ["q", "exit"]:
            break
        response = chain.invoke({"question": question})
        print("\nGenerated Code LLAMA :\n")
        print(response)


if __name__ == "__main__":
    main()

# ===========================================================
# bu qismida men ai lar bilan ishlashni moljalladim lekin bular pullik ekan kopincha
# ================================================
# # from dotenv import load_dotenv
# # from langchain.tools import tool
# # from langchain_openai import ChatOpenAI
# # from langchain_ollama import OllamaLLM
# # from langgraph.prebuilt import create_react_agent
# # from langchain_core.messages import HumanMessage
# #
# # load_dotenv()
# #
# #
# # def main():
# #     model = ChatOpenAI(temperature=0)
# #     tools = []
# #     agent_executor = create_react_agent(model, tools)
# #     while True:
# #         print("Salom open ai bilan chat qilamiz !")
# #         request_user = input("Your requests:  ")
# #         if request_user == "q" or request_user == "exit":
# #             break
# #         print("\nCHAT OPEN AI MESSAGES :\n")
# #         for chunk in agent_executor.stream(
# #                 {"messages": [HumanMessage(content=request_user)]}
# #         ):
# #             if "agent" in chunk and "messages" in chunk["agent"]:
# #                 for message in chunk["agent"]["messages"]:
# #                     print(message.content, end="")
# #             print()
# #
# #
# # if __name__ == "__main__":
# #     main()
# from dotenv import load_dotenv
# from langchain.tools import tool
# from langchain_openai import ChatOpenAI
# from langchain_ollama import OllamaLLM
# from langgraph.prebuilt import create_react_agent
# from langchain_core.messages import HumanMessage
#
# load_dotenv()
#
#
# def main():
#     model = ChatOpenAI(temperature=0)
#     tools = []
#     agent_executor = create_react_agent(model, tools)
#     while True:
#         print("Salom open ai bilan chat qilamiz !")
#         request_user = input("Your requests:  ")
#         if request_user == "q" or request_user == "exit":
#             break
#         print("\nCHAT OPEN AI MESSAGES :\n")
#         for chunk in agent_executor.stream(
#                 {"messages": [HumanMessage(content=request_user)]}
#         ):
#             if "agent" in chunk and "messages" in chunk["agent"]:
#                 for message in chunk["agent"]["messages"]:
#                     print(message.content, end="")
#             print()
#
#
# if __name__ == "__main__":
#     main()
