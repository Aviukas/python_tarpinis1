# Turimas "audi" dict.

# Parašykite funkciją "showObjectKeys", kuri kaip argumentą priims objektą 
# ir grąžins visus jo "values" list'e.

audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}
 
def showObjectKeys(obj):
  values = []

  for key in obj.keys():
    values.append(obj[key])

  return values

audi_values = showObjectKeys(audi)

print("Values of audi object:", audi_values)