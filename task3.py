def append():

    name = input("ENTER NAME")


    with open('task3.txt', 'a') as file:
        file.write(name +'\n')


if __name__ == '__main__':

    for _ in range(3):
        append()        