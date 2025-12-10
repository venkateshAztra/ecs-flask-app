from helper_functions import print_llm_response, get_llm_response

context = """
India is a country in South Asia. Its capital is New Delhi.
Narendra Modi is the Prime Minister of India.
The Taj Mahal is located in Agra.
"""
name = "india"
# print_llm_response("What is the capital of India?", context)
# print_llm_response("Where is the Taj Mahal?", context)
# print_llm_response("Who is the Prime Minister of India?", context)

print_llm_response("singa song for india{name}", context)
