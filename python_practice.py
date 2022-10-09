from curses import erasechar


def hello () :
    print("Hello User")

def pack (item_one, item_two, item_three) :
    return [item_one, item_two, item_three]

def eat_lunch (food) :
    if len(food) == 0:
        print('My lunchbox is empty!')
    else:
        for i in range(len(food)):
            if i == 0:
                print(f"First I eat {food[0]}")
            else:
                print(f"Next I eat {food[i]}")

hello()
print(pack('a','b','c'))
print(pack('c','s','r'))
eat_lunch([])
eat_lunch(['Pizza','Burgers','Salami','Cheesecake'])
