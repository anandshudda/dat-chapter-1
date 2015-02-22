import csv

# Read the file using DictReader
f = open('rock.csv', "r")
dict = csv.DictReader(f)

# Count variable to store "How many songs were released in 1981?"
count_released_1981 = 0

# Create a list for sorting to answer: "What are the top 20 songs by playcount?"
list = []

# Loop to populate the list and to count for the songs released in 1981
for row in dict:
    if (row['Release Year'] == '1981'):
        count_released_1981 = count_released_1981 + 1
    list.append(row)

# Sort list by PlayCount
sorted_list = sorted(list, key=lambda song: int(song['PlayCount']), reverse=True)   

print "Number of songs released in 1981: ", count_released_1981, '\n' 

print "Top 20 songs by play count: ", '\n' 

for n in xrange(0, 20):
    print n+1, ":", sorted_list[n]['Song Clean'], ":", sorted_list[n]['PlayCount']


