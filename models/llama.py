# models/llama.py



import requests

def query_llama(prompt):
    """
    Sends a prompt to the locally running LLaMA 3 container and returns the response.

    Assumes Ollama or compatible LLaMA 3 server is running at http://localhost:11434.
    """
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",  # Make sure your model is named 'llama3' in Ollama
                "prompt": prompt,
                "stream": False
            }
        )
        response.raise_for_status()
        return response.json().get("response", "").strip()
    
    except requests.RequestException as e:
        print(f"Error connecting to LLaMA 3 API: {e}")
        return None
