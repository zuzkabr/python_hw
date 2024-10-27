import csv
import json



# 1) prevest na seznam slovniku

def read_file_to_dicts(file_path, delimiter=","):
    list_of_dicts = []
    
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        text = csv.DictReader(csvfile, delimiter=delimiter)
        
        for row in text:
            list_of_dicts.append(row)
    
    return list_of_dicts

tsv_file_path = "netflix_titles.tsv"
tsv_data = read_file_to_dicts(tsv_file_path, delimiter="\t")




# 2) vybrat jenom konkretni klice - smazat nerelevantni 

keys_to_drop = [
    "TCONST", 
    "TITLETYPE", 
    "ORIGINALTITLE", 
    "ISADULT", 
    "ENDYEAR", 
    "RUNTIMEMINUTES", 
    "AVERAGERATING", 
    "NUMVOTES", 
    "TITLETYPE_NEW", 
    "SHOW_ID", 
    "TYPE", 
    "TITLE", 
    "COUNTRY", 
    "DATE_ADDED", 
    "RELEASE_YEAR", 
    "RATING", 
    "DURATION", 
    "LISTED_IN", 
    "DESCRIPTION"
    ]

for dict_item in tsv_data:
    for key in keys_to_drop:
        dict_item.pop(key)
        



# 3) prejmenovat klice

key_names = {
    "PRIMARYTITLE": "title",
    "STARTYEAR": "decades",
    "GENRES": "genres",
    "DIRECTOR": "directors",
    "CAST": "cast",
    }

for dict_item in tsv_data:
    for old_key, new_key in key_names.items():
        if old_key in dict_item:
            dict_item[new_key] = dict_item.pop(old_key)




# 4) prevest herce, rezisery a zanry na seznam, prazdne hodnoty nechat jako prazdny seznam

keys_to_split = ["genres", "directors", "cast"]

for dict_item in tsv_data:
    for key in keys_to_split:
        if key in dict_item:
            dict_item[key] = dict_item[key].split(",")



# 5) roky prevest na dekady

key_to_change = "decades"

for dict_item in tsv_data:
    if key_to_change in dict_item:
        year = int(dict_item[key_to_change])
        decade = year - (year % 10)
        dict_item[key_to_change] = decade



with open("hw02_output.json", mode="w", encoding ="utf-8") as file:
    json.dump(tsv_data, file, indent=4)