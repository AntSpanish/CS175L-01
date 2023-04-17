#Ant Spanish
#CS-l75L
#expensePieChart

import matplotlib.pyplot as plt

def main():
    try:
        name_list=[]
        num_list=[]
        
        with open("expenses.txt") as f:
            for line in f:
                name, number = line.strip().split("\t")
                try:
                    number = int(number)
                    name_list.append(name)
                    num_list.append(number)
                except ValueError:
                    pass

        plt.pie(num_list,labels=name_list)
        plt.title('Monthly Expenses')
        
        plt.show()
        
    except IOError:
        print('ERROR: File not found!')

if __name__ == "__main__":
    main()
