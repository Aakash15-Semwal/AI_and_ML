from pathlib import Path

Path.mkdir(Path.cwd() / "Helper", parents = True, exist_ok = True)

file = open(Path.cwd() / "Helper/random.txt", 'w', encoding='utf-8')
file.write("Hello World \n")
file.close()

file = open(Path.cwd() / "Helper/random.txt", 'a', encoding='utf-8')
file.write("How are you?\n")
file.close()

file = open(Path.cwd() / "Helper/random.txt", 'r', encoding='utf-8')
print(file.read())
file.close()