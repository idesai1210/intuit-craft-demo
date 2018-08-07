import pandas as pd
import xlrd
import numpy as np


def Estimate(d, d2):

    # Load a sheet into a DataFrame by name: df1
    df1 = d

    df2 = d2

    # print(df1)
    # print(df2)

    my_df = {}
    my_df['Type'] = list()
    my_df['Price/Hr'] = list()
    my_df['Price'] = list()

    for index, row in df1.iterrows():
        # print(row["CPU cores"], row["RAM (MB)"])
        # print(df2.loc[(df2['CPU'] <= row["CPU cores"]) | (df2["RAM (MB)"] <= row["RAM (MB)"])].iloc[-1])
        l = df2.loc[(df2['CPU'] <= row["CPU cores"]) | (df2["RAM (MB)"] <= row["RAM (MB)"])].iloc[-1]
        # print(l['Type'])
        my_df['Type'].append(l['Type'])
        my_df['Price/Hr'].append(l['Price/Hr'])
        my_df['Price'].append(float(l['Price/Hr'][1:]) * 24 * 7 * 365)
        # print(d)

    my_df = pd.DataFrame(my_df)

    result = pd.concat([df1, my_df], axis=1, sort=False)

    group = result.groupby('Group')


    rs = group['Price'].agg([np.sum])

    # print(type(rs))
    costList = []
    for index, row in rs.iterrows():

        if index == 'Engineering':
            year1 = '${:,.2f}'.format(row["sum"])
            year2 = row["sum"] * 0.10 + row["sum"]
            year3 = year2 * 0.10 + year2
            year2 = '${:,.2f}'.format(year2)
            year3 = '${:,.2f}'.format(year3)
            costList.append({'Department': index, 'Year1': year1, 'Year2': year2, 'Year3': year3})
            #costList.append((index, [round(year1, 2), round(year2, 2), round(year3, 2)]))

        if index == 'Sales':
            year1 = '${:,.2f}'.format(row["sum"])
            year2 = row["sum"] - row["sum"] * 0.80
            year3 = year2 - year2
            year2 = '${:,.2f}'.format(year2)
            year3 = '${:,.2f}'.format(year3)
            costList.append({'Department': index, 'Year1': year1, 'Year2': year2, 'Year3': year3})
            #costList.append((index, [round(year1, 2), round(year2, 2), round(year3, 2)]))

        if index == 'Engineering Canada':
            year = '${:,.2f}'.format(row["sum"])
            costList.append({'Department': index, 'Year1': year, 'Year2': year, 'Year3': year})
            #costList.append((index, [round(row["sum"], 2), round(row["sum"], 2), round(row["sum"], 2)]))

        if index == 'Marketing':
            year = '${:,.2f}'.format(row["sum"])
            costList.append({'Department': index, 'Year1': year, 'Year2': year, 'Year3': year})
            #costList.append((index, [round(row["sum"], 2), round(row["sum"], 2), round(row["sum"], 2)]))

    return costList

