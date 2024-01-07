filename = 'learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    learning_python_string = ''
    for line in lines:
        learning_python_string += line
    #contents = file_object.read()
print(learning_python_string)
modificando_c = learning_python_string.replace('Python', 'C')
print(modificando_c)
#print(contents)