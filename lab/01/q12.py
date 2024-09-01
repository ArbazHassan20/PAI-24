list1 = ["key 1", "key 2", "key 3"]  # List of keys for the dictionary
list2 = [1, 2, 3]  # List of values for the dictionary

# Initialize an empty dictionary
dictionary = {}

# Iterate over list1 and use the index to fetch corresponding values from list2
for index, key in enumerate(list1):
    dictionary[key] = list2[index]

print(dictionary)
