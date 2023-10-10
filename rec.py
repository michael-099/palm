import google.generativeai as palm

# Configure with your API key
palm.configure(api_key='AIzaSyD4iOipAbxMSKI3ESrqCpNx7L68sg9_SK0')

# Retrieve and select a generative AI model that supports 'generateText'
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

# Define a prompt for medical-related questions
exposure_percent=40
weight=50
height=1.70

medical_prompt = """
Provide personalized advice for stroke prevention based on the user's profile:

User Profile:

Weight:{weight} kg
Height: {height}meters
Risk of a Stroke:{exposure_percent}%
Please offer recommendations on what the user can 
do to reduce their risk of a stroke, taking into 
account their weight, height, and the elevated risk
factor. Include specific lifestyle changes, dietary suggestions,
and any relevant exercise routines to promote 
better health and stroke prevention
"""
medical_response = palm.generate_text(
    model=model,
    prompt=medical_prompt,
    max_output_tokens=800,
).result

while True:
    # user_input = input("Ask a question: ")
    # if 'medicine' in user_input.lower() or 'health' in user_input.lower() or 'stroke ' in user_input.lower() or 'hey' in user_input.lower() or 'hello' in user_input.lower() or 'hi' in user_input.lower() :
    response = palm.generate_text( 
            model=model,
            prompt=medical_prompt,
            max_output_tokens=800,
        ).result
    print(response)
    