customer = {
    "name": "Hassan",
    "age":30,
    "is_verified": True
}
# print(customer["name"])
print(customer.get("birthday"))
print(customer.get("birthday","Jan 1 1991"))