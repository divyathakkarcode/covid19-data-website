## Contains method for sorting through different fields data
#  The data table parameter is the dictionary with all the data read from the .txt file


def getRequiredColumns(dataTable, sortColumn):
    dict = dataTable

    #making a 2d list with the required columns
    requiredList = []
    for entry in dict:
        requiredList.append([entry, dict[entry][sortColumn]])

    #sorting the 2d list based on the second column (sortColumn) first
    #sorting by country name (first column) if it is a tie
    sortedList = sorted(requiredList, key = lambda x:(x[1], x[0]))

    return sortedList



def sortTotalCases(dataTable):
    #getting and sorting the required columns
    sortedList = getRequiredColumns(dataTable, "Total_Cases")
    
    #column names
    countryCol = 0
    casesCol = 1


    #writing to results to the file
    file = open("Total_Cases.txt", "w")
    for i in range(len(sortedList)):
        file.write(sortedList[i][countryCol] + ", " + str(sortedList[i][casesCol]) + "\n")


def sortNewCases(dataTable):
    #getting and sorting the required columns
    sortedList = getRequiredColumns(dataTable, "New_Cases")
    
    #column names
    countryCol = 0
    casesCol = 1


    #writing to results to the file
    file = open("New_Cases.txt", "w")
    for i in range(len(sortedList)):
        file.write(sortedList[i][countryCol] + ", " + str(sortedList[i][casesCol]) + "\n")


def sortTotalDeaths(dataTable):
    #getting and sorting the required columns
    sortedList = getRequiredColumns(dataTable, "Total_Deaths")
    
    #column names
    countryCol = 0
    casesCol = 1


    #writing to results to the file
    file = open("Total_Deaths.txt", "w")
    for i in range(len(sortedList)):
        file.write(sortedList[i][countryCol] + ", " + str(sortedList[i][casesCol]) + "\n")
    

def sortTotalRecovered(dataTable):
    #getting and sorting the required columns
    sortedList = getRequiredColumns(dataTable, "Total_Recovered")
    
    #column names
    countryCol = 0
    casesCol = 1


    #writing to results to the file
    file = open("Total_Recovered.txt", "w")
    for i in range(len(sortedList)):
        file.write(sortedList[i][countryCol] + ", " + str(sortedList[i][casesCol]) + "\n")

def sortActiveCases(dataTable):
    #getting and sorting the required columns
    sortedList = getRequiredColumns(dataTable, "Active_Cases")
    
    #column names
    countryCol = 0
    casesCol = 1


    #writing to results to the file
    file = open("Active_Cases.txt", "w")
    for i in range(len(sortedList)):
        file.write(sortedList[i][countryCol] + ", " + str(sortedList[i][casesCol]) + "\n")

def main():
    dict = {"USA": {"Total_Cases": 200, "New_Cases": 300},
            "India": {"Total_Cases": 2030, "New_Cases": 300},
            "Canada": {"Total_Cases": 900, "New_Cases": 10},
            "Other": {"Total_Cases": 200, "New_Cases": 99}}

    sortTotalCases(dict)
    sortNewCases(dict)

main()