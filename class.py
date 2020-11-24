# write a function to take in a list and remove the first and last element
# student = ['Ayo', 'Winner', 'david']

# def pop(x):
#     x.pop(-1)
#     x.pop(0)
#     return x
# print(pop(student))

# write a function to return the lagest value in the  above list
# word = 0
# def max_len (x):
#     for word in x:
#         len(word)
#         return max(len(x))
# print(max_len(student))


# words=["alpha","omega","up","down","over","under","purple","red","blue","green"]
# sortedwords = sorted(words, key=len)
# print "The number of words in the list is: %s." % (len(words),)
# print "The shortest word in the list is: %s." % (sortedwords[0],)
# print "The longest word in the list is: %s." % (sortedwords[-1],)


# list = ["winner", "ade", "daniel", "maxi"]
# def largest_in_list(max):
#     count = o
#     for x in max:
#         len = x+1
#         return x
#     print (largest_in_list(list))
    
    
# list = [1, 2, 3, 4, 5]
# def largest(max):
#     value = 0
#     for x in max:
#         if x > value:
#             value = x
#     return value
# print(largest(list))

# list = ["winner", "ade", "daniel", "maxi"]
# def largest(max):
#     longest = []
#     value = 0
#     for x in list:
#         z = 0
#         for i in x:
#             z += 1
#         if z >= value:
#             value = z
#             longest.append(x)
#         # if x > value:
#         #     value = x
#     return longest
# print(largest(list))






















list = ["winner", "ade", "daniel", "maxi"]
def name(max):
    largest = []
    z = 0
    for x in list:
        i = 0
        for a in x:
            i += 1
        if i >= z:
            z = i
            largest.append(x)
    return largest
print(name(list))










            