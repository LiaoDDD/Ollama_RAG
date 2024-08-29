# PDF RAG
This project is to implement LLM PDF RAG __locally__ .
Set up API by using Ollama,LangChain,ChromaDB,and Flask.
Uplaod the PDF file by API,and integrate with the LLM to complete Retrieval Augemented Generation.
At the end of the project we look forward to complete system as a Rest API for uploading PDF documents and asking questions againsts the document.
## Workspace

### Download Ollama

First you will have to download the ollama for using the LLM.

[Ollama](https://ollama.com/download) 
 
### Run LLM

After Download Ollama,choose the LLM you want and pull.

```zsh
ollama pull llama3
```

Now you can run the LLM that you pull.
```zsh
ollama run llama3
```
### Create virtual environment

Went to the place where you want to create your virtual environment.
Here we will use Documents for example.
```bash 
cd Documents
```

Create a new file for virtual environment and get into the file.
```zsh
mkdir llama_RAG
cd llama_RAG
```

Now you can setting up the environment,we will use 'RAG' for example to be our environment name.
```zsh
python -m venv RAG
```
### Activating/Deactivating environment

To activate the environment __you will have to do this for every new terminal session.__
```zsh
source RAG/bin/activate
```
To deactivate:
```zsh
deactivate
```



