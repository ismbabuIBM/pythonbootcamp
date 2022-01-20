d = {'aaa' : 1,  'bbb' : 'test', 'ccc' : [1, 'a', 90.987], 'ddd' : {'a':1, 'b':2}, 111 : 222}

#keys
print(d.keys())

#values
print(d.values())

#items
print(d.items())

#print disc
print(d)

#print the type of items in disc
print(type(d['ccc']), type(d['ddd']))

#print any key
print(d['bbb'])

#print nested element
print(d['ccc'][1])

#change nested value
d['ddd']['a']  = 5
print(d['ddd']['a'])
print(d['ddd'])