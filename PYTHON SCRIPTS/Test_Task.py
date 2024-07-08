my_list = ["Sir Saeed", "M Jawad", "M Sami"]
max_length = max([len(string) for string in my_list])
print(max_length)


dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"d": 40, "e": 50, "f": 60}
dict1.update(dict2)
print(dict1)

string = "Saeed Anwar"
output = [""]
for char in string:
    new_subsets = []
    for subset in output:
        new_subsets.append(subset + char)
    output += new_subsets

print(output)
