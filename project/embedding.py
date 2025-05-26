from sentence_transformers import SentenceTransformer
import config

model = SentenceTransformer(config.EMBEDDING_MODEL)

def generate_embeddings(chunks):
    """Generates embeddings for a list of text chunks."""
    return [model.encode(chunk) for chunk in chunks]
