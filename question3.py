
# function to find how many a character is repeated
s = "banana"
def count_char(s, char):
    count = 0
    for i in s:
        if i == char:
            count += 1
    return count
print(count_char(s, "a"))