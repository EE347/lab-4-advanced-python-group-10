import csv

def write_to_csv():

    with open('task5.csv', 'w',newline='') as file:
       writer = csv.writer(file)


       while True:
           
           name = input("ENTER NAME OR TYPE QUIT TO STOP")


           if name.lower() =='quit':
               break
           


           writer.writerow([name])

def read_from_csv():

    with open('task5.csv', 'r') as file:
        reader = csv.reader(file)

        print("\nNames in CSV: ")

        for row in reader:
            print(row[0])

if __name__ == '__main__':
   
   write_to_csv()

   read_from_csv()