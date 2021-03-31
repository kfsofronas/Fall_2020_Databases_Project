import csv

# print("\nCar_Model Inserts:\n")
with open('car_model.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        output = "INSERT INTO CAR_MODEL VALUES ("
        for i in row:
            if(i == "NULL"):
                output = output + "NULL,"
            else:
                output = output + "\'" + i + "\',"
        output = output[:len(output)-1] + ");"
        print(output)

# print("\nDealership Inserts:\n")
with open('dealership.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        output = "INSERT INTO DEALERSHIP VALUES ("
        # print("\t row = " + ",".join(row))
        for i in row:
            splt2 = i.split("'")
            # print("\t\t splt2 = " + ",".join(splt2))
            if(len(splt2) == 1):
                if (i == "NULL"):
                    output = output + "NULL,"
                else:
                    output = output + "\'" + i + "\',"
            else:
                # print("\t\t\t\t splt2[0] = " + splt2[0] + "\n\t\t\t\t splt2[1] = " + splt2[1])
                temp = ""
                for k in splt2:
                    # print("\t\t\t\t\t k = " + k)
                    temp = temp + "\'" + k + "\'"
                output = output + "\'" + temp[1:len(temp)-1] + "\',"
        output = output[:len(output)-1] + ");"
        print(output)

# print("\nSalesperson Inserts:\n")
with open('salesperson.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        output = "INSERT INTO SALESPERSON VALUES ("
        for i in row:
            if (i == "NULL"):
                output = output + "NULL,"
            else:
                output = output + "\'" + i + "\',"
        output = output[:len(output)-1] + ");"
        print(output)

# print("\nCar Inserts:\n")
with open('car.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        output = "INSERT INTO CAR VALUES ("
        for i in row:
            if (i == "NULL"):
                output = output + "NULL,"
            else:
                output = output + "\'" + i + "\',"
        output = output[:len(output)-1] + ");"
        print(output)

# print("\nOwner Inserts:\n")
with open('owner.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        output = "INSERT INTO OWNER VALUES ("
        for i in row:
            if (i == "NULL"):
                output = output + "NULL,"
            else:
                output = output + "\'" + i + "\',"
        output = output[:len(output)-1] + ");"
        print(output)

# print("\nAccident_History Inserts:\n")
with open('accident_history.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        output = "INSERT INTO ACCIDENT_HISTORY VALUES ("
        for i in row:
            if (i == "NULL"):
                output = output + "NULL,"
            else:
                output = output + "\'" + i + "\',"
        output = output[:len(output)-1] + ");"
        print(output)
