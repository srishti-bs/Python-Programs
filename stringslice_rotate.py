s = "GeeksforGeeks"
d = 2

left = s[d:] + s[:d]
right = s[-d:] + s[:-d]

print("Left rotation:", left)
print("Right rotation:", right)