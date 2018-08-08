#import os
from flask import Flask, render_template
import story1 as s1
import story2 as s2
import pandas as pd
app = Flask(__name__)

# Assign spreadsheet filename to `file`
file_hardware = 'hardware.xlsx'

# Load spreadsheet
xl_hardware = pd.ExcelFile(file_hardware)

# Print the sheet names

# Load a sheet into a DataFrame by name: df1
df_hardware = xl_hardware.parse('Page 1')

file_prices = 'prices.xlsx'
xl_prices = pd.ExcelFile(file_prices)
# print(xl1.sheet_names)
df_prices = xl_prices.parse('Sheet1')

@app.route('/')
def todo():
    # Render default page template
    listOfDept = s1.listOfAllDepartments(df_hardware)
    return render_template('listOfAllDepartments.html', items=listOfDept)


@app.route('/listOfAppsByDept', methods=['GET'])
def listOfAppsByDept():
    listOfApps = s1.listOfAllAppByDepartments(df_hardware)
    return render_template('listOfAppsByDept.html', items=listOfApps)

@app.route('/cpuMemByDept', methods=['GET'])
def cpuMemByDept():
    cpuMemByD = s1.noOfCPUMemByDep(df_hardware)
    return render_template('cpuMemByDept.html', items=cpuMemByD)


@app.route('/cpuMemByApp', methods=['GET'])
def cpuMemByApp():
    cpuMemByA = s1.noOfCPUMemByApp(df_hardware)
    return render_template('cpuMemByApp.html', items=cpuMemByA)


@app.route('/cpuMemByDC', methods=['GET'])
def cpuMemByDC():
    cpuMemBydc = s1.noOfCPUMemByDataCenters(df_hardware)
    return render_template('cpuMemByDC.html', items=cpuMemBydc)


@app.route('/cost', methods=['GET'])
def cost():
    costByDept = s2.Estimate(df_hardware, df_prices)
    return render_template('cost.html', items=costByDept)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)