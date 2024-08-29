# Ollama RAG
To implement RAG locally by using Ollma and vector database.

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



