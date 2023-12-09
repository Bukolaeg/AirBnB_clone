# 0x00 AirBnB clone | The Console

<p align="center">
<img src="https://i.imgur.com/JOhaZ5m.png">
</p>

# 0x00 AirBnB clone - The console

In this directory you will find a implementation of a AirBnB clone.
In this first step is implemented the Console. Commands for create, update, destroy, show and manage diferent classes and attributes for the items that the app will be offer and for the users.

### The console ###
* create your data model
* manage (create, update, destroy, etc) objects via a console / command interpreter
* store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.
This abstraction will also allow you to change the type of storage easily without updating all of your codebase.
The console will be a tool to validate this storage engine

### Command interpreter ###

Our command interpreter looks like a mini shell and allow us manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

### Objectives of project ###

* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

### Content of Directory ###
* Models Folder: Classes of the project. BaseModel is the parent Class. The other classes (amenity, city, place, review, state, user) inherit from BaseModel and specify others attributes for itselfs.
* Tests Folder : Unittests for the project
* AUTHORS: Information about the authors
* console.py: Eceutable file for the console
* file.json: JSON file with all information of instances

---

## Table of Contents

- [Examples and Usage](#ExamplesandUsage)
- [Installation](#installation)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Team](#team)
- [Support](#support)
- [License](#license)



---

## Examples of Usage

### Execution ###
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
---
## Installation

* Clone the repository. git clone https://github.com/mecomonteshbtn/AirBnB_clone.git
* Open the /AirBnB_clone directory and execute console.py

### Setup

* You need Python interpreter.
IMPORTANT: The project was created in UBUNTU 14.04.3 LTS and Python 3.4.3.

---

## Documentation

<a href="https://intranet.hbtn.io/rltoken/Fx9HXIjmGzbmET4ylYg2Rw">`cmd module`</a><br>
<a href="https://intranet.hbtn.io/rltoken/jKl9WFpKA-fPt7_guv9_3Q">`packages`</a><br>
<a href="https://intranet.hbtn.io/rltoken/eaQ6aELbdqb0WmPddhD00g">`uuid module`</a><br>
<a href="https://intranet.hbtn.io/rltoken/_ySDcgtfrwLkTyQzYHTH0Q">`datetime`</a><br>
<a href="https://intranet.hbtn.io/rltoken/QX7d4D__xhOJIGIWZBp39g">`unittest module`</a><br>
<a href="https://intranet.hbtn.io/rltoken/jQd3P_uSO0FeU6jlN-z5mg">`args/kwargs`</a><br>
<a href="https://intranet.hbtn.io/rltoken/WPlydsqB0PG0uVcixemv9A">`Python test cheatsheet`</a><br>
---


## Authors

* **Jamiu Shomoye** - [github](https://github.com/jomojay) - [linkedin](https://www.linkedin.com/in/jamiu-shomoye-706b39a7?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app) - [X](https://x.com/jassmenn16?s=09)
* **Bukola Egberongbe** - [github](https://github.com/Bukolaeg)
