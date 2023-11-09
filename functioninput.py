import os 

def data_input(file_path) :
    data = []
    with open(file_path, 'r') as file:
        for line in file : 
            data.append(line.strip())
    for i in range (len(data)):
        data[i] = (data[i])
    data = list(set(data))
    with open(file_path, 'w') as file:
        for i in range(len(data)) :
            file.write(str(data[i])+'\n')

    return data