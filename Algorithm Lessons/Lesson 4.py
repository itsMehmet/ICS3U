# Predict
"""
Predict A:
3 4 1 2 6 
9 2 3 7 5 
4 2 1 0 3 

Predict B:
[[3, 4, 1, 2, 6], [9, 2, 3, 7, 5], [4, 2, 1, 0, 3]]
"""

# Modify
ar2 = [[3, 4, 1, 2, 6],
      [9, 2, 3, 7, 5],
      [4, 2, 1, 0, 3]]
added_ar = []
for i in range(len(ar2)):
  ar3 = ar2[i]
  amount = 0
  for j in range(len(ar3)):
      amount += ar3[j]
  added_ar.append(amount)

print(added_ar)
