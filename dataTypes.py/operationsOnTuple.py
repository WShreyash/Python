"""Write a Python program to perform following operations on Tuple.
-> Creating a Tuple - tuple=( )
-> Accessing Elements - tuple[0], tuple[-1]
-> Index - tuple.index(7)
-> Slicing - tuple[1:3]=[6,8]
-> Concatenation - t3=t1+t2
-> Deleting - have to convert tuple into list then tuple again 
-> Nested Tuples - tuple((1,3,4), (2,6,9))"""

tuple = (1.3, 7, 4, "Hello")
print("Accessing element: ", tuple[0], tuple[-1])
print("Indexing: ", tuple.index(7))
print("Slicing: ", tuple[1:4])

# concatenation - adding two tuples
tuple2 = (69, 12, "World")
tuple3 = tuple+tuple2
print("concatenation: ", tuple3)


# Original Tuple
tup = (10, 20, 30, 40, 50)

#nested tuple
nested_tuple=((1,3,4), (1.3,1))
print("Nested Tuple: ", nested_tuple)