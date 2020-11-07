from countryinfo import CountryInfo
import math
def readData():
    f = open("testing.txt", "r")

    Country_Name =  {}

    size = [0, 0, 0, 0, 0, 0]

    for line in f:
        meas = line.split(',')

        for i in range(1,6):
            meas[i] = meas[i].strip()
            if meas[i] == "[]\n":
                meas[i]="[0]\n"
            elif meas[i] == "[]":
                meas[i]="[0]"
            print (meas[i])
        size[0] = len(meas[0])
        size[1] = len(meas[1])
        size[2] = len(meas[2])
        size[3] = len(meas[3])
        size[4] = len(meas[4])
        size[5] = len(meas[5])

        country = CountryInfo( meas[0][2 : (size[0] - 2)])
        lat_lng = country.latlng()

        Country_Name[meas[0][2:(size[0]-2)]] = { meas[0][2 : (size[0] - 2)]: {
            "Total_Cases": int(meas[1][1 : (size[1] - 1)]), 
            "New_Cases": int(meas[2][1 : (size[2] - 1)]),
            "Total_Deaths" : int(meas[3][1 : (size[3] - 1)]),
            "Total_Recovered" : int(meas[4][1 : (size[4] - 1)]),
            "Active_Cases" : int(meas[5][1 : (size[5] - 1)]),
            "Latitude" : lat_lng[0],
            "Longitude" : lat_lng[1]}
        }
    f.close()