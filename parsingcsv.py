#parsing csv file
weather_data = []
f = open('la_weather.csv', 'r')
data = f.read()
rows = data.split('\n')
#the above part loads the file and gets it ready to work with
for row in rows:
    split_row = row.split(",")
    weather_data.append(split_row)

#this is exercise 7 in list operations, comparing two ists
weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]

weather_type_found = []
for item in weather_types:
    in_list=item in new_weather
    weather_type_found.append(in_list)

#counts how many times an element occurs in a dictionary
    
pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]
pantry_counts={}
for item in pantry:
    if item in pantry_counts:
        pantry_counts[item]=(pantry_counts[item]+1)
    else: 
        pantry_counts[item]=1
                              
