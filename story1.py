import pandas as pd
import xlrd
import numpy as np

def listOfAllDepartments(d):
    ls = list(d["Group"].unique())
    deptDict = []
    i = 0
    for l in ls:
        deptDict.append({"ID": i, "Department": l})
        i = i + 1
    return deptDict

def listOfAllAppByDepartments(d):
    ls = d["Group"].unique()
    tempDict = []
    i = 0
    for l in ls:
        listOfApp = list(d.loc[d['Group'] == l]["Application"].unique())
        listOfApp = ','.join(listOfApp)
        tempDict.append({"ID": i, "Department": l, "Applications": listOfApp})
        i = i+1

    return tempDict

def noOfCPUMemByDep(d):

    group = d.groupby('Group')
    #print(group)
    cpu_json = group['CPU cores'].agg([np.sum]).to_json(orient='index')
    #print(group['CPU cores'].agg([np.sum]))
    memory = group['RAM (MB)'].agg([np.sum]).to_json(orient='index')
    return [("CPU", cpu_json), ("Memory", memory)]

def noOfCPUMemByApp(d):

    group = d.groupby('Application')
    cpu_json = group['CPU cores'].agg([np.sum]).to_json(orient='index')
    memory = group['RAM (MB)'].agg([np.sum]).to_json(orient='index')
    return [("CPU", cpu_json), ("Memory", memory)]

def noOfCPUMemByDataCenters(d):

    group = d.groupby('Site')
    cpu_json = group['CPU cores'].agg([np.sum]).to_json(orient='index')
    memory = group['RAM (MB)'].agg([np.sum]).to_json(orient='index')
    return [("CPU", cpu_json), ("Memory", memory)]

def main():
    # Assign spreadsheet filename to `file`
    file = 'hardware.xlsx'

    # Load spreadsheet
    xl = pd.ExcelFile(file)

    # Print the sheet names
    print(xl.sheet_names)

    # Load a sheet into a DataFrame by name: df1
    df1 = xl.parse('Page 1')


    # List of All Departments that has an application hosted

    uniqueDepartments = listOfAllDepartments(df1)


    # Number of CPU and Memory used by each departments

    noOfCPUMemByDepartment = noOfCPUMemByDep(df1)
    print(noOfCPUMemByDepartment)

    # Number of CPU and Memory used by each Data centers
    noOfCPUMemByDC = noOfCPUMemByDataCenters(df1)
    print(noOfCPUMemByDC)

    # Number of CPU and Memory used by each Data centers
    noOfCPUMemByApplication = noOfCPUMemByApp(df1)
    print(noOfCPUMemByApplication)



    print(listOfAllAppByDepartments(df1))


if __name__ == "__main__":
    main()