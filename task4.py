def read_print():
   with open('task3.txt', 'r') as file:
      names = file.readlines()


      for name in names:
         print(name.strip())


if __name__ == '__main__':
   
   read_print()