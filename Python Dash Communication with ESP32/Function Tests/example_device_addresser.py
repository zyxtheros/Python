import csv


fields = ['alias','address'] # component definition paramaters
address_loc = "Function Tests/addresser.csv"
def get_addresses( addressFile: list, names: list, printout=False):
    with open(addressFile, newline="\n") as csvfile: # note that "with" automatically closes the file once finished
        reader = csv.DictReader(csvfile, delimiter=",", quotechar='"', fieldnames=names)

        output={names[0]:[], names[1]:[]}
        #for row in addresses:
         #   for i in range(0, len(names)):
         #       output[names[i]].append(row[i])
                #print(row[i])
            #mydictionary[names[0]].append(row[0])
            #print(row[1])
            #mydictionary[names[1]].append(row[1])
        output = {row[names[0]]:int(row[names[1]],16) for row in reader }
        if printout == True:
            for row in output:
                #print(row, output[row])
                print("Alias:\t%s\t\tAddress:\t%x"%(row, output[row]))
    return output

# main/test
my_dev = get_addresses(address_loc, fields, True)
print(my_dev)
