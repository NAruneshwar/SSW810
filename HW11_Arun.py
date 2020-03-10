from prettytable import PrettyTable
from collections import defaultdict
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/hellorarey")

def hello():
    return "Hello "

@app.route("/pretty")
def _instructor_table_db():
    return (render_template('base.html'))
    conn = None
    try:
        conn = sqlite3.connect("C:\\sqlite\\810_startup.db")
        cur = conn.cursor()
        cur.execute("select i.cwid, i.Name, i.Dept, g.course, COUNT(g.StudentCWID) as stucnt from grades g,instructors i where i.CWID = g.InstructorCWID group by g.Course, g.InstructorCWID")
        rows = cur.fetchall()
        
    except FileNotFoundError as FE:
        print(f"Required file not found in the path {FE}")
    except Exception as E:
        print(f"please check {E}")
    return(rows.items())



app.run(debug=True)