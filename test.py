

filename = 'davi.txt'
f = open(filename, "w+")

f.write(('%s, %s' % ('nome', 'idade')))
f.write(('%s, %d' % ('davi', 18)))

f.close()