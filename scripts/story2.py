import pandas as pd
import numpy as np
import logging

logging.basicConfig(filename='Story2.log', format='%(levelname)s:%(asctime)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)


def Estimate(original_df, prices_df):
    # Load a sheet into a DataFrame by name: df_hardware
    df_hardware = original_df

    df_prices = prices_df

    # print(df_hardware)
    # print(df_prices)
    # Create a temp Dataframe to Calculate prices
    pricesDict = {}
    pricesDict['Type'] = list()
    pricesDict['Price/Hr'] = list()
    pricesDict['Price'] = list()

    for index, row in df_hardware.iterrows():
        # print(row["CPU cores"], row["RAM (MB)"])
        # print(df_prices.loc[(df_prices['CPU'] <= row["CPU cores"]) | (df_prices["RAM (MB)"] <= row["RAM (MB)"])].iloc[-1])
        l = df_prices.loc[(df_prices['CPU'] <= row["CPU cores"]) | (df_prices["RAM (MB)"] <= row["RAM (MB)"])].iloc[-1]
        # print(l['Type'])
        pricesDict['Type'].append(l['Type'])
        pricesDict['Price/Hr'].append(l['Price/Hr'])
        pricesDict['Price'].append(float(l['Price/Hr'][1:]) * 24 * 7 * 365)
        # print(d)

    pricesDict = pd.DataFrame(pricesDict)

    try:
        # Join Dataframes on the primary key index
        result = pd.concat([df_hardware, pricesDict], axis=1, sort=False)

        # Group By Department
        groupByDept = result.groupby('Group')

        # Aggregate to calculate the sum
        rs = groupByDept['Price'].agg([np.sum])
        logging.info("Concatenation Successful")
    except Exception as e:
        logging.error("Error in concatenating two dataframes")
        logging.error(repr(e))
    # print(type(rs))
    # Create JSON String to feed to web app
    costList = []
    try:
        for index, row in rs.iterrows():

            if index == 'Engineering':
                year0 = row["sum"]
                year1 = year0 * 0.10 + year0
                year2 = year1 * 0.25 + year1
                year3 = year2 * 0.40 + year2
                year0 = '${:,.2f}'.format(year0)
                year1 = '${:,.2f}'.format(year1)
                year2 = '${:,.2f}'.format(year2)
                year3 = '${:,.2f}'.format(year3)
                costList.append({'Department': index, 'Year0': year0, 'Year1': year1, 'Year2': year2, 'Year3': year3})
                # costList.append((index, [round(year1, 2), round(year2, 2), round(year3, 2)]))

            if index == 'Sales':
                year0 = row["sum"]
                year1 = row["sum"] - row["sum"] * 0.80
                year2 = year1 - year1
                year3 = 0
                year0 = '${:,.2f}'.format(year0)
                year1 = '${:,.2f}'.format(year1)
                year2 = '${:,.2f}'.format(year2)
                year3 = '${:,.2f}'.format(year3)
                costList.append({'Department': index, 'Year0': year0, 'Year1': year1, 'Year2': year2, 'Year3': year3})
                # costList.append((index, [round(year1, 2), round(year2, 2), round(year3, 2)]))

            if index == 'Engineering Canada':
                year0 = row["sum"]
                year1 = year0 * 0.10 + year0
                year2 = year1 * 0.25 + year1
                year3 = year2 * 0.40 + year2
                year0 = '${:,.2f}'.format(year0)
                year1 = '${:,.2f}'.format(year1)
                year2 = '${:,.2f}'.format(year2)
                year3 = '${:,.2f}'.format(year3)
                costList.append({'Department': index, 'Year0': year0, 'Year1': year1, 'Year2': year2, 'Year3': year3})
                # costList.append((index, [round(row["sum"], 2), round(row["sum"], 2), round(row["sum"], 2)]))

            if index == 'Marketing':
                year = '${:,.2f}'.format(row["sum"])
                costList.append({'Department': index, 'Year0': year, 'Year1': year, 'Year2': year, 'Year3': year})
                # costList.append((index, [round(row["sum"], 2), round(row["sum"], 2), round(row["sum"], 2)]))
    except Exception as e:
        logging.error("The result set is empty")
        logging.error(repr(e))

    print(costList)

    return costList
