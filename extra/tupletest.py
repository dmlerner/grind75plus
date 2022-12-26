stuff = {1, 2, 3, 4}

def f(n):
    initial_stuff = tuple(stuff)
    print(n, stuff, initial_stuff)
    count = 0
    for s in tuple(stuff):
        count += 1
        # AH. Indeed, count > len_initial_stuff, sometimes.
        # unclear exactly how this all works, but the moral is that you should do:
            # for s in tuple(stuff)
        print('count', count, len(initial_stuff))
        assert count <= len(initial_stuff)
        stuff.remove(s)
        print('removed', s, stuff, initial_stuff)
        f(n+1)
        stuff.add(s)
        print('readded', s, stuff, initial_stuff)
f(100)
