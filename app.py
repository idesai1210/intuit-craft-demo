#import os
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def todo():
    items = ["Hi"]
    # Render default page template
    return render_template('index.html', items=items)


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
    app.run(host='34.230.75.72', debug=True)