"""Write a Python program to perform following operations on List.
-> Creating a List - [ ]
-> Accessing Elements - list[0] ,list[-1]
-> Index - list.index('BMW')
-> Slicing - list[1:3]=[' ',' ']
-> Adding and Removing Elements - list.insert(3,'Lambo'), list.append('Apache') ,list.remove('BMW'), list.pop(0)
-> Modifying and Searching elements - list[0]='Porshe', ('BMW M5' in cars)
-> Sorting and Reversing elements - list.sort(), list.reverse()"""

#This is list - can store multiple data types,In this case this is String
cars=['BMW M5','Porsche 911','Pagani Huayra','Lamborghini Huracan','Audi R8'] 
print("\nArray Of Strings:",cars)

#Accessing elements
print("\nAccessed Element:",cars[1])
print("\nAccessed Element With -Ve Index:",cars[-1]) #Access from the end
print("\nAccessed Elements From Index 1 to 3 :",cars[1:4]) #Range of indexes - cars[start:end]
print("\nAccessed Elements From Index 0 to 2 :",cars[:3]) #Leaving out the start value,range will start from 0 will go till end value
print("\nAccessed Elements From Index 2 to 4 :",cars[2:]) #Leaving out the end value,range will go on till end of the list from the start value

#Finding index of an element
print("\nIndex of the BMW M5:",cars.index('BMW M5'))

#Slicing
cars[1:3]=['Bugatti Chiron','McLaren'] #replaces element on index 1 and index 2
print("\nSlicing:",cars)
#inserting more items then u replace, means cars[1:2] replaces element on index 1 and then again wants replace element on index 1
cars[1:2]=['Ferrari','Rolls-Royce Ghost'] #so instead it replaces element on index 1 and adds element on index 2 
print("\nSlicing 2:",cars) 
#inserting less items then u replace, means cars[1:4] replaces element on index 1 and then again wants replace element on index 4
cars[1:4]=['Ford GT'] # but we dont have Element to insert so instead it removes elements in between indexes 1 and 4
print("\nSlicing 3:",cars)  
                           

#Adding an element using .insert() and .append()
cars.insert(3,"Koenigsegg Jesko")  #insertes an element on specified on position
print("\nAdded Element:",cars)
cars.append("Aston Martin Valkyrie") #adds an element to the end of the list
print("\nAdded Element 2:",cars)

#Removing an element using .remove() and .pop()
cars.remove("Audi R8") 
print("\nRemoved using .remove():",cars)
cars.pop() #If value is not specified, removes the last element
print("\nRemoved using .pop():",cars)

#Modifying/Changing/searching
cars[2]='Nissan GTR'
print("\nModified Element:",cars)
print('BMW M5' in cars)


#Sorting Elements
Nums=[69,0,11,7]
Nums.sort() #By Deafult Ascending Sorting
print("\nSorted List:",Nums)
Nums.sort(reverse=True) #Sorts In Descendig Order
print("\nSorted List 2:",Nums)

#Revering Elements 
Nums.reverse()
print("\nReversed List:",Nums)

#Deleting The Entire List
Nums.clear()
print("\nDeleted Nums list using .clear():")

print("\n",cars)




