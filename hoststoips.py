import socket

records = {}

fileName = input("Filename: ")
file1 = open(fileName, "r")
file1lines = file1.readlines()
for line in file1lines:
  line = line.strip("\n")
  if "http://" in line or "https//" in line:
    line = line.split("//")[0]
  if line.startswith("//"):
    line = line[2::]
  if ":" in line:
    line = line.split(":")[0]
  if "/" in line:
    line = line.split("/")[0]
  try:
    ip = socket.gethostbyname(line)
  except Exception as e:
    if not "N/A" in records.keys():
      records["N/A"] = line
    else:
      records["N/A"] = records["N/A"] + ", " + line
    continue
  if ip not in records:
    records[ip] = line
  else:
    if line in records[ip].split(", "):
      continue
    records[ip] = records[ip] + ", " + line

for k, v in records.items():
  print("{0}: {1}".format(k, v))
