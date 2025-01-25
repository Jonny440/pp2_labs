#Boolean
#print(10.42 > 10.41999)
#print(bool(""))
#print(bool("not empty string"))

#Operators
#print(5 > 2 and 6 == 6)
#list = [1, 2, 3]
#print(4 not in list)

#Lists
#list1 = [1, 2, 3, 3 , 4, 5]
#print(list1[1])
#list1.append(6) insert in the end
#list3 = [7, 8, 9]
#list3.remove(8)
#print(list1 + list3)
#list = [10, 20, 30]
#list.insert(1, 15) inserts 15 in the index 1, everything else goes right by 1
#print(list[1:3]) print everything from index 1 to index 2. 3 is not printed
#newList = list #copied the list

##Tuple
#tuple = ("one", "two", "three", 4)
#print(tuple[1:] + " " + tuple[-1])
#tuple.append("four")
#
#remove element
#y = list(tuple)
#t.remove(4)
#tuple = y
#
#(one, two, others) = tuple

#Sets

#set = {"mother", "fahter", "baby"}
#print(len(set))
#for person in set:
#    if person == "fahter":
#        print("helo father")
#
#setTwo = {"granny", "mother", "pops", "baby"}
#print(set.intersection(setTwo)) # only what is in both sets

#Dict
#months = {
#    "Jan" : 31,
#    "Feb" : 28,
#    "Mar" : 30
#}
#
#for month in months.keys():
#    print(months[month])
#months["Feb"] = 29 # in leap year
#
#months["Apr"] = 31

##while loops, if else
#count = 0
#while True:
#    if count <= 1000:
#        print(count)
#        count += 1
#    else:
#        print("Countdown is over")
#        break
