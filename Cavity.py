__author__ = 'rfischer'


num_lines = input()

m = []

for n in xrange(0, num_lines):
  m.append(str(raw_input()))


print m[0]

for y in xrange(1, num_lines-1):
    s = m[y][0]
    for x in range(1, num_lines-1):
        current = int(m[y][x])
        if int(m[y-1][x]) < current > int(m[y+1][x]) and int(m[y][x-1]) < current > int(m[y][x+1]):
            s += "X"
        else:
            s += str(current)
    s += m[y][num_lines-1]
    print s

if num_lines > 1:
  print m[num_lines-1]

