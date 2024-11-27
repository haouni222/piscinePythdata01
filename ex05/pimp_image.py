from load_image import ft_load


def ft_invert(array):
    return 255 - array

def ft_red(array):
    data = array.copy()
    i = 0
    while i < len(data): 
        data[i] = data[i] * [1, 0, 0]  
        i += 1
    print(data)
    return data

def ft_green(array):
    data = array.copy()
    i = 0
    while i < len(data): 
        j = 0
        while j < len(data[i]):
            data[i][j][0] -= data[i][j][0]
            data[i][j][2] -= data[i][j][2]
            j+=1
        i += 1
    print(data)
    return data

def ft_blue(array):
    data = array.copy()
    i = 0
    while i < len(data): 
        j = 0
        while j < len(data[i]):
            data[i][j][0] = 0
            data[i][j][1] = 0
            j+=1
        i += 1

    print(data)
    return data

def ft_grey(array):
    data = array.copy()
    for i in range(len(data)):
        for j in range(len(data[i])):
            gray_value = data[i][j][0] / 3 + data[i][j][1] / 3 + data[i][j][2] / 3
            data[i][j][0] = gray_value
            data[i][j][1] = gray_value
            data[i][j][2] = gray_value
    return data