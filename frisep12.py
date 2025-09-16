





# def fib(n):
#     if n < 2:
#         return n 
#     else:
#         return fib(n-1) + fib(n-2)

# print(fib(3))



# def my_start(s,prefix): 
#     return s[:len(prefix)]==prefix


# def my_end(s,suffix): 
#     return s[-len(suffix):]==suffix


# print(my_start("hello","he"), my_end("hello","lo"))





# s1, s2 = "abc", "axbxc"
# i = 0
# for ch in s2:
#     if i < len(s1) and ch == s1[i]: 
#         i+=1
# print(i==len(s1))




# lst = [1,2,3,4,5]
# k = 2
# # for i in lst[0:k]:
# for i in range(k+1):    
#     lst.insert(0,lst.pop())

# print(lst)    





# lst, k = [1,2,3,4,5], 2
# for _ in range(k):
#     lst.insert(0,lst.pop())
# print(lst)



# lst, k = [3,1,4,1,5,9], 2
# print(sorted(lst)[-k])


# lst = [3,1,4,1,5,9]
# k = 4
# print(sorted(set(lst))[-k])


# a,b,c=[1,2,3],[2,3,4],[3,4,5]
# print(set(a),set(b),set(c))
# print(set(a) & set(b) & set(c))


# lst = [1,2,3,4,5]
# even = [i for i in lst if i%2 == 0]
# odd = [j for j in lst if j%2 == 1]
# print(even,odd)



# lst=[-1,2,-3,4,-5,6]
# plus = [i for i in lst if i > 0]
# minus = [j for j in lst if j < 0]
# equal = [k for k in lst if k == 0]
# print(plus,minus,equal)



# lst=[-1,2,-3,4,-5,6]
# pos=[x for x in lst if x>0]
# neg=[x for x in lst if x<0]
# res=[]
# while pos or neg:
#     if pos: 
#         res.append(pos.pop(0))
#     if neg: 
#         res.append(neg.pop(0))
# print(res)






# s={1,2,3,4}
# ps=[set()]
# for e in s: ps += [x|{e} for x in ps]
# print(ps)
# -----------------------------------------------






d={"apple":1,"kiwi":2,"banana":3}
print(sorted(d,key = len))









# Rotate a list by k positions without slicing.

# Find the kth largest element in a list.

# Find common elements in three lists.

# Split a list into two lists: one with even numbers, one with odd numbers.

# Rearrange a list so that positive and negative numbers alternate.

# Find all subsets of a set (power set).

# Count frequency of words in a paragraph (case-insensitive).

# Check if two dictionaries are mirror images (key ↔ value swapped).

# Sort dictionary keys by their length.

# Group numbers by remainder when divided by k.

# Implement a stack using two queues.

# Implement a queue using two stacks.

# Implement a priority queue using a list.

# Find the intersection of two sorted arrays.

# Merge overlapping intervals.

# Implement insertion sort.

# Implement selection sort.

# Implement bubble sort.

# Implement quicksort.

# Implement merge sort.




# def star(a,s):
#     return a[0:len(s)] == s

# def end(s,e):
#     return s[-len(e):] == e

# print(star('hello','he'))
# print(end('hello','lo'))






# years = ['2025','2026']
# months = ['Jan','Feb']
# days = range(1,30)
# for y in years:
#     for m in months:
#         for d in days:
#             print(f'report_{y}_{m}_{d}.csv')






tables = ['customers','orders','products','prices']
columns = ['id','date']
for t in tables:
    for c in columns:
        print(f'SELECT COUNT(*) FROM {t} WHERE {c} IS NULL')
























































# def longest_pal(s):
#     res=""
#     for i in range(len(s)):
#         for j in range(i,len(s)):
#             sub=s[i:j+1]
#             if sub==sub[::-1] and len(sub)>len(res):
#                 res=sub
#     return res
# print(longest_pal("babad"))
