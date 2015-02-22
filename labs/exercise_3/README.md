Objective: Learn to read data from a csv file and analyze it in pure Python

Using the csv library (https://docs.python.org/2/library/csv.html), read in this data on classic rock songs and answer the following 2 questions:

How many songs were released in 1981?
What are the top 20 songs by playcount? (Hint: use the built-in sorted() function, documentation here: https://wiki.python.org/moin/HowTo/Sorting)


Solution:
- Read the csv file using csv DictReader
- Iterate the dict to count for songs released in 1981
- Populate a list and use sorted() method to return the top 20 songs by 'PlayCount'