employee = {
    "name": "A",
    "age": 49,
    "type": {"developer": ["ios", "android"]},
    "permanent": True,
    100: (1, 2, 3),
    4.5: {5, 6, True, 7, 1}
}

# 1) Print length, type, and the dictionary
print("Length of dictionary:", len(employee))
print("Type of dictionary:", type(employee))
print("Dictionary:", employee)

# 2) Access the key employee["type"]["developer"]
developer_data = employee["type"]["developer"]
print("Accessed value of key 'developer':", developer_data)

# 3) Change the value of "permanent" to False
employee["permanent"] = False
print("Dictionary after changing 'permanent' to False:", employee)

# 4) Add a new key "gender" with value "male"
employee["gender"] = "male"
print("Dictionary after adding 'gender':", employee)

# 5) Remove "age" key from dictionary
employee.pop("age", None)
print("Dictionary after removing 'age':", employee)

# 6) Use keys(), values(), items()
print("Keys in the dictionary:", list(employee.keys()))
print("Values in the dictionary:", list(employee.values()))
print("Items in the dictionary:", list(employee.items()))

# 7) Iterate the dictionary using loop
print("Iterating over dictionary:")
for key, value in employee.items():
    print(f"{key}: {value}")

a = {1,3,5,8,5,2}
b = {0,False,1,5}

print(len(a))
print(len(b))

print(type(a))
print(type(b))


a.add(10)
print(a)


a.discard(8)
print(a)


union_set = a.union(b)
intersection_set = a.intersection(b)
difference_set = a.difference(b)

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)

for item in a:
    if item == 5:
        break
    print(item)


c={2,3,4}
d=a.union(c)
print(d)