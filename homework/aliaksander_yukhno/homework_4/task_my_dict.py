my_dict = [
    (1, 2, 3, 4, 5, 6),
    ["a", "b", "c", "d", "e", "f"],
    {"a": 1, "b": 2, "c": (7, 7), "d": "gift", "e": [1, 2]},
    {1, 3, 3, 2, 1}
]
my_dict[1].append("g")
my_dict[1].pop(1)
my_dict[2].update({"i am a tuple": (1, 2)})
my_dict[2].pop("a")
my_dict[3].add(88)
my_dict[3].remove(3)
print(my_dict)
