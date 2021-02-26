import json
import yaml

# read json file
myjsonfile = open('C:/Users/37441/Desktop/HTI-1-Practical-Group-1-Mher-Barseghyan/json_folder/json_files/task_urls.json', 'r')
json_data = myjsonfile.read()

# parse
obj = json.loads(json_data)

# list = obj['items']
# for i in range(len(list)):
#     print(list[i].get('url'))

file = open("output_file.txt", "w")
yaml.dump(obj, file)
file.close()
