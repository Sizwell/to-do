=========================
Double Eye Employee Tasks
=========================

To-Do is an application where one can perform CRUD (Create, Read, Update, Delete) operations
for employees/users and their tasks.

Newly created users/employees and tasks are stored to a Postgres database.
A user can be assigned to multiple tasks or no tasks at all. 
A task can be created and not be assigned to any user but it can at a later stage be assigned to a user.
Users can update the contents of existing tasks and also change the tasks status of 'done' to true or false.
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
