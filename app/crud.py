from sqlalchemy.orm import Session

from . import models, schemas


def create_employee(
    db: Session,
    employee: schemas.EmployeeCreate
):
    db_employee = models.Employee(
        name=employee.name,
        email=employee.email,
        department=employee.department,
        position=employee.position
    )

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee


def get_employees(
    db: Session,
    skip: int = 0,
    limit: int = 100
):
    return (
        db.query(models.Employee)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_employee(
    db: Session,
    employee_id: int
):
    return (
        db.query(models.Employee)
        .filter(models.Employee.id == employee_id)
        .first()
    )


def update_employee(
    db: Session,
    employee_id: int,
    employee: schemas.EmployeeCreate
):
    db_employee = get_employee(db, employee_id)

    if not db_employee:
        return None

    db_employee.name = employee.name
    db_employee.email = employee.email
    db_employee.department = employee.department
    db_employee.position = employee.position

    db.commit()
    db.refresh(db_employee)

    return db_employee


def delete_employee(
    db: Session,
    employee_id: int
):
    db_employee = get_employee(db, employee_id)

    if not db_employee:
        return None

    db.delete(db_employee)
    db.commit()

    return db_employee
