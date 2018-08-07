#import os
from flask import Flask, redirect, url_for, request, render_template, json
import story1 as s1
import pandas as pd
import xlrd
import numpy as np
app = Flask(__name__)

# Assign spreadsheet filename to `file`
file = 'hardware.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('Page 1')

@app.route('/')
def todo():
    # Render default page template
    listOfDept = s1.listOfAllDepartments(df1)
    return render_template('listOfAllDepartments.html', items=listOfDept)


@app.route('/listOfAppsByDept', methods=['GET'])
def listOfAppsByDept():
    listOfApps = s1.listOfAllAppByDepartments(df1)
    return render_template('listOfAppsByDept.html', items=listOfApps)


# @app.route('/new', methods=['POST'])
# def new():
#
#     item_doc = {
#         'name': request.form['name'],
#         'description': request.form['description']
#     }
#     # Save items to database
#     db.todos.insert_one(item_doc)
#
#     return redirect(url_for('todo'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)