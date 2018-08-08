import numpy as np


# This function will get the List of All Unique Departments
def listOfAllDepartments(original_df):
    deptAll = list(original_df["Group"].unique())
    deptList = []
    i = 0
    # Creating JSON String to feed to the web app
    for l in deptAll:
        deptList.append({"ID": i, "Department": l})
        i = i + 1

    return deptList

# This function will get the list of All Applications by Departments
def listOfAllAppByDepartments(original_df):
    appByDept = original_df["Group"].unique()
    appByDeptList = []
    i = 0
    for l in appByDept:
        # Check each application for a particular Department
        listOfApp = list(original_df.loc[original_df['Group'] == l]["Application"].unique())
        listOfApp = ','.join(listOfApp)
        # Creating JSON String to feed to the web app
        appByDeptList.append({"ID": i, "Department": l, "Applications": listOfApp})
        i = i + 1

    return appByDeptList

# This function will calculate Total Number of CPUs and Memory used by each Department
def noOfCPUMemByDep(original_df):
    # Group By Department
    groupByDept = original_df.groupby('Group')
    allDept = original_df["Group"].unique()

    # Aggregate the sum of all rows
    noOfCpu = groupByDept['CPU cores'].agg([np.sum])
    totalMemory = groupByDept['RAM (MB)'].agg([np.sum])

    cpuMemDeptList = []
    i = 0
    for l in allDept:
        # Create JSON String to feed to the web app
        cpuMemDeptList.append({"ID": i, "Department": l, "CPU": noOfCpu["sum"][l], "Memory": totalMemory["sum"][l]})
        i = i + 1

    return cpuMemDeptList

# This function will calculate Total Number of CPUs and Memory used by each Application
def noOfCPUMemByApp(original_df):
    #Group By Application
    groupByDept = original_df.groupby('Application')
    allApps = original_df["Application"].unique()

    #Aggregate the sum of all rows
    noOfCpu = groupByDept['CPU cores'].agg([np.sum])
    totalMemory = groupByDept['RAM (MB)'].agg([np.sum])

    cpuMemAppList = []
    i = 0
    for l in allApps:
        # Create JSON String to feed to the web app
        cpuMemAppList.append({"ID": i, "Application": l, "CPU": noOfCpu["sum"][l], "Memory": totalMemory["sum"][l]})
        i = i + 1

    return cpuMemAppList


# This function will calculate Total Number of CPUs and Memory used by each Data Centers
def noOfCPUMemByDataCenters(original_df):
    # Group By Site
    groupBySite = original_df.groupby('Site')
    allSites = original_df["Site"].unique()

    noOfCpu = groupBySite['CPU cores'].agg([np.sum])
    totalMemory = groupBySite['RAM (MB)'].agg([np.sum])

    cpuMemDCList = []
    i = 0
    for l in allSites:
        # Create JSON String to feed to web app
        cpuMemDCList.append({"ID": i, "Site": l, "CPU": noOfCpu["sum"][l], "Memory": totalMemory["sum"][l]})
        i = i + 1

    return cpuMemDCList
