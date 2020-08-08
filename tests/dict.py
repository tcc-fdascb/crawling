data = [
    {'rec20': [0, 1, 2, 3]},
    {'rec21': [4, 5, 6, 7]}
]

for dt in data:
    for key in dt.keys():
        print(key)
        for value in dt.get(key):
            print(value)
