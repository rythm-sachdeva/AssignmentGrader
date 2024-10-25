# School Management System

This project is a school management system built with Flask (or another framework) that provides different functionalities for three user roles: Principal, Students, and Teachers. The database includes a predefined set of users and allows for role-based functionalities, including managing users, assignments, and grading workflows.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
  - [Principal](#principal)
  - [Student](#student)
  - [Teacher](#teacher)
- [Setup](#setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Overview
This application has five core resources:
1. **Users** - General users of the application
2. **Principal** - Has administrative privileges
3. **Students** - Can create, edit, and submit assignments
4. **Teachers** - Can review and grade assignments
5. **Assignments** - Assignments created by students and graded by teachers

The database includes sample data with:
- 1 Principal
- 2 Students
- 2 Teachers

Each user role has specific access and functionalities for interacting with the resources.

## Features
### Principal
- **View All Teachers**: A principal can access the list of all teachers.
- **View All Assignments**: A principal can view all assignments that have been submitted or graded by teachers.
- **Re-grade Assignments**: The principal can re-grade assignments that have already been graded by teachers.

### Student
- **Create/Edit Draft Assignment**: Students can create and modify assignments in draft mode.
- **View Created Assignments**: Students can list all assignments they have created.
- **Submit Assignment**: Students can submit a draft assignment to a teacher.

### Teacher
- **View Submitted Assignments**: Teachers can view all assignments submitted to them by students.
- **Grade Assignment**: Teachers can grade assignments submitted to them by students.

## Setup
---
### Clone The Repository
   ```bash
   git clone https://github.com/rythm-sachdeva/AssignmentGrader.git
   cd school-management-system
   ```
### Install requirements

```
virtualenv env --python=python3.8
source env/bin/activate
pip install -r requirements.txt
```
### Reset DB

```
export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/
```
### Start Server

```
bash run.sh
```

## Usage
Each user type has different access capabilities and functions. Use the appropriate login credentials to test each user role's functionalities.

## API Endpoints
Here's a brief list of API endpoints with functionality:

### Principal Endpoints
- **GET /api/principal/teachers**: View all teachers.
- **GET /api/principal/assignments**: View all assignments submitted or graded.
- **PUT /api/principal/assignments/<assignment_id>/regrade**: Re-grade an assignment.

### Student Endpoints
- **POST /api/student/assignments**: Create a new draft assignment.
- **PUT /api/student/assignments/<assignment_id>**: Edit a draft assignment.
- **GET /api/student/assignments**: List all created assignments.
- **POST /api/student/assignments/<assignment_id>/submit**: Submit a draft assignment to a teacher.

### Teacher Endpoints
- **GET /api/teacher/assignments**: List assignments submitted to the teacher.
- **PUT /api/teacher/assignments/<assignment_id>/grade**: Grade an assignment submitted by a student.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any new ideas or improvements.

---



