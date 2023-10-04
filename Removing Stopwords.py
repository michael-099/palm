import nltk
from nltk.corpus import stopwords

# Download NLTK stopwords if not already downloaded
nltk.download('stopwords')

# Define the path to the input text file
input_file_path = 'input.txt'  # Replace with your file path

# Read the text from the input file
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    text = input_file.read()

# Tokenize the text
words = text.split()

# Remove stopwords
filtered_words = [word for word in words if word.lower() not in stopwords.words('english')]

# Join the filtered words back into a sentence
filtered_text = ' '.join(filtered_words)

# Define the path to the output file
output_file_path = 'output.txt'  # Replace with your desired output file path

# Write the filtered text to the output file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(filtered_text)

print("Stopwords removed and saved to output.txt")
