n = input()
result = []

for char in n:
    if 'a' <= char <= 'z':
        result.append(chr(ord(char) - 32)) 
    elif 'A' <= char <= 'Z':
        result.append(chr(ord(char) + 32))  
    else:
        result.append(char) 

print("".join(result))
