## Contains method for sorting through different fields data
#  The data table parameter is the dictionary with all the data read from the .txt file


def getRequiredColumns(dataTable, sortColumn):
    dict = dataTable

    #making a 2d list with the required columns
    requiredList = []
    for entry in dict:
        requiredList.append([entry, dict[entry][sortColumn]])

    #sorting the 2d list based on the second column (sortColumn)
    sortedList = sorted(requiredList, key = lambda x:x[1])

    return sortedList



def sortTotalCases(dataTable):
    return getRequiredColumns(dataTable, "Total_Cases")


def sortNewCases(dataTable):
    return getRequiredColumns(dataTable, "New_Cases")

def sortTotalDeaths(dataTable):
    return getRequiredColumns(dataTable, "Total_Deaths")

def sortTotalRecovered(dataTable):
    return getRequiredColumns(dataTable, "Total_Recovered")

def sortActiveCases(dataTable):
    return getRequiredColumns(dataTable, "Active_Cases")

