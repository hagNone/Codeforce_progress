#codeforeces 4A watermelon problem solution
word = str(input())   # take input

if len(word) > 10:   # check if word is longer than 10 chars
    # print first + (middle count) + last
    print(word[0] + str(len(word) - 2) + word[-1])
else:
    print(word)   # otherwise, just print the word