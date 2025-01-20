"""
Author : Mehmet Yucel
Student Number: 759742
Revison date : 15 Jan 2025
Program : Report: Credit Card 
Description : Report of all credit cards in the customer database that have expired.
VARIABLE DICTIONARY :
    filename: str - Name of the file
    fh: file object - File handle
    names: list - List of names (first and last)
    cc_nums: list - List of credit card numbers
    cc_types: list - List of credit card types
    expiry_dates: list - List of expiry dates
    lines: list - List of all the lines in file
    first_line: str - First line of the file (to be removed from lines)
    output_file: file object - File handle for the output file
    expired_text: str - Text to display when expired
"""




def mergeSort(arr, arr2, arr3, arr4, l, r):
    if l < r:
        
        m = l + (r - l) // 2
   
        mergeSort(arr, arr2, arr3, arr4, l, m)
        mergeSort(arr, arr2, arr3, arr4, m + 1, r)
        merge(arr, arr2, arr3, arr4, l, m, r)
        

def merge(arr, arr2, arr3, arr4, l, m, r):
    n1 = m - l + 1
    n2 = r - m
   
    L = [0] * (n1)
    L2 = [0] * (n1)
    L3 = [0] * (n1)
    L4 = [0] * (n1)
    R = [0] * (n2)
    R2 = [0] * (n2)
    R3 = [0] * (n2)
    R4 = [0] * (n2)
    
    for i in range(0, n1):
        L[i] = arr[l + i]
        L2[i] = arr2[l + i]
        L3[i] = arr3[l + i]
        L4[i] = arr4[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
        R2[j] = arr2[m + 1 + j]
        R3[j] = arr3[m + 1 + j]
        R4[j] = arr4[m + 1 + j]
    
    i = 0  
    j = 0  
    k = l  
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            arr2[k] = L2[i]
            arr3[k] = L3[i]
            arr4[k] = L4[i]
            i += 1
        else:
            arr[k] = R[j]
            arr2[k] = R2[j]
            arr3[k] = R3[j]
            arr4[k] = R4[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        arr2[k] = L2[i]
        arr3[k] = L3[i]
        arr4[k] = L4[i]
        i += 1
        k += 1
   
    while j < n2:
        arr[k] = R[j]
        arr2[k] = R2[j]
        arr3[k] = R3[j]
        arr4[k] = R4[j]
        j += 1
        k += 1


filename = "data.dat"
fh = open(filename, 'r')

names = []
cc_nums = []
cc_types = []
expiry_dates = []

lines = fh.readlines()
first_line = lines.pop(0)
for line in lines:
    given_name, surname, cc_type, cc_number, exp_mo, exp_yr = line.strip().split(',')
    name = given_name + ' ' + surname
    names.append(name)
    cc_types.append(cc_type)
    cc_nums.append(cc_number)
    if len(exp_mo) == 1:
        exp_mo = '0' + exp_mo
    expiry_date = exp_yr + exp_mo
    expiry_dates.append(int(expiry_date))

fh.close()

mergeSort(expiry_dates, names, cc_nums, cc_types, 0, len(expiry_dates) - 1)
output_file = open("output.txt","w")
for i in range(len(expiry_dates)):
    if expiry_dates[i] > 202501:
        break
    expired_text = "RENEW IMMEDIATELY"
    if expiry_dates[i] < 202501:
        expired_text = "EXPIRED"
    print("%-35s %-15s %-20s %-8s %-15s" % (names[i], cc_types[i], cc_nums[i], expiry_dates[i], expired_text))
    output_file.write("%-35s %-15s %-20s %-8s %-15s\n" % (names[i], cc_types[i], cc_nums[i], expiry_dates[i], expired_text))
output_file.close()