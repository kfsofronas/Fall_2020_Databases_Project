b = True
where = ""
detail = input("Do you want *simple* or *detailed* results? ")
while b:
    where = where + " AND "
    temp = input("What (other) qualities do you want to search for? \nex. New/Used, Asking Price, Mileage, Color, Model Name, Manufacturer, Body Style, Drive Type, Year, Transmission, Fuel, City MPG, Highway MPG)\n Type \"done\" when finished. ")
    if temp == "done":
        b = False
        where = where[5:len(where)-5]
    elif temp == "Asking Price" or temp == "Mileage" or temp == "Year" or temp == "City MPG" or temp == "Highway MPG":
        temp2 = input("Greater than, Less than, or exactly equal to what? (example \"< 3000\") ") # example "< 3000"
        if temp == "Asking Price":
            where = where + "c.AskingPrice " + temp2
        elif temp == "City MPG":
            where = where + "m.MPG_City " + temp2
        elif temp == "Highway MPG":
            where = where + "m.MPG_Highway " + temp2
        elif temp == "Year":
            where = where + "m.Year " + temp2
        elif temp == "Mileage":
            where = where + "c.Mileage " + temp2

    elif temp == "New/Used":
        temp2 = input("Do you want a New or Used car? ")
        where = where + "c.NewOrUsed = '" + temp2 + "'"
    elif temp == "Color":
        temp2 = input("What color do you want? ")
        where = where + "c.Color = '" + temp2 + "'"
    elif temp == "Model Name":
        temp2 = input("What Model Name do you want? ")
        where = where + "m.Model_Name = '" + temp2 + "'"
    elif temp == "Manufacturer":
        temp2 = input("What Manufacturer do you want? ")
        where = where + "m.Manufacturer = '" + temp2 + "'"
    elif temp == "Body Style":
        temp2 = input("What Body Style do you want? (SUV, Minivan, Pickup, Sedan, Chassis, Coupe, Van, Wagon, Convertible) ")
        where = where + "m.Body_Style = '" + temp2 + "'"
    elif temp == "Drive Type":
        temp2 = input("What Drive Type do you want? (FWD, AWD, 4WD, RWD) ")
        where = where + "m.Drive_Type = '" + temp2 + "'"
    elif temp == "Transmission":
        temp2 = input("What Transmission style do you want? (Automatic, Manual) ")
        where = where + "m.Transmission = '" + temp2 + "'"
    elif temp == "Fuel":
        temp2 = input("What type of fuel do you want to use? (Gasoline, Diesel, Flexible-Fuel) ")
        where = where + "m.Fuel = '" + temp2 + "'"

if(detail == "simple"):
    print("\nSELECT VIN, NewOrUsed, Year, Model_Name, Manufacturer, AskingPrice, Mileage, Color, (SELECT COUNT(VIN) FROM Accident_History a WHERE a.VIN = c.VIN) as Accidents_Reported FROM car c, car_model m WHERE c.Model_ID = m.Model_ID AND " + where + ";")
elif(detail == "detailed"):
    print("\nSELECT VIN, NewOrUsed, Year, Model_Name, Manufacturer, AskingPrice, Mileage, Color, (SELECT COUNT(VIN) FROM Accident_History a WHERE a.VIN = c.VIN) as Accidents_Reported, Body_Style, Drive_Type, Transmission, Engine, Fuel, MPG_City, MPG_Highway, Fname as Salesperson_Fname, Lname as Salesperson_Lname, Employee_Phone as Salesperson_Phone, Dealership_Name, Dealership_Address FROM car c, car_model m, salesperson s, dealership d WHERE c.Model_ID = m.Model_ID AND c.Salesperson_ID = s.Employee_ID AND c.Dealership_ID = d.Dealership_ID AND " + where + ";")