import string
input_file_path = 'C:/Users/micha/OneDrive/Documents/2016 cods/PALm/Abstract.txt'
output_file_path = 'C:/Users/micha/OneDrive/Documents/2016 cods/PALm/Abstract.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file:
    text = input_file.read()

text_without_punctuation = ''.join([char for char in text if char not in string.punctuation])

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(text_without_punctuation)

print(f"Text without punctuation saved to {output_file_path}")

