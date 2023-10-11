import google.generativeai as palm
palm.configure(api_key='AIzaSyD4iOipAbxMSKI3ESrqCpNx7L68sg9_SK0')
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
user_input=""
while True:
    user_input = input("Ask a question: ")
    medical_prompt = f"""
         You are  NuroGen a health assistant for patients, especially on stroke.
         You will be given a question below, and you are not allowed to answer a question that is not related to health and medicine
         if the question is greeting you are alowed to answer 
         if you are asked who you are or what you say that you are  NuroGen a health assistant
         just tell the user that you cannot answer a question not related to health . 
         If the question is related to health, give a response.
         The question:{user_input}
         """
    response = palm.generate_text( 
            model=model,
            prompt=medical_prompt,
            max_output_tokens=800,
        ).result
    print(response)