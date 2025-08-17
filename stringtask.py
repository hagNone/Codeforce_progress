# codeforces 118A - String Task

s = input().lower()   # convert to lowercase
vowels = "aoyeui"     # all vowels in the problem statement

resul= ""
for c in s:
    if c not in vowels:   # if consonant
        resul += "." + c

print(resul)
