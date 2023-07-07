"""
import json

input_file=open('D:\\Rasa\\API_Weather_Ver1\\citylist.txt', 'r', encoding='utf-8')
output_file=open('D:\\Rasa\\API_Weather_Ver1\\city.txt', 'w', encoding='utf-8')
json_decode=json.load(input_file)

for item in json_decode:
    my_dict={}
    my_dict['name']=item.get('name')
    print (my_dict)
    output_file.write(item.get('name'))
    output_file.write("\n")

output_file.close()"""

# Insert normal .txt/.csv path here
file = open('D:\\Rasa\\API_Weather_Ver1\\city.txt', "r", encoding='utf-8')

# Splits each row
lines = file.read().splitlines()
n = 0

# Insert target output path here
file2 = open('D:\\Rasa\\API_Weather_Ver1\\city.yml', "w", encoding='utf-8')

# Writes the headers(?), remember to change the lookup name
file2.write("version: \"2.0\"\nnlu:\n  - lookup: location  \n    examples: |\n")

# Adds indent and dash to each line
for line in lines:
    file2.write("      - " + str(line) + "\n")

# Closes the files
file.close()
file2.close()