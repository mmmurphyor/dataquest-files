f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])
final_data = []
for city in rows:
    split_list = city.split(',')
    final_data.append(split_list)
print(final_data[0:5])
 '''created a list of lists by doing this'''
print(five_elements)
cities_list =[]
for row in five_elements:
    city = (row[0])
    cities_list.append(city)

#creates alist of strings that has the city names from each list in five_elements
