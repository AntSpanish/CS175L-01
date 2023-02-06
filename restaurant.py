#CS175L
#Ant Spanish
#restaurant

#Constants
vegetarian=False
vegan=False
glutenFree=False

#Input
response=str(input('Is anyone in your party vegetarian? '))
if response.lower()=='yes':
    vegetarian=True

response=str(input('Is anyone in your party vegan? '))
if response.lower()=='yes':
    vegan=True

response=str(input('Is anyone in your party gluten-free? '))
if response.lower()=='yes':
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
