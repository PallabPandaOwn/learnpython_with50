# it is a mutable datatypes

my_list = [1,2,3,4,5]


my_list.append(6)
print(f"my list :- {my_list}")
print(f"ID of my_list :- {id(my_list)}")
my_list.remove(3)
print(f"my list :- {my_list}")
print(f"ID of my_list :- {id(my_list)}")