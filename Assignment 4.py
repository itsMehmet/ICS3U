def sort(words, dates):
    pass

def merge(year, month, day):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    line_int = ""
    line_int += year
    month_str = str(months.index(month) + 1)
    if len(month) == 1:
        month_str = "0" + month_str
    line_int += month_str
    line_int += day
    return(int(line_int))
    

filename = "wordle.dat"
fh = open(filename, "r")

lines = fh.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

lines_int = []
for line in lines:
    month, day, year, word = line.split()
    myDate = merge(year, month, day)
    lines_int.append(myDate)
    

