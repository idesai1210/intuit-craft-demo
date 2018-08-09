import pandas as pd
import numpy as np
import logging
import datetime
from multiprocessing import Pool
from functools import partial

logging.basicConfig(filename='Story2.log', format='%(levelname)s:%(asctime)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

def valuation_formula(cpu,ram,df_prices):
    l = df_prices[(df_prices.CPU <= cpu) | (df_prices['RAM (MB)'] <= ram)].iloc[-1]
    return float(l['Price/Hr'][1:])

def mulitprocessFunc(hardware, prices):
    hardware['Price'] = hardware.apply(lambda row: valuation_formula(row['CPU cores'], row['RAM (MB)'], prices), axis=1)
    return hardware

def Estimate(df_hardware, df_prices):
    # Load a sheet into a DataFrame by name: df_hardware
    logging.info(1)
    logging.info(datetime.datetime.now())

    #df_hardware['Price'] = df_hardware.apply(lambda row: valuation_formula(row['CPU cores'], row['RAM (MB)'], df_prices), axis=1)
    df_hardwareArray = np.array_split(df_hardware, 4)

    pool = Pool(processes=4)
    ans = pool.map(partial(mulitprocessFunc, prices=df_prices), df_hardwareArray)
    df_hardware = pd.concat(ans)

    logging.info(2)
    logging.info(datetime.datetime.now())

    logging.info(3)
    logging.info(datetime.datetime.now())


    try:
        # Join Dataframes on the primary key index

        # Group By Department

        groupByDept = df_hardware.groupby('Group')
        # Aggregate to calculate the sum
        rs = groupByDept['Price'].agg([np.sum])
        logging.info("Concatenation Successful")
    except Exception as e:
        logging.error("Error in concatenating two dataframes")
        logging.error(repr(e))
    # print(type(rs))
    # Create JSON String to feed to web app
    logging.info(4)
    logging.info(datetime.datetime.now())

    costList = []
    try:
        for index, row in rs.iterrows():
            row["sum"] = row["sum"]*24*7*365
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

    logging.info(5)
    logging.info(datetime.datetime.now())

    return costList
