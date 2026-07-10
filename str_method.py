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
print(s.count('z'))

print(s.startswith("py"))
print(s.startswith("th"))
print(s.startswith("t"))
print(s.startswith("thIs"))


s = "thIs is pyThon clAss123"

print(s.endswith('py'))
print(s.endswith('ss'))
print(s.endswith('clAss'))
print(s.endswith('clAss'))
print(s.endswith('clAss'))


s = "thIs is pyThon clAss123"
print(s.split())
print(s.split('i'))
print(s.split('i',1))
print(s.split('i',0))
print(s.split('i',10))
print(s.split('i',10))



s1 ="python"
s2 = "java"
s3 = "PHP"

l = [s1,s2,s3]
# syntex:- "kisse join karna hai ".join(argument)
# print(" ".join(s1,s2,s3))
print(" ".join(l))
print("-".join(l))
print("".join(l))

s = ""

# l = [10,20,30, 'python','java']
# print(s.join(l))

l = [10,20,30, 'python','java']
print(s.jion(l))
