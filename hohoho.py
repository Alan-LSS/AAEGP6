def mf() :
  return True

if mf() :
    print("yes.")
else :
    print("no.")

x = 20
print(isinstance(x,int))    

thdict = {  #thdict is just the name
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thdict["model"]#to get the items
print(x)
thdict['year']=2020
a=thdict['year']
print(a)

for c in thdict: #c,f,s,a,e,w,...all is fine, just a tool
  print(thdict[c])

for x in thdict.values(): #same as the foward
  print(x)

z=2*3+6+7/7
print (z)
y=2*(3+6)+7/7
print (y)


thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

print(thdict['model'])


  #print('{}scores {}marks'.format(name,score))

thdict.popitem()
print(thdict)

thdict.clear()
print(thdict)

mydict = dict(thdict)
print(mydict)

j=range(1,9)
for n in j:
  print(n[::2]) 