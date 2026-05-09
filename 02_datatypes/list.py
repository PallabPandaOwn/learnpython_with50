# it is a mutable datatypes

# my_list = [1,2,3,4,5]


# my_list.append(6)
# print(f"my list :- {my_list}")
# print(f"ID of my_list :- {id(my_list)}")
# my_list.remove(3)
# print(f"my list :- {my_list}")
# print(f"ID of my_list :- {id(my_list)}")


#######################
# Shoping List project

my_cart = ["apple", "bananas" , "milk"]

print(f"My shoping list :- {my_cart}")

my_cart.append("bread")
print(f"My shoping list :- {my_cart}")

my_cart.insert(0 , "ketchup")

print(f"My shoping list :- {my_cart}")

my_cart.remove("bananas")
print(f"My shoping list :- {my_cart}")

removed_item = my_cart.pop()
print(f"My shoping list :- {my_cart}")
print(f"Removed item :- {removed_item}")

my_cart.extend(["rice", "butter"])
print(f"My shoping list :- {my_cart}")

my_cart.sort()
print(f"My shoping list :- {my_cart}")

my_cart.reverse()
print(f"My shoping list :- {my_cart}")

my_cart2 = ["juice", "jam"]

final_cart = my_cart + my_cart2
final_cart.sort()
print(f"My shoping result :- {final_cart}")


duplicate_list = final_cart * 2
print(f"My duplicate list :- {duplicate_list}")



