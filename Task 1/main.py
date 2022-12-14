# Turimas "users" masyvas. 

# Parašykite funkcijas, kurios atlikas(klaida:)) nurodytas užduotis:
# 1. funkcija "filterDogOwers" - kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins "users", kurie turi augintinį.
# 2. funkcija "filterAdults" - kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins masyvą su "users", kurie yra pilnamečiai.

users = [
  { "id": '1', "name": 'John Smith', "age": 20, "hasDog": True },
  { "id": '2', "name": 'Ann Smith', "age": 24, "hasDog": False },
  { "id": '3', "name": 'Tom Jones', "age": 31, "hasDog": True },
  { "id": '4', "name": 'Rose Peterson', "age": 17, "hasDog": False },
  { "id": '5', "name": 'Alex John', "age": 25, "hasDog": True },
  { "id": '6', "name": 'Ronald Jones', "age": 63, "hasDog": True },
  { "id": '7', "name": 'Elton Smith', "age": 16, "hasDog": True },
  { "id": '8', "name": 'Simon Peterson', "age": 30, "hasDog": False },
  { "id": '9', "name": 'Daniel Cane', "age": 51, "hasDog": True },
]

# 1. funkcija

#def filterDogOwners(users):
#  has_dog = lambda user: user["hasDog"]

#  filtered_users = filter(has_dog, users)

#  return filtered_users

#filtered_users = filterDogOwners(users)

#for user in filtered_users:
#  print(user)

#2 funkcija

#def filterAdults(users):

#  is_adult = lambda user: user["age"] >= 18

#  filtered_users = filter(is_adult, users)

#  return filtered_users

#filtered_users = filterAdults(users)

#for user in filtered_users:
#  print(user)