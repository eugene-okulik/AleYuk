my_dict = {
    "tuple": (1, 2, 3, 4, 5, 6),
    "list": ["a", "b", "c", "d", "e", "f"],
    "dict": {"a": 1, "b": 2, "c": (7, 7), "d": "gift", "e": [1, 2]},
    "set": {1, 7, 3, 2, 99}
}
print(my_dict["tuple"][-1])
my_dict["list"].append("g")
my_dict["list"].pop(1)
my_dict["dict"].update({"('i am a tuple'),": 1})
my_dict["dict"].pop("a")
my_dict["set"].add(88)
my_dict["set"].remove(3)
print(my_dict)
