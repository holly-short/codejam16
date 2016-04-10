#source code

t = int(raw_input())
x = 1
mylist = [];

def comp(k,c,s) :
    if c == 1 :
       if k == s:
          i=1
          temp = [];
          while i<=k :
                temp.append(i)
                i+=1
          mylist.append('Case #'+str(x)+': '+str(temp))
       elif k != s :
          mylist.append('Case #'+str(x)+': '+str('IMPOSSIBLE'))
    else :
         if s==(k-1) or s==k :
            i=2
            temp = [];
            while i<=k :
                  temp.append(i)
                  i+=1
            mylist.append('Case #'+str(x)+': '+str(temp)) #correction is needed here in temp
         elif s==(k-2) :
              i=2
              temp = [];
              temp.append(i)
              while i<(k-1) :
                  temp.append((k**c)-(i+1))
                  i+=1
              mylist.append('Case #'+str(x)+': '+str(temp))
         else :
              mylist.append('Case #'+str(x)+': '+str('IMPOSSIBLE'))
    return

while t>0 :
      k, c, s = map(int, raw_input().split())
      comp(k,c,s)
      x+=1
      t-=1

for p in mylist:
    for item in p:
        print item,
    print

