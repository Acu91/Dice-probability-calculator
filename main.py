
import probability

lst = []
#Enter the number dice to predict
n = int(input("Enter number of elements : "))
 
# Iterating till the range
for i in range(0, n):
    ele = int(input("item " + str(i+1) + ": "))
    lst.append(ele) # adding the element

#Enter the number of expirements
x = int(input("Enter number of expirements : "))

print("The probability of draw " + str(lst) + " with " + str(len(lst)) + " rolls is " + str(probability.prob(lst,len(lst),x)))
