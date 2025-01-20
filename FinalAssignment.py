"""
Author : Mehmet Yucel    
Student Number: 759742
Revison date : 20 Jan 2025
Program : Credit Card Report
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

"""
Function to perform merge sort on two arrays.
Parameters:
    arr (list): Array to be sorted.
    arr2, arr3, arr4 (list): Other arrays to be sorted.
    l (int): Left index of the subarray.
    r (int): Right index of the subarray.
"""
def mergeSort(arr, arr2, arr3, arr4, l, r):
    # Check if the subarray has more than one element
    if l < r:
        # Find the middle point to divide the array into two halves
        # Avoids potential overflow for large values of l and r
        m = l + (r - l) // 2
        
        # Sort first and second halves
        mergeSort(arr, arr2, arr3, arr4, l, m)
        mergeSort(arr, arr2, arr3, arr4, m + 1, r)
        merge(arr, arr2, arr3, arr4, l, m, r)
        
"""
Function to merge two sorted arrays.
Parameters:
    arr (list): Array to be sorted.
    arr2, arr3, arr4 (list): Other arrays to be sorted.
    l (int): Left index of the subarray.
    m (int): Middle index of the subarray.
    r (int): Right index of the subarray.
"""
def merge(arr, arr2, arr3, arr4, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    # Create temp arrays
    L = [0] * (n1)
    L2 = [0] * (n1)
    L3 = [0] * (n1)
    L4 = [0] * (n1)
    R = [0] * (n2)
    R2 = [0] * (n2)
    R3 = [0] * (n2)
    R4 = [0] * (n2)
    # Copy data to temp arrays L[] and R[]
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
    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray
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
    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        arr2[k] = L2[i]
        arr3[k] = L3[i]
        arr4[k] = L4[i]
        i += 1
        k += 1
    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        arr2[k] = R2[j]
        arr3[k] = R3[j]
        arr4[k] = R4[j]
        j += 1
        k += 1

# Open the file
filename = "data.dat"
fh = open(filename, 'r')

# Create lists for names, cc numbers, cc types, and expiry dates
names = []
cc_nums = []
cc_types = []
expiry_dates = []

# Read all the lines from file in add data into lists
lines = fh.readlines()
# Remove first line from the list
first_line = lines.pop(0)
for line in lines:
    # Split each line into components
    given_name, surname, cc_type, cc_number, exp_mo, exp_yr = line.strip().split(',')
    # Add first and last name together
    name = given_name + ' ' + surname
    # Add name to names list
    names.append(name)
    # Add cc_type to list
    cc_types.append(cc_type)
    # Add cc_number to list
    cc_nums.append(cc_number)
    # Adds a leading zero to single digit month
    if len(exp_mo) == 1:
        exp_mo = '0' + exp_mo
    # Adds month and year together into expiry_date
    expiry_date = exp_yr + exp_mo
    # Add expiry_date to list in type int
    expiry_dates.append(int(expiry_date))

# Close the file
fh.close()

# Sort the lists using merge sort
mergeSort(expiry_dates, names, cc_nums, cc_types, 0, len(expiry_dates) - 1)
# Open the output file
output_file_name = "output.txt"
output_file = open(output_file_name,"w")
# Loop through the expiry_dates list
for i in range(len(expiry_dates)):
    # Break if the expiry date is larger than 202501, meaning it is not expiried
    if expiry_dates[i] > 202501:
        break
    # Set expired_text string
    expired_text = "RENEW IMMEDIATELY"
    # If expiry date is lower than 202501 than set string to EXPIRED
    if expiry_dates[i] < 202501:
        expired_text = "EXPIRED"
    # Print the data
    print("%-35s %-15s %-20s %-10s %-15s" % (names[i] + ':', cc_types[i], '#' + cc_nums[i], expiry_dates[i], expired_text))
    # Write data to output file
    output_file.write("%-35s %-15s %-20s %-10s %-15s\n" % (names[i] + ':', cc_types[i], '#' + cc_nums[i], expiry_dates[i], expired_text))
# Close the output file
output_file.close()
print("\nOutput sent to %s" % output_file_name)
