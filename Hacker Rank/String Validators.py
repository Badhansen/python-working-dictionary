str=input()

print(any([char.isalnum() for char in str]))
print(any([char.isalpha() for char in str]))
print(any([char.isdigit() for char in str]))
print(any([char.islower() for char in str]))
print(any([char.isupper() for char in str]))
