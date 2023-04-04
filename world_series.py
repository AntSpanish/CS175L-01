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
    print(world_series)
    while running:
        team_name=input('\nEnter the name of the team (or q to quit). ').lower()
        if team_name=='q':
            print('Goodbye.')
            running=False
        else:
            team_in_world_series=[line for line in world_series if team_name in line.lower()]
            print(f'The {team_name} won the world series {len(team_in_world_series)} times between 1903 and 2009.')
    
if __name__ == '__main__':
    main()
