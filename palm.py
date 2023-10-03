# # import pprint 
# # import google
# # import google.generativeai as palm

# # palm.configure(api_key='AIzaSyD4iOipAbxMSKI3ESrqCpNx7L68sg9_SK0')
# # models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
# # model = models[0].name
# # print(model)
# # prompt = """
# # You are an expert at solving word problems.

# # Solve the following problem:

# # I have three houses, each with three cats.
# # each cat owns 4 mittens, and a hat. Each mitten was
# # knit from 7m of yarn, each hat from 4m.
# # How much yarn was needed to make all the items?

# # Think about it step by step, and show your work.
# # """

# # # completion = palm.generate_text(
# # #     model=model,
# # #     prompt=prompt,
# # #     temperature=0,
# # #     # The maximum length of the response
# # #     max_output_tokens=800,
# # # )

# # # print(completion.result)
# # # calc_prompt = f"""
# # # Please solve the following problem.

# # # {prompt}

# # # ----------------

# # # Important: Use the calculator for each step.
# # # Don't do the arithmetic in your head. 

# # # To use the calculator wrap an equation in <calc> tags like this: 

# # # <calc> 3 cats * 2 hats/cat </calc> = 6

# # # ----------------

# # # """
# # calc_prompt = f"""
# # Please solve the following problem.

# # {prompt}

# # ----------------

# # Important:replay not in my domain if the question is not relaated to medicine or health 


# # ----------------

# # """

# # equation=None
# # while equation is None:
# #     completion = palm.generate_text(
# #         model=model,
# #         prompt=calc_prompt,
# #         stop_sequences=['</calc>'],
# #         # The maximum length of the response
# #         max_output_tokens=800,
# #     )

# #     try:
# #         response, equation = completion.result.split('<calc>', maxsplit=1)
# #     except Exception:
# #         continue
# import google.generativeai as palm

# # Configure with your API key
# palm.configure(api_key='AIzaSyD4iOipAbxMSKI3ESrqCpNx7L68sg9_SK0')

# # Retrieve and select a generative AI model that supports 'generateText'
# models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
# model = models[0].name

# # Define your prompt
# prompt = """
# You are an expert at solving word problems.

# Solve the following problem:

# I have three houses, each with three cats.
# each cat owns 4 mittens, and a hat. Each mitten was
# knit from 7m of yarn, each hat from 4m.
# How much yarn was needed to make all the items?

# Think about it step by step, and show your work.
# """

# # Define the prompt with the health-related filter
# calc_prompt = f"""
# Please solve the following problem.

# {prompt}

# ----------------

# Important: Replay out of domain if the question is related to medicine or health.

# ----------------

# """

# # Generate text with the modified prompt
# completion = palm.generate_text(
#     model=model,
#     prompt=calc_prompt,
#     max_output_tokens=800,
# )

# try:
#     response = completion.result

#     # Check if the response contains health-related keywords
#     if 'medicine' not in response.lower() and 'health' not in response.lower():
#         # Response is not related to health, continue with your logic
#         print(response)
# except Exception as e:
#     print("Exception:", str(e))
import google.generativeai as palm

# Configure with your API key
palm.configure(api_key='AIzaSyD4iOipAbxMSKI3ESrqCpNx7L68sg9_SK0')

# Retrieve and select a generative AI model that supports 'generateText'
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

# Define a prompt for medical-related questions
medical_prompt = """
You are an expert in medical matters.

Please ask your medical question, and I'll do my best to provide an answer.
"""
medical_response = palm.generate_text(
    model=model,
    prompt=medical_prompt,
    max_output_tokens=800,
).result

while True:
    user_input = input("Ask a question: ")
    if 'medicine' in user_input.lower() or 'health' in user_input.lower() or 'stroke ' in user_input.lower() or 'hey' in user_input.lower() or 'hello' in user_input.lower() or 'hi' in user_input.lower() :
        response = palm.generate_text( 
            model=model,
            prompt=user_input,
            max_output_tokens=800,
        ).result
        print(response)
    else:
        print("I can only answer medical-related questions. Please ask a stroke related question.")
