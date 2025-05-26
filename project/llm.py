import openai
import config

openai.api_key = config.OPENAI_API_KEY

def generate_response(query, context):
    """Generates a response using OpenAI LLM."""
    prompt = f"Context: {context}\n\nUser Query: {query}\n\nAnswer:"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI assistant."},
                  {"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']
