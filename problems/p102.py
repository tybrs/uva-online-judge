from collections import defaultdict
from itertools import permutations
import fileinput

def group(lst, n):
    for i in range(0, len(lst), n):
        grp = lst[i:i + n]
        if len(grp) == n:
            yield tuple(int(x) for x in grp)

def compute_costs(bins):
    positions = {'B': 0, 'G': 1, 'C': 2}
    possible_worlds = sorted(permutations('BGC', 3))
    cost = defaultdict(lambda: 0)
    for world in possible_worlds:
        for color in world:
            p0, p1 = set(positions.values()) - set([world.index(color)])
            cost[world] += bins[p0][positions[color]]
            cost[world] += bins[p1][positions[color]]
    return min(cost.items(), key=lambda d: d[1])

def print_result(result):
    world, cost = result
    print(''.join(world), cost)
    
def main():
    for line in fileinput.input():
        bins = list(group(line.split(), 3))
        print_result(compute_costs(bins))

if __name__ == '__main__':
    main()
    exit(0)