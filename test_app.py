from flask import Flask, request
from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

response = llm.invoke("Tell me a dog joke?")

print(response)


