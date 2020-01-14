import itertools
player = ['X','O',None]
all_possible_states = [[list(i[0:3]),list(i[3:6]),list(i[6:10])] for i in itertools.product(player, repeat = 9)]

print(all_possible_states)