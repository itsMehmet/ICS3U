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
    # Proceed only if the segment has more than one element
    if l < r:
        # Calculate the middle index to divide the segment into two halves
        m = l + (r - l) // 2
       
        # Recursively sort the left and right halves
        mergeSort(arr, arr2, arr3, arr4, l, m)
        mergeSort(arr, arr2, arr3, arr4, m + 1, r)
        merge(arr, arr2, arr3, arr4, l, m, r)
       
"""
Merges two sorted portions of arrays into one sorted portion.
Parameters:
    arr (list): Main array to be sorted.
    arr2, arr3, arr4 (list): Additional arrays to align with the main array.
    l (int): Start index of the segment.
    m (int): Middle index of the segment.
    r (int): End index of the segment.
"""
def merge(arr, arr2, arr3, arr4, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    # Create temporary arrays for the two halves
    L = [0] * n1
    L2 = [0] * n1
    L3 = [0] * n1
    L4 = [0] * n1
    R = [0] * n2
    R2 = [0] * n2
    R3 = [0] * n2
    R4 = [0] * n2
    # Copy data from the main arrays to the temporary arrays
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
    # Merge the temporary arrays back into the main arrays
    i, j, k = 0, 0, l
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
    # Add remaining elements from the left half, if any
    while i < n1:
        arr[k] = L[i]
        arr2[k] = L2[i]
        arr3[k] = L3[i]
        arr4[k] = L4[i]
        i += 1
        k += 1
    # Add remaining elements from the right half, if any
    while j < n2:
        arr[k] = R[j]
        arr2[k] = R2[j]
        arr3[k] = R3[j]
        arr4[k] = R4[j]
        j += 1
        k += 1

# Open and read the data file
filename = "data.dat"
fh = open(filename, 'r')

# Initialize lists for names, credit card numbers, types, and expiry dates
names = []
cc_nums = []
cc_types = []
expiry_dates = []

# Read all lines from the file and organize the data into lists
lines = fh.readlines()
# Remove the header line
lines.pop(0)
for line in lines:
    # Split each line into components
    given_name, surname, cc_type, cc_number, exp_mo, exp_yr = line.strip().split(',')
    # Combine first and last names into a single string
    name = given_name + ' ' + surname
    names.append(name)
    cc_types.append(cc_type)
    cc_nums.append(cc_number)
    # Format the expiry month to always have two digits
    if len(exp_mo) == 1:
        exp_mo = '0' + exp_mo
    # Combine year and month into a single expiry date
    expiry_date = exp_yr + exp_mo
    expiry_dates.append(int(expiry_date))

# Close the input file
fh.close()

# Sort all lists based on expiry dates
mergeSort(expiry_dates, names, cc_nums, cc_types, 0, len(expiry_dates) - 1)

# Open the output file
output_file_name = "output.txt"
output_file = open(output_file_name, "w")

# Write expired cards to the output file and print them
for i in range(len(expiry_dates)):
    # Stop processing if the expiry date is beyond January 2025
    if expiry_dates[i] > 202501:
        break
    # Determine the expiry status
    expired_text = "RENEW IMMEDIATELY" if expiry_dates[i] < 202501 else "EXPIRED"
    # Format the output
    formatted_output = "%-35s %-15s %-20s %-10s %-15s" % (names[i] + ':', cc_types[i], '#' + cc_nums[i], expiry_dates[i], expired_text)
    print(formatted_output)
    output_file.write(formatted_output + "\n")

# Close the output file
output_file.close()
print("\nOutput saved to %s" % output_file_name)
