#CS175L
#Ant Spanish
#restaurant

#Constants
vegetarian=False
vegan=False
glutenFree=False
retry=False
loop=True

#Input2.0
while loop:
    response=str(input('\nIs anyone in your party vegetarian? '))
    if not(response.lower()=='yes' or response.lower()=='no'):
        retry=True
    while (retry==True):
        response=input('Please enter \'yes\' or \'no\': ')
        if not(response.lower()=='yes' or response.lower()=='no'):
            retry=True
        else:
            retry=False
    if (response.lower()=='yes'):
        vegetarian=True

    response=str(input('Is anyone in your party vegan? '))
    if not(response.lower()=='yes' or response.lower()=='no'):
        retry=True
    while (retry==True):
        response=input('Please enter \'yes\' or \'no\': ')
        if not(response.lower()=='yes' or response.lower()=='no'):
            retry=True
        else:
            retry=False
    if (response.lower()=='yes'):
        vegan=True

    response=str(input('Is anyone in your party gluten-free? '))
    if not(response.lower()=='yes' or response.lower()=='no'):
        retry=True
    while (retry==True):
        response=input('Please enter \'yes\' or \'no\': ')
        if not(response.lower()=='yes' or response.lower()=='no'):
            retry=True
        else:
            retry=False
    if (response.lower()=='yes'):
        glutenFree=True

#Output
    print('\nHere are your restaurant choices.')
    if not vegetarian and not vegan and not glutenFree:
        print('Joe\'s Gourment Burgers')
    if not vegan:
        print('Main Street Pizza Company')
    print('Corner Café')
    if not vegan and not glutenFree:
        print('Mama\'s Fine Italian')
    print('The Chef\'s Kitchen')

#Loop Statement
    yesOrNo=str(input('\nEnter \'yes\' if you would like to do another restaurant search (enter \'no\' to end): '))
    if not (yesOrNo.lower()=='yes' or yesOrNo.lower()=='no'):
        retry=True
    while (retry==True):
        yesOrNo=str(input('Please enter \'yes\' or \'no\': '))
        if not (yesOrNo.lower()=='yes' or yesOrNo.lower()=='no'):
            retry=True
        else:
            retry=False
    if (yesOrNo.lower()=='yes'):
        loop=True
    elif (yesOrNo.lower()=='no'):
        loop=False
