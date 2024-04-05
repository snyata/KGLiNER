# QDrant Vector Database Cloud Utility 
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct

def create_qdrant_client(host: str, port: int) -> QdrantClient:
    """
    Creates and returns a Qdrant client.
    
    Args:
        host: The host where the Qdrant service is running.
        port: The port on which the Qdrant service is accessible.
    
    Returns:
        A QdrantClient instance.
    """
    return QdrantClient(host=host, port=port)

def upsert_documents(client: QdrantClient, collection_name: str, documents: list):
    """
    Upserts documents into a specified Qdrant collection.
    
    Args:
        client: The Qdrant client instance.
        collection_name: The name of the collection to upsert documents into.
        documents: A list of documents, where each document is expected to be
                   a dictionary matching the Qdrant collection schema.
    """
    points = [PointStruct(**doc) for doc in documents]
    client.upload_collection(collection_name=collection_name, points=points)