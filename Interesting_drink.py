Input
The first line of the input contains a single integer n (1 ≤ n ≤ 100 000) — the number of shops in the city that sell Vasiliy's favourite drink.

The second line contains n integers xi (1 ≤ xi ≤ 100 000) — prices of the bottles of the drink in the i-th shop.

The third line contains a single integer q (1 ≤ q ≤ 100 000) — the number of days Vasiliy plans to buy the drink.

Then follow q lines each containing one integer mi (1 ≤ mi ≤ 109) — the number of coins Vasiliy can spent on the i-th day.

Output
Print q integers. The i-th of them should be equal to the number of shops where Vasiliy will be able to buy a bottle of the drink on the i-th day.

code:
import bisect;c=int;p=input;p();x=sorted(map(c,p().split()))
for i in' '*c(p()):print(bisect.bisect(x,c(p())))
  

Bisect Algorithm Functions in Python
Difficulty Level : Medium
Last Updated : 19 Feb, 2021
The purpose of Bisect algorithm is to find a position in list where an element needs to be inserted to keep the list sorted.

Python in its definition provides the bisect algorithms using the module “bisect” which allows to keep the list in sorted order after insertion of each element. This is essential as this reduces overhead time required to sort the list again and again after insertion of each element.

Important Bisection Functions

1. bisect(list, num, beg, end) :- This function returns the position in the sorted list, where the number passed in argument can be placed so as to maintain the resultant 
list in sorted order. If the element is already present in the list, the right most position where element has to be inserted is returned. This function takes 4 arguments, 
list which has to be worked with, number to insert, starting position in list to consider, ending position which has to be considered.

2. bisect_left(list, num, beg, end) :- This function returns the position in the sorted list, where the number passed in argument can be placed so as to maintain the resultant
list in sorted order. If the element is already present in the list, the left most position where element has to be inserted is returned.This function takes 4 arguments, list 
which has to be worked with, number to insert, starting position in list to consider, ending position which has to be considered.
