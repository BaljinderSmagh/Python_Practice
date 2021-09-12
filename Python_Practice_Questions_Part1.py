#library
import numpy as np

# List Questions


# Question 1: Remove Even Integers from List

def remove_even(lst):
    return [number for number in lst if number%2!=0]

# Question 2: Merge two sorted lists

# Solution 1:

def merge_lists(lst1, lst2):
    final_list=[]
    length=len(lst1) + len(lst2)
    start1=0 #to track the index of lst1
    start2=0 #to track the index of lst2
    for i in range(length):
        
        if lst1[start1]>lst2[start2] :
            
            final_list.append(lst2[start2])
            start2+=1
            if start2==len(lst2):
              #if start2 reached end limit of lst2 directly extend final list with the remaining lst1 elements
              final_list=final_list+ lst1[start1:]
              break
      
        else:
            final_list.append(lst1[start1])
            start1+=1
            #if start1 reached end limit of lst1 directly extend final list with the remaining lst2 elements
            if start1==len(lst1):
              final_list=final_list+lst2[start2:]
              break
    return final_list

# Solution 2:

def merge_arrays(lst1, lst2):
    ind1 = 0  # Creating 2 new variable to track the 'current index'
    ind2 = 0
    # While both indeces are less than the length of their lists
    while ind1 < len(lst1) and ind2 < len(lst2):
        # If the current element of list1 is greater
        # than the current element of list2
        if(lst1[ind1] > lst2[ind2]):
            # insert list2's current index to list1
            lst1.insert(ind1, lst2[ind2])
            ind1 += 1  # increment indices
            ind2 += 1
        else:
            ind1 += 1

    if ind2 < len(lst2):  # Append whatever is left of list2 to list1
        lst1.extend(lst2[ind2:])
    return lst1

# Question 3:List of Products of all Elements

# Given a list, modify it so that each index stores the product of all elements in the list except the element at the index itself.


def find_product(lst):
  new_list=[0] * len(lst)
  for i in range(len(lst)):
    # for product using numpy and exclude the that index number using slicing
    new_list[i]=np.prod(lst[i+1:] +lst[:i])
  
  return new_list


# Question 4:Find Minimum Value in List
# Given a list of size ‘n,’ can you find the minimum value in the list? without using min function

def find_minimum(arr):
  #Checking first if array is empty
  if  (len(arr)==0):
    return None
  #declaring intial min value
  min_val=arr[0]
  for i in arr:
    if i<min_val:
      min_val=i
  return min_val


# Question 5: Find Second Maximum Value in a List

#Solution 1 based on removing the first maximum and then getting second max
def first_maximum(lst):
  max_val=lst[0]
  for i in range(len(lst)):
    # update the max_no if max_no value found
    if max_val<lst[i]:
      max_val=lst[i]
  return max_val


def find_second_maximum(lst):
  first_max_val=first_maximum(lst)
  lst.remove(first_max_val)
  #find second max val
  second_max_val=first_maximum(lst)
  return second_max_val
    

#Solution 2:This is O(n) solution since list in traversed once only.
def find_second_maximum(lst):
  max_val = second_max_val =float('-inf')

  for i in range(len(lst)):
   
    # update the max_no if max_no value found
    if max_val<lst[i]:
      
      second_max_val=max_val
      max_val=lst[i]
    # check if it is the second_max_no and not equal to max_no
    elif (lst[i]>second_max_val and lst[i]!=max_val):
      second_max_val=lst[i]

  if (second_max_val == float('-inf')):
    return
  else:
    return second_max_val,max_val

# Question 6: Right Rotate List

#             Given a list, can you rotate its elements by one index from right to left?


def right_rotate(lst, k):
  #rotate the list based on its last element if the value of k is greater than length of list.  
  if k>len(lst):
    return lst[-1:] +lst[:-1]
  else:
    return lst[-k:] + lst[:-k]


# Question 7: Rearrange Positive & Negative Values

#           Given a list, can you rearrange its elements in such a way that the a negative elements appear at one end and positive elements appear at the other?
    

#Solution1:Time complexity O(n) with extra space
def rearrange(lst):
  left_lst=[]
  right_lst=[]
  #making list of postive and negative numbers

  for i in lst:
    if i<0:
      left_lst.append(i)
    else:
      right_lst.append(i)
  #merging two list
  return left_lst+right_lst

#Solution 2:Time complexity is O(n) as is iterated over twice 
def rearrange(lst):
  return [i for i in lst if i<0] +[i for i in lst if i>=0]


# Question 8:Rearrange Sorted List in Max/Min Form.

#Arrange elements in such a way that the maximum element appears   at first position, then minimum at second, then second maximum at third and second minimum at fourth and so on.

def max_min(lst):
  result=[]
  for i in range(len(lst)//2):
    # Append corresponding last max element
    result.append(lst[-(i+1)])
    # append current or first min element
    result.append(lst[i])
    print(result)
  #if list is odd numbered
  if len(lst) % 2 !=0:
    # if middle value then append
    result.append(lst[len(lst)//2])
  return result

# Question 9:Maximum Sum Sublist

#Given an array, find the contiguous sublist with the largest sum.

#Solution 1: Time complexity O(n^2)
def find_max_sum_sublist(lst):
  max_sum=lst[0]
  for i in range(len(lst)):
    start=lst[i]
    
    for j in range(i+1,len(lst)):
      start+=lst[j]
     
      if max_sum<start:
        max_sum=start
     
  return max_sum

#Solution 2: Using Kadane 's Algorithm by using current max and global max concept, runtime complexity O(n)

def find_max_sum_sublist(lst): 
  if (len(lst) < 1): 
    return 0
   
  curr_max = lst[0]
  global_max = lst[0]
  for i in range(1, len(lst)):
    if curr_max < 0: 
      curr_max = lst[i]
    else:
      curr_max += lst[i]
    if global_max < curr_max:
      global_max = curr_max

  return global_max


# Question 10: Minimum Index Sum of Two Lists(From leetcode).

#     You need to find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. 
#     You could assume there always exists an answer.

def findRestaurant(list1,list2):
   common_dict={}
   for index,value in enumerate(list1):
     if value in list2:
       index_sum=list2.index(value)+index
       common_dict[value]=index_sum
   temp=min(common_dict.values())
   result=[key for key in common_dict if common_dict[key]==temp]
  

   return result


# Question 11:Decompress Run-Length Encoded List(LeetCode).

#     Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. 
#     Concatenate all the sublists from left to right to generate the decompressed list.

#nums = [1,1,2,3]
#output [1,3,3]

def decompressRLElist(List):
   result=[]
   for i in range(0,len(List),2):
      value=[List[i+1]]*List[i]
      result.extend(value)

   return result


#Question 12:Factoral of a number

def factorial(n):
  if n<=1:
    return 1
  else:
    return n * factorial(n-1)


# Question 13: Fibonacci Number 

# Solution 1
def fibonacci(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)


#Solution 2: Using memorization concecpt, runtime will be reduced

def fibonacci(n,memo={}):
  if n in memo:
    return memo[n]
  elif n<=2:
    return 1
  memo[n]=fibonacci(n-1,memo) + fibonacci(n-2,memo)
  return memo[n]


#Question 14: Fibonacci Series

def fibonacci(n,k,memo={}):
  if n in memo:
    return memo[n]
  elif n<=2:
    return 1
  memo[n]=fibonacci(n-1,n) + fibonacci(n-2,n)
  if n==k:
    final_list = [0,1,1]
    final_list.extend(memo.values())
    return final_list
  return memo[n]

# fibonacci(6,6) 
# [0, 1, 1, 2, 3, 5, 8]


# Question 15:Palindrome Number
def isPalindrome(x):
  if str(x)[::-1]==str(x):
    return True
  else:
    return False

# Question 16:Given a string s, return true if the s can be palindrome after deleting at most one character from it.

def validPalindrome(s):
  reverse = s[::-1]
  if s == reverse:
    return True
  else:
    for i, j in enumerate(s):
      if reverse[i] != j:
        reverse = reverse[:i] + reverse[i+1:]
        if reverse == reverse[::-1]:
          return True
       
        s = s[:i] + s[i+1:]
        return s == s[::-1]
        

# Question 18: Grid search to go from start from the grid to end of the grid


#Solution 1
def grid_search(x,y):
  #if this happens you reached the end of grid
  if (x==1 and y==1):
    return 1
  #reached the end
  elif (x==0 or y==0):
    return 0
  else:
    return grid_search(x-1,y) + grid_search(x,y-1)


# grid_search(x=5,y=4)
# 35

# Solution 2: using memo
def grid_search(x,y,memo={}):
  val = str(x)+","+str(y)
  rev_val = str(y)+","+str(x)
  if (val in memo):
    return memo[val]
  elif rev_val in memo:
    return memo[rev_val]
  #if this happens y if x in memo and 
  if (x==1 and y==1):
    return 1
  #reached the end
  if (x==0 or y==0):
    return 0
  
  memo[val] = grid_search(x-1,y,memo) + grid_search(x,y-1,memo)
  return memo[val]


#Question 19: Using list comprehenision print even and odd for number in list

def oddEven(nums):
  values=["even" if number%2==0 else "odd" for number in nums]
  return values

# Question 19: Given sorted list with duplicates return a unqiue list
# Solution 1:
def unique(nums):
  temp = []
  for i in nums:
    if i not in temp:
      temp.append(i)
  return temp

# Solution 2: Using list comprehension
nums=[0,0,1,1,1,2,2,3,3,4]
[nums.remove(x) for x in nums if nums.count(x)> 1]
nums


# Question 20:Factorial Trailing Zeroes
# Given an integer n, return the number of trailing zeroes in n!.

# Solution:
def trailingZeroes(n):
  number=factorial(n)
  new_num = str(number)
  count = len(new_num) - len(new_num.rstrip("0"))
  return count



#Solution 2:
def trailingZeroes(n):
  count = 0
  while n > 0:
    
    n = n // 5
    count += n
  return count