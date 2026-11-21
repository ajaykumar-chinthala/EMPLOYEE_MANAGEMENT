from fastapi import FastAPI,Request,Form
from fastapi.templating import Jinja2Templates
import sqlite3
from pydantic import BaseModel,Field
from fastapi.responses import RedirectResponse

templates=Jinja2Templates(
    directory="templates"
)

app=FastAPI()


class Employee(BaseModel):
   name:str=Field(max_length=50,min_length=3)
   gender:str
   image:str
   salary:int=Field(le=1000000,ge=1000)
   department:str
   experience:int=Field(le=30,ge=0)
   attendance:bool



def get_db_connection():
    connection=sqlite3.connect(
        "employees.db"
    )
    return connection
get_db_connection()



def create_table():
    connection=get_db_connection()
    cursor=connection.cursor()
    q="""CREATE TABLE IF NOT EXISTS EMPLOYEES(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    gender TEXT,
    image TEXT,
    salary INTEGER,
    department TEXT,
    experience INTEGER,
    attendance INTEGER
    )"""
    cursor.execute(q)
    connection.commit()
    connection.close()
create_table()



@app.get("/")
def home_page(req:Request):
    return templates.TemplateResponse(
        request=req,
        name="home.html",
        context={}  
    )



@app.get("/emp/add")
def add_student(req:Request):
    return templates.TemplateResponse(
        request=req,
        name="reg.html",
        context={}
    )

# @app.get("/employee")
# def all_employees(req:Request):
#     connection=get_db_connection()
#     cursor=connection.cursor()
#     q="SELECT * FROM EMPLOYEES"
#     cursor.execute(q)
#     emps=cursor.fetchall()
#     connection.commit()
#     connection.close()
#     return templates.TemplateResponse(
#         request=req,
#         name="Allemp.html",
#         context={"emps": emps}

#     )



@app.post("/emp/add")
def student_add(
    name:str=Form(),
    gender:str=Form(),
    image:str=Form(),
    salary:int=Form(),
    department:str=Form(),
    experience:int=Form(),
    attendance:int=Form()
    ):
    emp=Employee(
        name=name,
        gender=gender,
        image=image,
        salary=salary,
        department=department,
        experience=experience,
        
        attendance=attendance
    )
    print(name,gender,image,salary,department,experience,attendance)
    values=(emp.name,emp.gender,emp.image,emp.salary,emp.department,emp.experience,emp.attendance)
   
    connection=get_db_connection()
    cursor=connection.cursor()
    q="""
      INSERT INTO EMPLOYEES(name,gender,image,salary,department,experience,attendance) values(?,?,?,?,?,?,?)
    """
    cursor.execute(q,values)
    connection.commit()
    connection.close()
    return RedirectResponse(url="/employee",status_code=303)




@app.get("/employee/{emp_id}")
def get_single_emp(req:Request,emp_id:int):
    print(emp_id)
    connection=get_db_connection()
    cursor=connection.cursor()
    q="select * from EMPLOYEES WHERE id=?"
    cursor.execute(q,(emp_id,))
    sing_emp=cursor.fetchone()
    connection.close()
    return templates.TemplateResponse(
        request=req,
        name="singelemp.html",
        context={"emp":sing_emp}
    )

@app.post("/employee/{emp_id}")
def get_single_emp(emp_id:int):
    print(emp_id)
    connection=get_db_connection()
    cursor=connection.cursor()
    q="delete from EMPLOYEES WHERE id=?"
    cursor.execute(q,(emp_id,))
    connection.commit()
    connection.close()
    return RedirectResponse(url="/employee",status_code=303)

@app.get("/employee")
def get_gender_wise(req:Request,gend:str=None):
    connection=get_db_connection()
    cursor=connection.cursor()
    q="select * from EMPLOYEES"

    cursor.execute(q)
    emps=cursor.fetchall()
    connection.commit()
    connection.close()
    filterd=[]
    if gend is None:
        filterd=emps
    if gend is not None :
        for emp in emps:
            if emp[2]==gend:
                filterd.append(emp)
    
    return templates.TemplateResponse(
        request=req,
        name="Allemp.html",
        context={"emps":filterd}
    )

@app.get("/department")
def get_department(req:Request,dept:str=None):
    connection=get_db_connection()
    cursor=connection.cursor()
    q="select * from employees"
    cursor.execute(q)
    emps=cursor.fetchall()
    connection.commit()
    connection.close()
    filted=[]
    if dept is None:
        filted=emps
    else:
        for emp in emps:
            if emp[5]==dept:
                filted.append(emp)
    return templates.TemplateResponse(
        request=req,
        name="dept.html",
        context={"emps":filted}
    )


@app.get("/employee/update/{emp_id}")
def get_upd_form(req:Request,emp_id):
    connection=get_db_connection()
    cursor=connection.cursor()
    q="select * from employees where id=?"
    cursor=cursor.execute(q,(emp_id,))
    emp=cursor.fetchone()
    connection.close()
    return templates.TemplateResponse(
        request=req,
        name="update.html",
        context={
            "emp":emp
        }
    )


@app.post("/employee/update/{emp_id}")
def get_upd_form(emp_id,
    name:str=Form(),
    gender:str=Form(),
    image:str=Form(),
    salary:int=Form(),
    department:str=Form(),
    experience:int=Form(),
    attendance:int=Form()):
    emp_obj=Employee(
        name=name,
        gender=gender,
        image=image,
        salary=salary,
        department=department,
        experience=experience,
        attendance=attendance
    )
    values=(emp_obj.name,emp_obj.gender,emp_obj.image,emp_obj.salary,emp_obj.department,emp_obj.experience,emp_obj.attendance,emp_id)
    connection=get_db_connection()
    cursor=connection.cursor()
    q="update employees set name=?,gender=?,image=?,salary=?,department=?,experience=?,attendance=? where id=?"
    cursor=cursor.execute(q,values)
    connection.commit()
    connection.close()
    return RedirectResponse(url="/employee",status_code=303)