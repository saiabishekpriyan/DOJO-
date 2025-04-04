n = input()
result = " "


uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"

for char in n:
    if char in lowercase:  
        index = lowercase.index(char)  
        result += uppercase[index] 
    elif char in uppercase:  
        index = uppercase.index(char)  
        result += lowercase[index]  
    else:
        result += char  

print(result)