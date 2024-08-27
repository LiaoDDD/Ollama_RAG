from langchain_openai import AzureChatOpenAI

llm = AzureChatOpenAI(
    openai_api_version=os.environ["AZURE_OPRNAI_API_VERSION"],
    azure_deployment=os.environ[
        "AZURE_OPRNAI_DEPLOYMENT_NAME"
    ]
)