#CS-175L
#Ant Spanish
#AverageFromInput

def main():
    num_file = open("numbers.txt", 'r')

    total=0
    count=0
    
    for x in num_file:
        count+=1
        num=int(x)
        total+=num
        print(f'I read in {count} number(s)', f'\tCurrent number is: {num:.2f}', f'\tTotal is: {total:.2f}')

    avg=total/count

    print(f'Average: {avg:.1f}')

    num_file.close()

if __name__ == '__main__':
    main()
