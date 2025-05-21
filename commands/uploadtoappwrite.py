from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.id import ID
from utils.logmanager import *
import json
from appwrite.exception import AppwriteException
from tqdm import *

client = Client()
client.set_endpoint("https://fra.cloud.appwrite.io/v1")
client.set_project("6829e934001311b82b67")
client.set_key(
    "standard_12c229c003c0633bd468e676c133617bed8b6376d38e8504b6f1ea56ec9a439b41aeac2ff7a4ccdcbb95ea2b2394b84e6de4ed81e47b2505b81a9f21f62455e5d4d62a4304b43d3f092f3fd2d50208ec0183494b48795cb44e14cb152385caab84d7afaabace01d283c10cfbf5d4b64e681459e0efad359ec24a376e29a55c71"
)
databases = Databases(client)


def uploadtoappwrite():
    info("Ładowanie final_data.json")
    try:
        with open("././data/final_data.json") as f:
            loaded_data = json.load(f)
        success("Załadowano danne!")
    except json.JSONDecodeError as e:
        error("Error loading JSON data:", e)
        return

    documents_to_upload = []

    info("Tworzenie dokumentów...")
    for item in tqdm(
        loaded_data,
        desc="Tworzenie dokumentów",
        unit="document",
        bar_format="{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} {unit} • {elapsed} elapsed • {remaining} remaining",
        colour="yellow",
        ascii=True,
    ):
        document = {"collectionId": "6829ea8d0030d8b2385e", "data": item}
        documents_to_upload.append(document)

    info("Usuwanie wszystkich starych dokumentów...")
    deletealldocuments()

    info("Wysyłanie dannych do Appwrite")

    warn("NIE ZAMYKAJ PROGRAMU ALBO DUPA")

    for document in tqdm(
        documents_to_upload,
        desc="Wysyłanie dannych",
        unit="document",
        bar_format="{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} {unit} • {elapsed} elapsed • {remaining} remaining",
        colour="green",
        ascii=True,
    ):
        try:
            response = databases.create_document(
                database_id="6829ea88000a4493c92c",
                collection_id="6829ea8d0030d8b2385e",
                document_id=ID.unique(),
                data=document["data"],
            )
        except AppwriteException as e:
            error(f"Error creating document: {e.message}")
            error(f"Document data: {document['data']}")
            return

        if "status" in response and response["status"] != 201:
            error("Error uploading document:", response.get("message", "Unknown error"))
            return

    success("All documents uploaded successfully!")


def deletealldocuments():
    warn("Usuwanie wszystkich dokumentów...")
    databases.delete_documents(
        database_id="6829ea88000a4493c92c",
        collection_id="6829ea8d0030d8b2385e",
        queries=[],
    )