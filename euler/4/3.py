p = []
for i in range (100,1000):
   for j in range (100,1000):
      m = i*j
      s = str(m)
      r = s[::-1]
      if(s == r):
          p.append(int(s))
print max(p)

