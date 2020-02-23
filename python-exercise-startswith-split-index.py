#set input then save it inside fname variable
fname = input("Enter file name: ")

if len(fname) < 1 : fname = "mbox-short.txt"

#open the variable and save it inside a file handler
fh = open(fname)

#set a variable counter
count = 0

#set definite loop for each line inside fh file handler
for line in fh:
    
    #filter if the line starts with "From:"
    if line.startswith("From:") :
        
        #print the line but it is splitted and return 2nd list
        print(line.split()[1])
        
        #increment the count of the line + 1
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
