dic = {
    "user" : "user@mail.com",
    "Rohit" : "rohit@mail.com",
    "Rajnish": "rajnish@mail.com",
    "Ritik" : "ritik@mail.com"
}


def adding_mister(item):
    key, value = item
    return ("Mr. "+key, value)



map_obj = list(map(adding_mister, dic.items()))
new_dict = dict(map_obj)

print(new_dict)




