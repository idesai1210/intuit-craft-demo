import numpy as np


def listOfAllDepartments(original_df):
    deptAll = list(original_df["Group"].unique())
    deptList = []
    i = 0
    for l in deptAll:
        deptList.append({"ID": i, "Department": l})
        i = i + 1

    return deptList


def listOfAllAppByDepartments(original_df):
    appByDept = original_df["Group"].unique()
    appByDeptList = []
    i = 0
    for l in appByDept:
        listOfApp = list(original_df.loc[original_df['Group'] == l]["Application"].unique())
        listOfApp = ','.join(listOfApp)
        appByDeptList.append({"ID": i, "Department": l, "Applications": listOfApp})
        i = i+1

    return appByDeptList


def noOfCPUMemByDep(original_df):

    groupByDept = original_df.groupby('Group')
    allDept = original_df["Group"].unique()

    noOfCpu = groupByDept['CPU cores'].agg([np.sum])
    totalMemory = groupByDept['RAM (MB)'].agg([np.sum])

    cpuMemDeptList = []
    i = 0
    for l in allDept:
        cpuMemDeptList.append({"ID": i, "Department": l, "CPU": noOfCpu["sum"][l], "Memory": totalMemory["sum"][l]})
        i = i + 1

    return cpuMemDeptList

def noOfCPUMemByApp(original_df):

    groupByDept = original_df.groupby('Application')
    allApps = original_df["Application"].unique()

    noOfCpu = groupByDept['CPU cores'].agg([np.sum])
    totalMemory = groupByDept['RAM (MB)'].agg([np.sum])

    cpuMemAppList = []
    i = 0
    for l in allApps:
        cpuMemAppList.append({"ID": i, "Application": l, "CPU": noOfCpu["sum"][l], "Memory": totalMemory["sum"][l]})
        i = i + 1

    return cpuMemAppList


def noOfCPUMemByDataCenters(original_df):

    groupBySite = original_df.groupby('Site')
    allSites = original_df["Site"].unique()

    noOfCpu = groupBySite['CPU cores'].agg([np.sum])
    totalMemory = groupBySite['RAM (MB)'].agg([np.sum])

    cpuMemDCList = []
    i = 0
    for l in allSites:
        cpuMemDCList.append({"ID": i, "Site": l, "CPU": noOfCpu["sum"][l], "Memory": totalMemory["sum"][l]})
        i = i + 1

    return cpuMemDCList
