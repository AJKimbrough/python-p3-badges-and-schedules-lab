def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    new_list = []
    for name in names:
        new_list.append(f"Hello, my name is {name}.")
    return new_list

def assign_rooms(names):
    new_list = []
    i = 1
    for name in names:
        new_list.append(f"Hello, {name}! You'll be assigned to room {i}!")
        i+=1
    return new_list

def printer(names):
    for name in batch_badge_creator(names):
        print(name)
    for name in assign_rooms(names):
        print(name)
    return None


printer((['Guido', 'Edsger', 'Ada', 'Charles', 'Alan', 'Grace', 'AJ']))