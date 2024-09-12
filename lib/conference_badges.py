def badge_maker(name):
    badge = f"Hello, my name is {name}."
    return badge

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    return [f"Hello, {name}! You'll be assigned to room {index}!" for index, name in enumerate(names, start= 1)]


def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)
    room_assignments = assign_rooms(names)
    for assignment in room_assignments:
        print(assignment)
