dict = {
    "name":"Swaroop",
    "age":21
}
print(dict)
print(type(dict))
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict["name"])
print(dict["age"])
dict["name1"] = "Faran"     #adding new element
print(dict)
dict.pop("name")    #key removed
print(dict)