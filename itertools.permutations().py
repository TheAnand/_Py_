from itertools import permutations

Str , N = input.split()
print(*[''.join(i) for i in permutations(sorted(Str) , int(N))] , sep='\n')
