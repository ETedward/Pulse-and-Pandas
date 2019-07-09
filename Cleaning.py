import csv

with open ('partnered1m.csv', 'w') as new:

    data = open("Dev_Pulse_1m.csv", "r")
    reader = csv.reader(data)

    headers = next(reader, None) # column headers
    #print(headers)

    lines = 0
    for l in reader: #l is the line
        # date, name, partner, level, site
        if l[8] not in (None, ""):
            new.write(l[0] + "," + l[5] + "," + l[8] + "," + l[9] + " " + l[11] + ",")
            tmp = str(float(l[12]) + float(l[13]) + float(l[14]))

            new.write(tmp + "\n")
            lines = lines + 1

    data.close()

new.close()
print("done")

