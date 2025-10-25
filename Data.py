my_tuple = (1,2,3)
print(my_tuple)

tuple_1 = ("Hello", [1, "Hi", "list"], (3.4, "name"))
print(tuple_1)

tuple_2 = ("Hena", "Neena", "Katrina")
for i in tuple_2:
    print("Hello", i)

tuple_3 = ("Delhi", "Bhutan", "Gangtok")
print(tuple_3[0])
print(tuple_3[-2])

set1 = {1,2,3,3,5,6,8,8}
print(set1)
set2 = {2,3,3,4,4,6,6,9,9}
print(set2)
print("Union: ", set1.union(set2))
print("Intersection: ", set1.intersection(set2))
print("Symmetric Difference: ", set1.symmetric_difference(set2))
print("Difference: ", set1.difference(set2))