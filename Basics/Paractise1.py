#Python Paractise 1

# In[62]:


print("Shahzaib Raja")


# From Here i Start Code

# In[63]:


if 52>20:
    print("This is Correct Statement")
else:    
    print("This is not a Correct Statement")        


# In[64]:


x = 53
print(x)


# In[65]:


# This is Just a Paractise Statement
x*x*x*x*x*x


# In[66]:


print(x)
x = "Abdul Rafay Ather"
print(x)


# In[67]:


x = str(3)
y = int(4)
z = float(54)
print(x)
print(y)
print(z)


# In[68]:


print(type(x))
print(type(y))
print(type(z))


# In[69]:


print('Water is the Best Source')


# In[70]:


i_am_physics = 37
print('i_am_physics')


# In[71]:


x = y = z = "Orange"
print(x)
print(y)
print(z)


# In[72]:


fruits = ["orange","Twitter","English"]
# x,y,z = fruits
print(fruits)
# print(y)
# print(z)


# In[73]:


x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


# In[74]:


x = "Python"
y = "is"
z = "awesome"
print(x+y+z)


# In[75]:


x = "523"
y = "35"
print(x,y)


# In[76]:


extra = "Shahzaib Raja"
def my_func():
    print("He is "+ extra)

my_func()


# In[77]:


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


# In[78]:


W = "awesome"

def myfunc():
  global z
  z = "fantastic"

myfunc()

print("Python is " + z)


# In[79]:


x = frozenset({"apple", "banana", "cherry"})
l = []
a= "king"
l.append(x)

print(x)


# In[80]:


x = frozenset({"Ali","Arshad","Naveed"})

print(type(x))


# In[81]:


x = 1    # int
y = 2.8  # float
z = 1j   # complex
print (type(z))


# In[82]:


x = 53
y = complex(x)
print(type(x))
print(type(y))


# Random Number Generator

# In[83]:


import random
print(random.randrange(1,10))


# In[84]:


y = str("056shahzaib3442")
print(y)


# In[85]:


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


# In[86]:


a = "This is a Master Class"
print(a[13])


# In[87]:


for x in "bananas":
    print(x)


# In[88]:


x = "Muhammad Shahaeer"
print(len(x))


# In[89]:


xxx = "Muhammad Shahaeer"
print("Shah" in xxx)


# In[90]:


txt = "The best things in life are free!"
if "frvee" in txt:
  print("Yes, 'free' is present.")
else:
    print("error")


# In[91]:


txt = "The best things in life are free!"
print("expensive" not in txt)


# In[92]:


x = "Muhammad Shahaeer"
print(x[2:8])


# In[93]:


x = "Muhammad Shahaeer"
print(x[-10:-5])


# In[94]:


a = "Donkey Raja!"
print(a.lower())


# In[95]:


a = "Donkey Raja! is the KING"
print(a.strip())


# In[96]:


a = "Donkey Raja! is the KING"
print(a.replace("Raja","Malik"))


# In[97]:


a = "Donkey$Raja!$ is$ the$ KING$"
print(a.split("$"))


# In[98]:


x = "Muhammad"
y = "ZAIBI"

print(x," ",y)


# In[99]:


f  = 19
txt = "Shahzaib Age is " + str(f)
print(txt)


# In[100]:


price = 59
txt = f"The price is {price} dollars"
print(txt)


# In[101]:


price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


# In[102]:


price = 59
txt = f"The price is {price} + {100*5}"
print(txt)


# In[103]:


txt = "This is a \"Software\" Book"
print(txt)


# In[104]:


txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


# In[105]:


print (10>9)


# In[106]:


bool("abc")
bool({})
bool(["apple", "cherry", "banana"])


# In[107]:


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


# In[108]:


def my_func():
    return False
print(my_func())


# In[109]:


x = 200
print(isinstance(x, str))


# In[110]:


print(2 ** 8) 
# Power


# In[111]:


mylist = ["India","aMERICA","Japan","Pakistan"]
print(mylist)


# In[112]:


print(mylist[-1])


# In[113]:


mylist = ["India","aMERICA","Japan","Pakistan"]
if "Japan" in mylist:
    print("Available Sir!")


# In[114]:


list = ["India","aMERICA","Japan","Pakistan"]
list[2] = "Palestine"
print(list)


# In[115]:


list = ["India","aMERICA","Japan","Pakistan"]
list.insert(-3,"Palestime")
print(list)


# In[116]:


thislist = ["apple", "banana", "cherry"]
Mark = ["mango", "pineapple", "papaya"]
thislist.extend(Mark)
print(thislist)


# In[117]:


list = ["India","aMERICA","Japan","Pakistan","Japan","America"]
list.remove("Japan")
print(list)


# In[118]:


list = ["India","aMERICA","Japan","Pakistan","Japan","America"]
list.pop()
print(list)


# In[119]:


list = ["India","aMERICA","Japan","Pakistan","Japan","America"]
del list
print(list)


# In[120]:


list = ["India","aMERICA","Japan","Pakistan","Japan","America"]
list.clear()
print(list)


# In[121]:


list = ["India","aMERICA","Japan","Pakistan","Japan","America"]
for x in list:
    print(x)


# In[122]:


list = ["India","aMERICA","Japan","Pakistan","Japan","America"]     #ForLoop
for x in range(len(list)):
    print(list[x])


# In[123]:


list = ["Haider","RAFAY","Shaheer","Shahzaib"]  #While LOOP
i = 0
while i < len(list):
 print(list[i])
 i= i+1


# In[124]:


list = ["Haider","RAFAY","Shaheer","Shahzaib"]
[print(x) for x in list]


# In[125]:


list = ["Haider","RAFAY","Shaheer","Shahzaib"]
newlist = []

for x in list:
    if "F" in x:
        newlist.append(x)
print(newlist)
# Only Prints Words having F in it


# In[126]:


# newlist = [for x in x range(10) if x > 5]
list = ["Haider","RAFAY","Shaheer","Shahzaib"]
# newlist = [x.upper() for x in list ]
newlist = ['hello' for x in list]
print(newlist)


# In[127]:


list = [50,45,34,23,12,45,76,87,34]            #Sorting the List
list.sort(reverse = True)           # (reverse = True)
print(list)


# In[128]:


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


# In[129]:


thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


# In[130]:


x = []
x = mylist
print(x)


# In[131]:


thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

# Also Used that
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist[:]
# print(mylist)


# In[132]:


list1 = ["Sweet","Orange","Cat","Banana"]
list2 = [43,23,34,45]

for x in list2:
    list1.append(x)

print(list1)


# In[133]:


xx = ("Sweet","Orange","Cat","Banana")
print(xx)


# In[134]:


thistuple = ("apple", "banana", "cherry" , "Physics", "Taple")
print(len(thistuple))


# In[135]:


tuple1 = ("abc", 34, True, 40, "male")
print(len(tuple1))


# In[136]:


thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


# In[137]:


thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


# In[138]:


thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


# In[139]:


thistuple = ("Twitter","Install", "Physics")
print(thistuple[2])


# In[140]:


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


# In[141]:


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])


# In[142]:


thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


# In[161]:


xy = ("Twitter","star","indian")   #Unpacking a Tuple
(pak,india,xx) = xy
print (pak,india,xx)


# In[164]:


xy = ("Twitter","star","indian")   #Loop a Tuple
for x in xy:
    print(xy)


# In[168]:


#Loop Through the Index Numbers
xy = ("Twitter","star","indian")
for x in range(len(xy)):
    print(xy)


# In[175]:


xy = (3,43,2,21,543,6,5,74,5,8,9,4,39,9,9,9,4) #count in Python
y = xy.count(9)
print(y)


# In[9]:


xyz = {"Twitter","star","indian","star",0,1}
print(xyz)


# In[17]:


#Finds out Not Available
xyz = {"Twitter","star",True,False,0,1,"star"}
print("star" not in xyz)


# In[32]:


xyz1 = {"Twitter","star","star"}
xyz2 = {"Twitter","stari","Askar"}
# xyz1.union(xyz2)
# # xyz1.update(xyz2)
# xyz3 = xyz1.intersection(xyz2)
xyz3 = xyz1.difference(xyz2)
print(xyz3)


# Python Dictionaries
# 

# In[33]:


dd = {"elon":"Twitter","Mark":"facebook","Larry":"Google"}
print(dd)


# In[41]:


dd = {"elon":"Twitter","Mark":"facebook","Larry":["Google","America","Physics"]}
print(dd["Mark"])
print(dd["Larry"])
print(len(dd))


# In[51]:


x = dd.get("elon")
print(x)
x =dd.values()
print(x)


# In[61]:


#Add Something into the Dictionary
dd = {"elon":"Twitter","Mark":"facebook","Larry":["Google","America","Physics"]}
x = dd.items()
print(x)
dd["jeff"] = "Amazon"
print(x)
print(dd)


# In[70]:


#Update the Dictionary Values
dd = {"elon":"Twitter","Mark":"facebook","Larry":["Google","America","Physics"]}
# dd["Mark"] = "India"
dd.update({"Mark":"Indian"})
print(dd)


# In[83]:


ddx = {"elon":"Twitter","Mark":"facebook","Larry":1997}
print(ddx)
del ddx["Mark"]
print(ddx)


# In[91]:


ddx = {"elon":"Twitter","Mark":"facebook","Larry":1997}
for x in ddx.values():
    print(ddx)


# In[102]:


ddx = { "Child1": {"elon":"Twitter","Mark":"facebook"},
       "Child2": {"elon":"Twitter","Mark":1957}}
print(ddx)
print(ddx["Child2"]["Mark"])

# print(myfamily["child2"]["name"])


# In[116]:


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])


# In[130]:


# x = [2,3,5,6,4,3]
for x in range(2, 30, 3):
  print(x)


# In[144]:


dp = ["Milk","Mango","Orange"]
for x in dp:
    print(x)
    if x == "Mango":
      break

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break


# In[147]:


#with difference of 2 in each value from 2-15
for x in range (2,15,2):
    print(x)


# In[2]:


dp = ["Milk","Mango","Orange"]
dpx = ["Jeff Bezos","Musk","Mark"]
for x in dp:
    for y in dpx:
        print(x,y)


# In[167]:


for x in [0, 1, 2]:
  pass


# In[4]:


#Function Made
def helloworld():
    print("Zaibi Noob")

helloworld()


# In[12]:


#Pass the Arguments to Functions
def ustad(wx):
    print(wx + " Thanks")

ustad("Naveed")
ustad("indian")
ustad("Pakistan")


# In[18]:


#If Arguments Unknown
def ustad(*wx):
    print("This is " + wx[1])

ustad ("Naveed","Anjum","Masood")


# In[21]:


# key = value Arguments to be send
def ustad(c1,c2,c3):
    print("This is " + c3)

ustad (c1 = "Naveed",c2 = "Anjum", c3 = "Masood")


# In[25]:


# If Known Keyword Arguments use -> **kwargs
def ustad(**wwx):
    print("This is " + wwx["c1"])

ustad (c1 = "Naveed",c2 = "Anjum", c3 = "Masood")


# In[27]:


# Default Parameter Value
def myking ( style= "Phy"):
    print("This is " + style )

myking("Naveed")
myking("kass")
myking()
myking("asa")


# In[10]:


# //Only Keyword Argument
def my_func(*,x):
    print(x)

my_func(x = "queen")


# In[16]:


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


# In[ ]:




