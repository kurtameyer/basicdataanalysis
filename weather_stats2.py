from sys import argv

#This program takes a text file of weather station data and performs rudimentary data cleaning and analysis tasks.
# Command line functionality is included for flexibility.  

def compute_stats(value_list):
    # Median calculation using modulo and list index positions.
    # Assume that the incoming list is sorted.

    # Check the length of the list (test for empty list)
    if len(value_list) == 0:
        return (None, None, None, None)

    # Test whether length is odd or even
    if len(value_list)%2 == 0:
        median1 = value_list[len(value_list)//2]
        median2 = value_list[len(value_list)//2-1]
        median = (median1 + median2)/2
    else:
        median = value_list[len(value_list)//2]

    #Mean, max, and min calculated and assigned variables.
    mean = sum(value_list)/len(value_list)
    min_value = value_list[0]
    max_value = value_list[len(value_list)-1]
    return (min_value, max_value, mean, median)


def main():

    import sys
    import csv
    
    #print(sys.argv)
    # If argv length > 1, and we have a number as the second item,
    # then it is probably specifying a column number to read....
    #User will input column number on a 1-10 basis
    if len(sys.argv)>1:
        the_column = int(sys.argv[1]) -1
    else:
        the_column = 1
  
    value_list =[]
    with open (sys.argv[2], "r") as csv_file:
        csv_reader = csv.reader(csv_file, skipinitialspace=True, delimiter = ' ')
        #for line in fp:
        for line in csv_reader:
            #To be safe I wrote my command line script to include one position to the left and right of field 9. Now I'm stripping whitespace to compensate.
            #value = line.strip()
            #print(line)
            value = line[the_column]
            #Skip 9999.
            if "9999" in value:
                continue
            #Cast value to float to perform math calculations.
            value = float(value)
            #Append empty list with clean values from data.
            value_list.append(value)
            #Sorting list in ascending order.
    value_list.sort()

    min_value,max_value,mean,median = compute_stats(value_list)

    print (f"min:{min_value} max: {max_value} average: {mean} median: {median}")
    #Tested list to ensure 9999's were successfully removed.
    #print (value_list)

#print (main("data.txt"))

if __name__ == "__main__":
    main()
