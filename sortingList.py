# In this snippet of code, we first open a file 
# Then pull a specific type of data
# Then sort them all


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
# we must first assign a dictionary to store data
myDict=dict()
# we create a loop 
# inside the loop, all lines with 'from' will be splitted
for line in handle:
    if not line.startswith('From'):
        continue
    else:
        words=line.split()
        # we create a histogram with dictionary to check how often the data we see
        for word in words:
            myDict[word]=myDict.get(word,0)

# We sort the final dictionary
a= sorted(myDict)
print(a)
# We parse the 27th data in dictionary which is the time and assign it in "dates" variable
dates= a[:27]
mylist= list()
# inside the loop, the each number in dates is parsed 
# and storeed in the list
for number in dates:
    number= number.split(":")
    mylist.append(number)
mysecList= list()
# we created a second list 
# by using loops we stored the first data which is 'the hour' of time inside the seclist
 
for iter in mylist:
    s= iter[0]
    mysecList.append(s)
the_dict=dict()
# we created histogram to check how often we see each hour
for iter in mysecList:
    the_dict[iter]= the_dict.get(iter,0)+1
for k,v in sorted(the_dict.items()):
    print(k,v)

