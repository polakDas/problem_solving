import collections

dic = {
    'name': 'polak',
    'age': 26,
    'marks': [10, 10, 12, 8]
}

# namedtuple
a = collections.namedtuple('person', 'name, age, nationality')
person = a('Polak', 26, 'Bangladeshi')

print(person)

# defaultdict
b = collections.defaultdict(dict, dic)
print(b['age'])

# orderdict
c = collections.OrderedDict(dic)
print(c['name'])