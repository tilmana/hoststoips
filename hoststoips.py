import socket

records = {}

fileName = input("Filename: ")
file1 = open(fileName, "r")
file1lines = file1.readlines()
for line in file1lines:
    line = line.strip("\n")
    print(line)
    if "http://" in line or "https//" in line:
        line = line.split("//")[0]
    if line.startswith("//"):
        line = line[2::]
    if ":" in line:
        line = line.split(":")[0]
    if "/" in line:
        line = line.split("/")[0]
    ip = socket.gethostbyname(line)
    if ip not in records:
        records[ip] = line
    else:
        records[ip] = records[ip] + ", " + line

for k, v in records.items():
    print("{0}: {1}".format(k, v))
