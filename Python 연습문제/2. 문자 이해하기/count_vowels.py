text = "Python is awesome"
count = sum(1 for c in text.lower() if c in "aeiou")
print("모음 개수:", count)
