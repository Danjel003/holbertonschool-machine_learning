#!/usr/bin/env python3
arr = [9, 8, 2, 3, 9, 4, 1, 0, 3]
arr1 = arr[:2]  # Merr dy elementët e parë
arr2 = arr[-5:]  # Merr pesë elementët e fundit
arr3 = arr[1:6]  # Merr nga elementi i dytë deri tek i gjashti
print("The first two numbers of the array are: {}".format(arr1))
print("The last five numbers of the array are: {}".format(arr2))
print("The 2nd through 6th numbers of the array are: {}".format(arr3))