<center> <h1>AirBNB - The Console</h1> </center>
<center> <h4>Holberton AirBnB Clone project</h4> </center>

---------------------------------------------------------------------------------------------------------
This is the first portion of a project to build a clone of the AirBnB website. The first goal of this project is to create a program that serializes and deserializes objects into json files, and reloads them on startup for use between sessions, or in other words making the data persist between sessions.

The second goal of the project is to build a console to manage all this stored data. The console is made to update, delete, and create new instances of any class of data. It also keeps track of when the objects it has made were created, and updated.

* This is a TEAM Project done during **Full Stack Software Engineering studies** at **ALX School**. It aims to learn about building your first full web application: the AirBnB clone**.

## Requirements
* Allowed editors: vi, vim, emacs
* All files would be interpreted/compiled on ubuntu 20.04 LTS using python3 (version 3.8.5)
* All files must end in a New Line
* Team Member: Lawrence Maduabuchi & Abdullahi Ngui.
* Date: August 7th 2023
* The first line of all your files should be exactly #!/usr/bin/python3
* Your code should use the pycodestyle (version 2.8.*)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')

## Python UnitTests
* All your test files should be inside a folder tests
* You have to use the unittest module
* All your test files should be python files (extension: .py)
* All your test files and folders should start by test_
* Your file organization in the tests folder should be the same as your project
* All your tests should be executed by using this command: python3 -m unittest discover tests

<center> <h1>General Use</h1> </center>

----------------------------------------------------------------------------------------
1. First clone this repository.
2. Once the repository is cloned locate the "console.py" file and run it as follows
```
/AirBnB_clone$ ./console.py
```
3. When this command is run the following prompt should appear:
```
(hbnb)
```
4. This prompt designates you are in the "HBnB" console, there are a variety of commands available once the console program is run.
##### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID
    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)

    - It is possible to call <class_name>.<command>(arguments) as well
----

## Files
All of the following files are programs written in Python:

| Filename | Description |
| -------- | ----------- |
| ` 0. README, AUTHORS` | README.md, AUTHORS.|
| ` 1. Be pycodestyle compliant!` | Prints a char.|
| ` 2. Unittests` | tests|
| ` 3. BaseModel` | models/base_model.py, models/__init__.py, tests/|
| ` 4. Create BaseModel from dictionary` | models/base_model.py, tests/.|
| ` 5. Store first object` | models/engine/file_storage.py, models/engine/__init__.py, models/__init__.py, models/base_model.py, tests/ |
| ` 6. Console 0.0.1` | console.py |
| ` 7. Console 0.0.1` | Update your command interpreter (console.py) to have these commands:|
| ` 8. First User` | Write a class User that inherits from BaseModel: models/user.py, models/engine/file_storage.py, console | 
|` 9. More classes!` | Write all those classes that inherit from BaseModel: |
| ` 10. Console 1.0` | Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review |
 | ` 11. All instances by class name` | Update your command interpreter (console.py) to retrieve all instances of a class by using: <class name>.all(). |
| ` 12. Count instances` | Update your command interpreter (console.py) to retrieve the number of instances of a class: <class name>.count(). |
| ` 13. Show` | Update your command interpreter (console.py) to retrieve an instance based on its ID: <class name>.show(<id>). |
| ` 14. Destroy` | Update your command interpreter (console.py) to destroy an instance based on his ID: <class name>.destroy(<id>). |
| ` 15. Update` | Update your command interpreter (console.py) to update an instance based on his ID: <class name>.update(<id>, <attribute value>).
|'16. Update from dictionary'| Update your command interpreter (console.py) to update an instance based on his ID with a dictionary: <class name>.update(<id>, <dictionary representation>).|
|'17. Unittests for the Console!| Write all unittests for console.py, all features! For testing the console, you should “intercept” STDOUT of it, we highly recommend you to use:with patch('sys.stdout', new=StringIO()) as f:
    HBNBCommand().onecmd("help show")|
