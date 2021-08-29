import json
import random
UZB = {
    0: ['Amir Temur Xiyoboni', '41.311221', '69.279760'],
    1: ['Shaxrisabz', '39.060073', '66.829483'],
    2: ['Shayxontohur me’moriy ansambli','41.323239', '69.258872'],
    3: ['Nukus','42.460341', '59.617996'],
    4: ['Samarqand','39.654383', '66.968698'],
    5: ['Buxoro', '39.767945', '64.421701'],
    6: ['Xiva', '41.384443', '60.361864'],
    7: ['Minorai Kalon', '40.019653', '64.517765'],
    8: ['Registon square', '39.654459', '66.975809' ],
    9: ['Sirk', '41.323657', '69.242548']

}

def _places_uzb(id: int):
    tasks = []
    ran_list = random.sample(range(len(UZB)), 3)
    for x in ran_list:
        if x == id:
            pass
        else:
            tasks = tasks + [UZB[x]] 
    if len(tasks) < 4:
        print('E')
        tasks.insert(random.randint(0,len(tasks)),UZB[id])

    return tasks

print(_places_uzb(2))


