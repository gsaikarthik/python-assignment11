with open("sample.txt") as f:
    with open("sample1.txt", "w") as f1:
        for line in f:
            f1.write(line)
f=open("sample.txt")
print("this content of old file")
print(f.read())
print("this the content of copied file")
f1=open("sample1.txt")
print(f1.read())       
