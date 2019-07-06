import re
a = {'a': '1', 'b': '2', 'c': '3'}
b=[1,2,3,4]
print(type(a).__name__ == 'dict')
print(type(b).__name__ == 'list')
for key in a:
    print(key + ':' + a[key])
