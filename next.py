# ---------------------------------------
# s = 'swiabsdfwighcss'
# for i in s:
#     if s.count(i) == 1:
#         print(i)
#         break
# else:
#     print(None)



# print(next((i for i in s if s.count(i) == 1), None))


# print(next(i for i in s if s.count(i) == 1))


# print([i for i in s if s.count(i) == 1])




# -------------------------------------------------------

# s = "A man, a plan, a canal: Panama"
# s = s.replace(',','').replace(':','').replace(' ','').lower().strip()
# if s == s[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")


# s = 'The quick brown fox jumpss'
# s = s.split()
# print({i:s.count(i) for i in set(s) })


# s = 'The quick brown fox jumpss fox'
# s = s.split()
# print({i:s.count(i) for i in s})




# s = 'The quick brown fox jumpss'
# s = s.split()
# for i in set(s):
#     print(i,len(i))


# s = 'The quick brown fox jumpss'
# a = max(len(i) for i in s.split())
# print(a)

# def longest_word(s):
#     max_length = 0
#     for i in s.split():
#         max_length = max(max_length, len(i))
#     return max_length

# print(longest_word("The quick browhhhn fox jumpss"))


# s = 'The quick brhhhown fox jumpss'
# n = s.split()
# final = ''
# max_length = max(len(i) for i in n)
# for i in n:
#     if len(i) == max_length:
#         final += i
# print(final)

# # --------------------------------------------------
# s = 'The quick brhhhhown fox jumpss'.split()
# high = ''
# for i in range(len(s)):
#     # print(len(s[i]))
#     if len(s[i]) > len(high):
#         high = s[i]
# print(high)


# print('hello')


# s = 'The quick brown fox jumpss'
# for i in s.split():
#     print(i,len(i))




# # sum of target in list
# nums = [1, 2, 3, 4, 5]
# target = 6
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print([nums[i], nums[j]])
#             break



# nums = [1, 2, 3, 4, 5]
# target = 6
# n = len(nums)
# for i in range(n):
#     for j in range(i+1, n):
#         if nums[i] + nums[j] == target:
#             print({nums[i], nums[j]})



# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# from collections import defaultdict
# groups = defaultdict(list)
# for word in words:
#     groups[''.join(sorted(word))].append(word)
# print(list(groups.values()))



# lst = [1, 2, 2, 3, 3, 3]
# print(max(set(lst), key=lst.count))


arr = [1,2,3,4,5]
target = 3
for i in range(len(arr)):
    if arr[i] == target:
        print(f"Found target {target} at index {i}")
        break
else:
    print(f"Target {target} not found")



# arr = [1,2,3,4,5,6,7,8]
# target = 3
# low = 0
# high = len(arr) - 1
# # while low <= high:
#     # mid = (low + high) // 2
# for i in range(len(arr)):
#     mid = (low + high) // 2
#     if arr[mid] == target:
#         print(mid)  
#     elif arr[mid] < target:
#         low = mid + 1
#     else:
#         high = mid - 1
# # print(-1)


# def search(lst,t):
#     low = 0
#     high = len(lst) - 1
#     # lst = sorted(lst)
#     while low <= high:
#         mid = (low + high) // 2
#         if lst[mid] == t:
#             return mid
#         elif lst[mid] < t:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1   

# lst = [1,3,5,6,3,7,8,3,6,8,9]
# t = 8
# print(search(lst,t))



# nums = [1, 2, 4, 5]
# n = 5
# print(int((n*(n+1))/2) - sum(nums))

# print(sum(range(1, n+1)) - sum(nums))









# Stack implementation using list.--------------------

# Queue implementation using collections.deque.-----------------

# Find the first non-repeating character in a string.

# Find all pairs in a list that sum to a target.

# Group anagrams from a list of words.

# Find the most frequent element in a list.

# Implement binary search on a sorted list.

# Find missing number from a sequence.

# Flatten a nested list.

# Find subarray with the maximum sum (Kadane’s Algorithm).



























