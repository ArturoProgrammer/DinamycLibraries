import dis

f = open("LibsCompiler/DLA.py", "r")
print("\n\n\n")


for i in f.readlines():
	i = i.replace("\t", "")
	print(i)
	print("***", dis.dis(i))

f.close()