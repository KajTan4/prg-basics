person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

print(person["name"])
print(person["hobby"])
print(person)
person["surname"] = "Nowak"
print(person["surname"])
person["married"] = False
print(person["married"])
person.update({"gender":"male"})
print(person)
person.update({"hobby":["bicycle","swimming","excursions"]})
print(person)