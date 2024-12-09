import os
import json
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient
import openai
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

# Funktio promottien lataamiseksi
def load_prompts(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)["prompts"]

# Funktio oikean promptin hakemiseen
def get_prompt(prompts, prompt_type, context, user_input):
    if prompt_type not in prompts:
        raise ValueError(f"Prompt type '{prompt_type}' ei löydy.")
    prompt = prompts[prompt_type]
    for message in prompt:
        message['content'] = message['content'].replace("{context}", context).replace("{user_input}", user_input)
    return prompt

# Haku tulosten käsittelyä varten
def process_search_results(results):
    search_content = []
    for result in results:
        chunk_content = result.get("chunk", result.get("content"))
        if chunk_content:
            search_content.append(chunk_content)
    if not search_content:
        return "Annetussa aineistossa ei ole tietoa tästä aiheesta."
    return ' '.join(search_content)

def main():
    try:
        # Lataa ympäristömuuttujat
        load_dotenv()
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")
        azure_storage_account_name = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
        azure_storage_account_key = os.getenv("AZURE_STORAGE_ACCOUNT_KEY")
        azure_storage_container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME")
        azure_storage_blob_name = os.getenv("AZURE_STORAGE_BLOB_NAME")
        azure_search_index = os.getenv("AZURE_SEARCH_INDEX")
        azure_search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
        azure_search_api_key = os.getenv("AZURE_SEARCH_API_KEY")  

        # Lataa promptit erillisestä JSON-tiedostosta
        prompts = load_prompts("prompts.json")

        # Yhdistä Azure Blob Storageen ja lataa blobin sisältö
        blob_service_client = BlobServiceClient(
            account_url=f"https://{azure_storage_account_name}.blob.core.windows.net",
            credential=azure_storage_account_key
        )

        blob_client = blob_service_client.get_blob_client(
            container=azure_storage_container_name,
            blob=azure_storage_blob_name
        )
        blob_data = blob_client.download_blob().readall().decode('utf-8')
        data = json.loads(blob_data)  # Muunna JSON:ksi

        # Yhdistä Azure Cognitive Searchiin ja tee haku
        search_client = SearchClient(endpoint=azure_search_endpoint,
                                     index_name=azure_search_index,
                                     credential=AzureKeyCredential(azure_search_api_key))

        user_input = input("Kirjoita kysymyksesi: ").strip()
        if not user_input:
            raise ValueError("Question cannot be empty.")

        # Tee haku Azure Cognitive Searchissa
        search_query = {"queryType": "simple", "search": user_input, "searchMode": "all"}
        results = search_client.search(search_query)

        # Käsittele hakutulokset
        search_content = []
        for result in results:
            chunk_content = result.get("chunk")
            if chunk_content:
                search_content.append(chunk_content)
            else:
                print("Warning: 'chunk' field not found in result.")

        if not search_content:
            raise RuntimeError("No relevant search results with 'chunk' field found in Azure Cognitive Search.")

        # Muodosta konteksti hakutuloksista
        context = ' '.join(search_content)

        # Valitse promptityyppi ja muodosta viestit
        prompt_type = "timeline_events"
        prompt_messages = get_prompt(prompts, prompt_type, context="Emman elämäntapahtumat", user_input="")

        # Aseta OpenAI asetukset
        openai.api_type = "azure"
        openai.api_key = azure_oai_key
        openai.api_base = azure_oai_endpoint
        openai.api_version = "2024-10-01-preview"

        # Lähetä kysymys OpenAI:lle valitulla promptilla
        response = openai.ChatCompletion.create(
            engine=azure_oai_deployment,
            messages=prompt_messages,
            temperature=0.2,
            max_tokens=750
        )

        # Tarkista ja tulosta vastaus
        if not response or 'choices' not in response or not response['choices']:
            raise RuntimeError("AI did not return a valid response.")
        print(f"Kysymys: {user_input}")
        print("Vastaus:", response['choices'][0]['message']['content'].strip())

    except Exception as ex:
        print("Error:", ex)

if __name__ == "__main__":
    main()