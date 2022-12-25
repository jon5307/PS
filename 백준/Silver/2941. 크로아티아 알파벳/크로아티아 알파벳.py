alphabet = input()
for i in ("c=","c-","dz=","d-","lj","nj","s=","z="):
    alphabet = alphabet.replace(i,"*")
print(len(alphabet))