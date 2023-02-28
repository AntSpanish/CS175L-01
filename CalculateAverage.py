#CS-175L
#Ant Spanish
#CalculateAverage

def calc_average(total):
    avg=total/5
    return avg
    

def determine_grade(s1):
    if s1>=90:
        s1='A'
    elif s1>=80:
        s1='B'
    elif s1>=70:
        s1='C'
    elif s1>60:
        s1='D'
    else:
        s1='F'
    return s1


def repeat():
    choice=input('\nWould you like to make another calculation? (y/n) ')
    choice = choice.lower()
    while not (choice=='y' or choice=='n'):
        choice=input('Please enter y for yes or n fo no. ')
        choice = choice.lower()
    if (choice=='y'):
        main()
    elif (choice=='n'):
        print('\nGoodbye.')
    

def main():
    total=0
    
    score1=float(input('\nEnter score 1: '))
    while score1<0 or score1>100:
        score1=float(input('Enter a valid score: '))
    else:
        total+=score1
        s1=determine_grade(score1)
        
    score2=float(input('Enter score 2: '))
    while score2<0 or score2>100:
        score2=float(input('Enter a valid score: '))
    else:
        total+=score2
        s2=determine_grade(score2)
    
    score3=float(input('Enter score 3: '))
    while score3<0 or score3>100:
        score3=float(input('Enter a valid score: '))
    else:
        total+=score3
        s3=determine_grade(score3)
    
    score4=float(input('Enter score 4: '))
    while score4<0 or score4>100:
        score4=float(input('Enter a valid score: '))
    else:
        total+=score4
        s4=determine_grade(score4)
    
    score5=float(input('Enter score 5: '))
    while score5<0 or score5>100:
        score5=float(input('Enter a valid score: '))
    else:
        total+=score5
        s5=determine_grade(score5)
    
    avg=calc_average(total)
    s6=determine_grade(avg)
    
    print('\nScore\t\tNumeric Grade\t\tLetter Grade')
    print('—————————————————————————————————————————————————————————')
    print(f'{"Score 1:":<16}{score1:<6.1f} {s1:>19}')
    print(f'{"Score 2:":<16}{score2:<6.1f} {s2:>19}')
    print(f'{"Score 3:":<16}{score3:<6.1f} {s3:>19}')
    print(f'{"Score 4:":<16}{score4:<6.1f} {s4:>19}')
    print(f'{"Score 5:":<16}{score5:<6.1f} {s5:>19}')
    print(f'{"Average Score:":<15} {avg:<6.1f} {s6:>19}')

    repeat()

main()
