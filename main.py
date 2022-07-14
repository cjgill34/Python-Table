filename = "tabletest.txt"
with open(filename, "r") as myfile:
    words = []
    for line in myfile.readlines():
        _words = line.rstrip("\n").split(" ")
        for word in _words:
            if word.startswith("tbl"):
                words.append(word)
print(words)