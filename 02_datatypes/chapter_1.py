sugar_amount = 2
print(f"I have {sugar_amount} cups of sugar.")
print(f"ID of sugar_amount: {id(sugar_amount)}")

sugar_amount = 3
print(f"I have {sugar_amount} cups of sugar.")
print(f"ID of sugar_amount: {id(sugar_amount)}")


# flour_amount = 3
# print(f"I have {flour_amount} cups of flour.")
# print(f"ID of flour_amount: {id(flour_amount)}")

# mix = set(["sugar", "flour", "eggs"])

# print(f"I will mix:, {mix}")

# print(f"ID of mix:", id(mix))

spices={"Ginger","Cardamom","Cinnamon"}
print(f"ID of spices:", id(spices))
print(f"I will add spices:, {spices}")

spices.add("Nutmeg")
print(f"Updated spices set: {spices}")
print(f"ID of updated spices:", id(spices))
