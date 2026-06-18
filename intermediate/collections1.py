# Collections : Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque
a = "aaaaabbbbbcccccddd"
print(Counter(a))
print(Counter(a).items())
print(Counter(a).keys())
print(Counter(a).most_common(1))
print(Counter(a).most_common(2))
print(Counter(a).most_common(1)[0][0])
print(list(Counter(a).elements()))


point = namedtuple('Point', 'x, y')
pt = point(1, -4)
print(pt)
print(pt.x, pt.y)
print(pt[0], pt[1])


ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
print(ordered_dict)
print(ordered_dict['a'])

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['b'])
print(d['c'])  # Key 'c' does not exist, but it will return the default value (0 for int)


d = deque()
d.append(1)
d.append(2)
d.appendleft(0)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.clear() # Clear the deque
d.extend([1, 2, 3])
print(d)
d.extendleft([0, -1, -2])
print(d)
d.rotate(1)  # Rotate the deque to the right
print(d)