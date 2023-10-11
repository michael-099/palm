import google.generativeai as palm

palm.configure(api_key='AIzaSyD4iOipAbxMSKI3ESrqCpNx7L68sg9_SK0')

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

exposure_percent=40
weight=150
height=1.70
history_of_stroke="yes "
family_history_of_stroke="yes"
physical_activity_level="sedentary"
diet="balaced "
systolic_blood_pressure=50
diastolic_blood_pressure=60

medical_prompt = f"""
As an expert in stroke disease prevention, you play a crucial role in advising and developing
personalized diet and exercise plans for patients based on their unique profiles. Your insights 
are backed by extensive data analysis and a powerful model that calculates the risk of stroke.
User Profile:
Weight: {weight} kg
Height: {height} meters
Risk of a Stroke: {exposure_percent}%
History of Stroke: {history_of_stroke}
Family History of Stroke: {family_history_of_stroke}
Physical Activity Level: {physical_activity_level}
Diet: {diet}
Systolic Blood Pressure: {systolic_blood_pressure} mmHg
Diastolic Blood Pressure: {diastolic_blood_pressure} mmHg
It's essential to emphasize that the risk of stroke provided is based on meticulous data analysis and should be taken seriously.
Taking into account the user's profile, it's commendable to acknowledge the positive aspects but also address areas that require improvement.
Please provide a comprehensive set of recommendations, highlighting the favorable aspects of the user's profile while pinpointing areas that necessitate change.
Please offer comprehensive recommendations tailored to the user's profile. 
Include specific guidance on lifestyle changes,dietary adjustments, and exercise routines that will not only promote better overall health but also reduce the risk of stroke effectively.
"""
response = palm.generate_text( 
            model=model,
            prompt=medical_prompt,
            max_output_tokens=800,
        ).result
print(response)
    