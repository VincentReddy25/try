"""a=input("Enter the word")
b=input("Enter second word")
c=""
for i in a:
    if i in b:
        continue
    else:
        c+=i
print(c)
"""
"""
a=["break","continue","while","for","case","goto"]
word=input("enter your word")
for i in range len(a):
    if word in a:
        print("it is a keyword")
    else:
        print("it is not {word} is keyword")
"""
"""
a=input("enter your word")
print(a[::-1])
"""
"""
vowels={"a","e","i","o","u"}
string=input("enter the string")
c=""
for i in string:
    if i in vowels:
        continue
    else:
        c+=i
print(c)
"""
"""
a=input("enter your string")
b=a[::-1]
if a==b:
    print("palindrome")
else:
    print("not a palindrome")




a=input("enter ur uppercase letter word")
if a in isupper():
    c=a.lower()
    print(c)
elif a islower():
    d=a.upper()
    print(d)
else:
    print(a)



string = input("Enter text : ")
toggle_str = ''
for i in range(len(string)):
    if(string[i] >= 'a' and string[i] <= 'z'): 
        toggle_str = toggle_str + chr(ord(string[i]) - 32)
    elif(string[i] >= 'A' and string[i] <= 'Z'):
        toggle_str = toggle_str + chr(ord(string[i]) + 32)
    else:
        toggle_str = toggle_str + string[i]
print("STRING ENTERED BY YOU                :", string)
print("RESULTANT STRING AFTER TOGGLING CASE :", toggle_str)

"""











"""

def bubble_sort(list1):
    for i in range(0,len(list1)-1):
        for j in range(len(list1)-1):
            if(list1[j]>list1[j+1]):
                temp=list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=temp
    return list1

list1=[5,3,6,1,6]
print()
"""

"""
#Selection Sort
def selection_sort(array):
    length=len(array)

    for i in range(length-1):
        minIndex=i
        
        for j in range(i+1,length):
            if(array[j]<array[minIndex]):
               minIndex=j

        array[i],array[minIndex]=array[minIndex],array[i]
        return array
    array=[21,6,9,33,3]
print("The Sorted array is:",selection_sort(array))
"""

#Insertion Sort
def insertion_sort(list1):
    for i in range(1,len(list1)):
        key = i-1
        while j>=0 and key < list[j]:
            list1[j+1] = list1[j]
            j-=1
            list1[j+1]=key
        return list1
list1=[10,5,13,8,2]
print("The unsorted list is:",list1)
print("The Sorted list1 is:",insertion_sort(list1))




































