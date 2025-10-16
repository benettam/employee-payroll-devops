from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory employee database (you can later connect MongoDB or SQLite)
employees = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add')
def add_employee_form():
    return render_template('add_employee.html')

@app.route('/add', methods=['POST'])
def add_employee():
    emp = {
        'id': len(employees) + 1,
        'name': request.form['name'],
        'designation': request.form['designation'],
        'salary': request.form['salary']
    }
    employees.append(emp)
    return redirect(url_for('view_employees'))

@app.route('/employees')
def view_employees():
    return render_template('view_employee.html', employees=employees)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
