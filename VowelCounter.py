text = input()
vowels = "aeiouAEIOU"
count = 0
for i in text:
    for j in vowels:
        if i == j:
            count = count + 1

print(count)
print(type(text))
print(type(count))