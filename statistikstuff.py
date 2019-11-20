import csv 

with open('radon.csv', 'r') as csv_file:
    
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    prevCounty = ""
    sumRadon = 0
    sumPop = 0

    #skip first line containing column names 
    next(csv_reader)

    for row in csv_reader: 
        countyname = row[1]
        sampsize = float(row[2])
        popsize = float(row[3])
        radon = float(row[4])
        #new county
        if not countyname == prevCounty:
            prevCounty = countyname
            sumPop = sumPop + popsize
        #used to calculate weighted mean 
        sumRadon = sumRadon + float(radon*popsize/sampsize)

    mean = float(sumRadon/sumPop)
    print("mean: ", mean)