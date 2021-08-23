=========================
Double Eye Employee Tasks
=========================

To-Do is an application where one can perform CRUD (Create, Read, Update, Delete) operations
for employees/users and their tasks.

Newly created users/employees and tasks are stored to a local database (SQLite).
This application has been designed to work through the CLI (Command line Interface).
See 'Run Application' section.


.. contents::
   :local:


Develop Application
===================

Activate Virtual Environment:
 .. code-block::
    
    pipenv shell 


Install dependencies:

 .. code-block::

    pipenv install --dev -e .


Run Application
===============

 .. code-block::

    to_do --help
