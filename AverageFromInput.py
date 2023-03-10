#CS-175L
#Ant Spanish
#AverageFromInput

def read_file_loop(num_file):
    total = 0
    count = 0

    for x in num_file:
        try:
            num = float(x)
        except ValueError:
            x = x.strip('\n')
            print('Non-numeric data found in file:',x)
        else:
            count+=1
            total+=num
            print(f'I read in {count} number(s)',f'\tCurrent number is: {num:.2f}', f'\tTotal is: {total:.2f}')

    return count,total
            
def average_from_values(total,count):
    if count==0:
        print('No numeric values to take average of.')
        return False
    else:
        avg = total/count
        return avg

def print_average(avg):
    print('Average (from numeric values):',f'{avg:.1f}')
    
def main():
    try:
        num_file = open("numbers.txt", 'r')

        count,total = read_file_loop(num_file)

        avg = average_from_values(total,count)

        if not avg==False:
            print_average(avg)

        num_file.close()
    except IOError:
        print('Error occurred when reading file.')
        
if __name__ == '__main__':
    main()
