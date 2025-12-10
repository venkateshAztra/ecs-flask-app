from helper_functions import get_llm_response, print_llm_response
# # List of tasks to send to the LLM
# tasks = [
#     "Write a short motivational quote about learning.",
#     "Generate a funny tweet about AI.",
#     "Write a 3-line poem about sunrise.",
#     "Summarize the plot of 'The Matrix'.",
#     "Compose a thank-you email for attending a meeting."
# ]

# # Loop through each task and generate + print a response
# for task in tasks:
#     response = get_llm_response(task)
#     print_llm_response(response)
#     print("-" * 50)  # separator for readability


#ice cream flavor example
ice_cream_flavors = [
    "Vanilla",
    "Chocolate",
    "Strawberry",
    "Mint Chocolate Chip"
]

for flavor in ice_cream_flavors:
    prompt = f"""For the ice cream flavor listed below, 
    provide a captivating description that could be used for promotional purposes.

    Flavor: {flavor}

    """
    print_llm_response(prompt)