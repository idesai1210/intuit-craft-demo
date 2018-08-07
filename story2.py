import pandas as pd
import xlrd
import numpy as np


def Estimate(d):

    group = d.groupby('Group')
    # print(group)
    cpu_json = group['Price'].agg([np.sum]).to_json(orient='index')
    print(group['Price'].agg([np.sum]))

    return group['Price'].agg([np.sum])


def main():
    # Assign spreadsheet filename to `file`
    file = 'hardware.xlsx'

    # Load spreadsheet
    xl = pd.ExcelFile(file)

    # Print the sheet names
    print(xl.sheet_names)

    # Load a sheet into a DataFrame by name: df1
    df1 = xl.parse('Page 1')

    file = 'prices.xlsx'
    xl1 = pd.ExcelFile(file)
    print(xl1.sheet_names)
    df2 = xl1.parse('Sheet1')

    print(df1)
    print(df2)

    my_df = {}
    my_df['Type'] = list()
    my_df['Price/Hr'] = list()
    my_df['Price'] = list()

    for index, row in df1.iterrows():
        #print(row["CPU cores"], row["RAM (MB)"])
        #print(df2.loc[(df2['CPU'] <= row["CPU cores"]) | (df2["RAM (MB)"] <= row["RAM (MB)"])].iloc[-1])
        l = df2.loc[(df2['CPU'] <= row["CPU cores"]) | (df2["RAM (MB)"] <= row["RAM (MB)"])].iloc[-1]
        # print(l['Type'])
        my_df['Type'].append(l['Type'])
        my_df['Price/Hr'].append(l['Price/Hr'])
        my_df['Price'].append(float(l['Price/Hr'][1:])*24*7*365)
        #print(d)


    my_df = pd.DataFrame(my_df)

    result = pd.concat([df1, my_df], axis=1, sort=False)

    rs = Estimate(result)
    #print(type(rs))
    costList = []
    for index, row in rs.iterrows():

        if index == 'Engineering':
            year1 = row["sum"]
            year2 = year1*0.10+year1
            year3 = year2*0.10+year2
            costList.append((index, [round(year1, 2), round(year2, 2), round(year3, 2)]))

        if index == 'Sales':
            year1 = row["sum"]
            year2 = year1-year1*0.80
            year3 = year2-year2
            costList.append((index, [round(year1, 2), round(year2, 2), round(year3, 2)]))

        if index == 'Engineering Canada':
            costList.append((index, [round(row["sum"], 2), round(row["sum"], 2), round(row["sum"], 2)]))

        if index == 'Marketing':
            costList.append((index, [round(row["sum"], 2), round(row["sum"], 2), round(row["sum"], 2)]))

    print(costList)


if __name__ == "__main__":
    main()
