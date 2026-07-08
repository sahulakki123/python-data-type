#  method
s = "thIs is pyThon clAss"
print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.title())
print(s.swapcase())


print(s.index("Th"))
# print(s.index("th"))  # ValueError : substring not found

print(s.find("Th"))
print(s.find("th"))

print(s.replace(" ",''))

print(s.count("i"))
