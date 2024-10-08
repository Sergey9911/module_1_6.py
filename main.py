my_dict= {"Name": 'Sergey', "year_of_birth": 1991}
print(my_dict)
print(my_dict["Name"])
my_dict["year_of_birth"] = 2002
print(my_dict)
my_dict.update({"Name": 'Igor',
                "year_of_birth": 2021})
print(my_dict)
del my_dict["Name"]
print(my_dict)

my_set = {10, 'Serg', True, False, 16, 10, True, 'Serg'}
print(my_set)
list_ = [10,16]
print(set(list_))
print(list_.remove(10))
print(list_)
