from transformers import pipeline

# Set up the text generation pipeline using GPT-2
generator = pipeline("text-generation", model="gpt2")

# Function to get a generated response for a given prompt
def get_llm_response(prompt):
    result = generator(prompt, max_length=150, do_sample=True)
    return result[0]["generated_text"]

# Optional: Keep your existing print function if you want to print in a formatted way
def print_llm_response(response):
    print("LLM Response:\n", response)
