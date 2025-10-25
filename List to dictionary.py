def convert(x):
    results = {}
    for i in x:
        results[i[0]] = i[1:]
    return results

students = [[1, "Renesha", "V"], [2,"Trishika", "VI"], [3, "Prajakta", "VII"]]

print("Original List")
print(students)
print("Converted Dictionary")
print(convert(students))