import sys
from itertools import dropwhile, takewhile

def parse_cmd(cmd):
    """parse string tinto function to evaluate
    """
    cmd = cmd.split()
    action, subj, prep, obj = cmd
    return f'{action}({subj}, {obj}, prep="{prep}")'

def find_stack(world, block):
    """ Given a world state and a bloc return stack number
    where block exists.
    """
    for stack in world:
        if block in world[stack]:
            return stack

def print_world(world):
    """Print world state in online-judge solutioin format
    """
    for stack in world:
        line = str(stack) + ':'
        if world[stack]:
            line += ' ' + ' '.join(str(x) for x in world[stack])
        print(line)
        
def takeuntil(predicate, iterable):
    """Generator function that yields each item of an iterable 
    until some predicate condition holds including the first item
    the predicate holds for.
    """
    break_condition = False
    for x in iterable:
        if break_condition:
            break
        else:
            yield x
        if predicate(x):
            break_condition = True
            
def takeafter(predicate, iterable):
    """Generator function that yields each item of an iterable 
    after some predicate condition holds not including the first item
    the predicate holds for.
    """
    yeild_condition = False
    for x in iterable:
        if yeild_condition:
            yield x
        if predicate(x):
            yeild_condition = True

def construct_move(n, actions):
    """Given a world state of ``n`` block starting positions and a list of actions
    print the world state after performing all actions.
    """
    world = {i: [i] for i in range(n)}

    def move(a, b, prep="over"):
        """where ``a`` and ``b`` are block numbers, puts block ``a``
        onto block ``b`` after returning any blocks that are stacked
        on top of blocks a their initial positions. If ``prep`` is
        "onto" also return any blocks that are stacked on top of 
        blocks ``b`` their initial positions before moving.
        """
        where_a = find_stack(world, a)
        where_b = find_stack(world, b)
    
        stack_a = world[where_a]
        stack_b = world[where_b]

        if where_a == where_b:
            return None

        to_move = takeafter(lambda x: x == a, stack_a)
        to_stay = takeuntil(lambda x: x == a, stack_a)
        # move blocks home
        list(map(lambda x: world[x].append(x), to_move))
        world[where_a] = list(to_stay)

        if prep == 'onto':
            to_move = takeafter(lambda x: x == b, stack_b)
            to_stay = takeuntil(lambda x: x == b, stack_b)
            # move blocks home
            list(map(lambda x: world[x].append(x), to_move))
            world[where_b] = list(to_stay)

        world[where_b].append(world[where_a].pop(-1))
        return None

    def pile(a, b, prep="over"):
        """where a and b are block numbers, puts the pile of blocks
        consisting of block a, and any blocks that are stacked
        above block a, onto the top of the stack containing block
        b. If ``prep`` is "onto" all blocks on top of block b are
        moved to theirinitial positions prior to the pile taking place.
        The blocks stacked above block a retain their original order when moved
        """
        where_a = find_stack(world, a)
        where_b = find_stack(world, b)
    
        stack_a = world[where_a]
        stack_b = world[where_b]

        if where_a == where_b:
            return None
        
        if prep == 'onto':
            to_move = takeafter(lambda x: x == b, stack_b)
            to_stay = takeuntil(lambda x: x == b, stack_b)
            # move blocks home
            list(map(lambda x: world[x].append(x), to_move))
            # set object block to state befor movement
            world[where_b] = list(to_stay)

        world[where_b] += list(dropwhile(lambda x: x != a, stack_a))
        world[where_a] = list(takewhile(lambda x: x != a, stack_a))

        return None

    for action in actions:
        eval(action)
    
    return world

def main():
    """Main function to collect and parse action statements and
    executes function to contruct and print final world state.
    """
    lines = []
    while True:
        line = sys.stdin.readline().rstrip('\n')
        if line == 'quit':
            break
        else:
            lines += [line]

    n = int(lines.pop(0))
    actions = [parse_cmd(line) for line in lines]
    world = construct_move(n, actions)
    print_world(world)


if __name__ == '__main__':
    main()
    exit(0)
