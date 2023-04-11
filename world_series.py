# Ant Spanish
# CS-175L
# world_series

def world_series_winners_list(file):
    world_series_winners=[]
    for line in file:
        line = line.rstrip('\n')
        world_series_winners.append(line)
    return world_series_winners 
    
def main():
    running=True
    file=open(r'C:\Users\17326\OneDrive\Documents\Python Files\WorldSeriesWinners.txt')
    world_series=world_series_winners_list(file)
    while running:
        team_name=input('\nEnter the name of the team (or q to quit). ').lower()
        if team_name=='q':
            print('Goodbye.')
            running=False
        else:
            appear_once=[]
            team_in_world_series=[line for line in world_series if team_name in line.lower()]
            team_in_world_series.sort()
            for line in team_in_world_series:
                if line not in appear_once:
                    appear_once.append(line)
            print(f'\nTeam list:')
            for line in appear_once:
                print(f'{line:>27}')
            print('')
            choice_specific=input('Choose a specific team. ')
            specific_team=[line for line in team_in_world_series if line.lower()==choice_specific.lower()]
            
            print(f'The {choice_specific} won the world series {len(specific_team)} times between 1903 and 2009.')
    
if __name__ == '__main__':
    main()
