with open("t.txt", "r") as f:
    lines = f.readlines()

f = open("o.txt", "w")
for line in lines:
    f.write(line[0:9] + " " + line[-12:].strip() + " " + line[10:-12].strip() + "\n")