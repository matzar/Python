from operator import itemgetter
stats = {'a':(1000, 2000), 'b':(3000, 200), 'c':(100, 100), 'd':(100, 100), 'e':(100, 2000), 'f':(1000, 2000)}
st_items = stats.items()
st_values = stats.values()
print(max(stats.values(), key=itemgetter(1))[0])

for i in stats:
    most_co
    if i[2] >