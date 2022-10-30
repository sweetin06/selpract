'''print("heloo")
a=10
print(a)'''

'''a,b,c = 9, 3.2,"ppp"
print(b)
print(c)
print(a)'''
'''b =7
print("{}{}".format(" value is",b))
print("value is",b)'''

'''a=10
b="ooo"
print(type(a))
print(type(b)'''


#list
'''a = [1, 2, "kkk", 0]
print(a[0])
print(a[2])
print(a[-1])
print(a[1:3])
a.insert(2,"ll") # 2 is a position and ll is a value
print(a)
a.append("end") #new value add into end
a[2] ="mmm" #to update by index
print(a)
del a[4] #to delete by index
print(a)'''

#tuple
#it similar to list, but immutable, not able to update
#a= (1, 2, 0.8, 67, "ppp")
#print(a[4])


a = {"k" : 2, 8:"ll", 'jj':"ooo"}# a value should be in the ""
print(a[8])
print(a["jj"])

#run time dictionary

dict = {}

dict["firstname"] ="sweetin"
dict["lastname"] = "aalesta"
dict["gender"] = "female"
print(dict)
print(dict["lastname"])