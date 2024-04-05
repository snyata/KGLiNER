# Selecting your embeddings model and uploading depending on use case.
import argparse
from qdrant_client import QdrantClient

def main():
    parser = argparse.ArgumentParser(description="Upload documents to Qdrant with selected embedding models.")
    parser.add_argument('--advanced', action='store_true', help="Use advanced embeddings OpenAI small model.")
    parser.add_argument('--mid', action='store_true', help="Use advanced embeddings Sentence Transformers).")
    parser.add_argument('--collection', type=str, help="The Qdrant collection name.")
    parser.add_argument('--data', type=str, help="Path to the data file.")
    parser.add_argument('--chunk_size', type=int, default=100, help="Chunk size for data upload.")
    
    args = parser.parse_args()
    
    # Example: Load your data here
    data = load_data(args.data)
    chunks = chunk_data(data, args.chunk_size)
    
    model_selected = select_embedding_model(args.advanced)
    print(f"Selected model: {model_selected}")
    
    # Initialize Qdrant client
    client = QdrantClient(host="localhost", port=6333)
    upload_to_qdrant(client, args.collection, chunks)

if __name__ == "__main__":
    main()
