str='Python Programming'

print(str[0:6])
print(str[:9])
print(str[-11:])
print(str[::2])
print(str[::-1])


words =["Python","is","awesome"]
sentence=" ".join(words) 
print(sentence)


path_parts=["user","local","awesome"]
full_path ="/".join(path_parts)
print(full_path)