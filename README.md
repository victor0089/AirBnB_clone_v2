# AirBnB_clone
# Team Project By Victor Adly & Maryam Amrani
 * One of the significant undertakings within the ALX Software Engineering program is the first project related to web development.
The console functions as a command interpreter, akin to a standard Python interactive shell or REPL (Read-Eval-Print Loop). It provides us with the means to execute commands and engage with the web application via a command-line interface, typically within a terminal. Through this command interpreter, our goal is to efficiently manage the objects within our project. This encompasses various tasks, such as creating new objects (e.g., users or places), retrieving objects from storage (like files or databases), performing operations on objects, such as counting and computing statistics, updating object attributes, and when necessary, deleting objects. Furthermore, the console serves as a valuable tool for debugging and identifying logic errors, as it enables us to experiment with the web application using different inputs and commands.

 * In a nutshell, "the console"refers to a command-line interface that facilitates interaction with our web application's objects by executing commands and receiving corresponding outputs.

 * In our Python-based Airbnb web application, we adhere to the principle that everything is treated as an object, indicating that they are instances of specific classes. This approach ensures a structured representation of various entities within our application. For instance, in our database:
 * 1-An instance (object) of the "User" class represents an individual who has registered an account on the web app. It encompasses essential information such as name, email, and password.

 * 2-Similarly, an instance (object) of the "State" class signifies a state or province, while an instance of the "City" class denotes a city within that state.

 * 3-Additionally, we have instances of the "Place" class, which represent temporary accommodations available for booking on the web app. These instances contain pertinent details like the room or suite's name, description, location, price, and availability dates.

 * This object-oriented approach ensures a structured and organized representation of data within our Airbnb web application.

 * In this project, we encountered approximately 18 distinct tasks to solve. The advantage of these tasks lies in their ability to dissect the overall project into more manageable segments, allowing us to focus on each task individually.

 * Furthermore, as these tasks come with clear prompts to guide us , their execution often becomes relatively straightforward.
This project have to be  ended in 7 days and demanded a team consisting of two members.
We began with a thorough review of the concept pages and extensive brainstorming sessions to formulate our project approach. Ultimately, we made the decision to convene daily for as many hours as possible, dedicating our available time and effort to the project.

 * The initial tasks we tackled were relatively straightforward. However, there were some among them for which we lacked prior knowledge, prompting us to search online for resources that could provide us with explanations. I distinctly recall one such task: "How to utilize the UUID module in Python."
<img align="center" alt="hbnb" width="850" src="https://github.com/victor0089/AirBnB_clone/blob/main/hbnb.png">
<img align="center" alt="hbnb" width="850" src="https://github.com/victor0089/AirBnB_clone/blob/main/hbnb2.png">
## 0x00.Table of contents

* [0x01 Introduction](#0x01-Introduction)
* [0x02 Environment](#0x02-Environment)
* [0x03 Installation](#0x03-Installation)
* [0x04 Testing](#0x04-Testing)
* [0x05 Usage](#0x05-Usage)
* [0x06 Authors](#0x06-Authors)

## 0x01 Introduction

Team project to build a clone of [AirBnB](https://www.airbnb.com/).

The console is a command interpreter to manage objects abstraction between objects and how they are stored.

To see the fundamental background of the project visit the [Wiki](https://github.com/ralexrivero/AirBnB_clone/wiki).

The console will perform the following tasks:

* create a new object
* retrive an object from a file
* do operations on objects
* destroy an object

### Storage

All the classes are handled by the `Storage` engine in the `FileStorage` Class.

## 0x02 Environment

<!-- ubuntu -->
<a href="https://ubuntu.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A" alt="Suite CRM"></a> <!-- bash --> <a href="https://www.gnu.org/software/bash/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GNU%20Bash&color=4EAA25&logo=GNU%20Bash&logoColor=4EAA25&labelColor=2F333A" alt="terminal"></a> <!-- python--> <a href="https://www.python.org" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Python&color=FFD43B&logo=python&logoColor=3776AB&labelColor=2F333A" alt="python"></a> </a> <!-- vim --> <a href="https://www.vim.org/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Vim&color=019733&logo=Vim&logoColor=019733&labelColor=2F333A" alt="Suite CRM"></a> <!-- vs code --> <a href="https://code.visualstudio.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Visual%20Studio%20Code&color=5C2D91&logo=Visual%20Studio%20Code&logoColor=5C2D91&labelColor=2F333A" alt="Suite CRM"></a> </a><!-- git --> <a href="https://git-scm.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Git&color=F05032&logo=Git&logoColor=F05032&labelColor=2F333A" alt="git distributed version control system"></a> <!-- github --> <a href="https://github.com" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="Github"></a>
 <!-- Style guidelines -->
* Style guidelines:
  * [pycodestyle (version 2.7.*)](https://pypi.org/project/pycodestyle/)
  * [PEP8](https://pep8.org/)

All the development and testing was runned over an operating system Ubuntu 20.04 LTS using programming language Python 3.8.3. The editors used were VIM 8.1.2269, VSCode 1.6.1 and Atom 1.58.0 . Control version using Git 2.25.1.

## 0x03 Installation

```bash
git clone https://github.com/victor0089/AirBnB_clone.git
```

change to the `AirBnb` directory and run the command:

```bash
 ./console.py
```

### Execution

In interactive mode

```bash
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

in Non-interactive mode

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## 0x04 Testing

All the test are defined in the `tests` folder.

### Documentation

* Modules:

```python
python3 -c 'print(__import__("my_module").__doc__)'
```

* Classes:

```python
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
```

* Functions (inside and outside a class):

```python
python3 -c 'print(__import__("my_module").my_function.__doc__)'
```

and

```python
python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
```

### Python Unit Tests

* unittest module
* File extension ``` .py ```
* Files and folders star with ```test_```
* Organization:for ```models/base.py```, unit tests in: ```tests/test_models/test_base.py```
* Execution command: ```python3 -m unittest discover tests```
* or: ```python3 -m unittest tests/test_models/test_base.py```

### run test in interactive mode

```bash
echo "python3 -m unittest discover tests" | bash
```

### run test in non-interactive mode

To run the tests in non-interactive mode, and discover all the test, you can use the command:

```bash
python3 -m unittest discover tests
```


## 0x05 Usage

* Start the console in interactive mode:

```bash
$ ./console.py
(hbnb)
```

* Use help to see the available commands:

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

* Quit the console:

```bash
(hbnb) quit
$
```

### Commands

> The commands are displayed in the following format *Command / usage / example with output*

* Create

> *Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file file.json.*

```bash
create <class>

```

```bash
(hbnb) create BaseModel
6cfb47c4-a434-4da7-ac03-2122624c3762
(hbnb)
```

* Show

```bash
show <class> <id>
```

```bash
(hbnb) show BaseModel 6cfb47c4-a434-4da7-ac03-2122624c3762
[BaseModel] (a) [BaseModel] (6cfb47c4-a434-4da7-ac03-2122624c3762) {'id': '6cfb47c4-a434-4da7-ac03-2122624c3762', 'created_at': datetime.datetime(2021, 11, 14, 3, 28, 45, 571360), 'updated_at': datetime.datetime(2021, 11, 14, 3, 28, 45, 571389)}
(hbnb)
```

* Destroy

> *Deletes an instance of a given class with a given ID.*
> *Update the file.json*

```bash
(hbnb) create User
0c56g2b8-7ffa-42b7-8709-d9d54b76j472
(hbnb) destroy User 0c56g2b8-7ffa-42b7-8709-d9d54b76j472
(hbnb) show User 0c56g2b8-7ffa-42b7-8709-d9d54b76j472
** no instance found **
(hbnb)
```

* all

> *Prints all string representation of all instances of a given class.*
> *If no class is passed, all classes are printed.*

```bash
(hbnb) create BaseModel
e45ddfg9-eb80-6558-99a9-226d4f08s329
(hbnb) all BaseModel
["[BaseModel] (4c8f7ebc-257f-4ed1-b26b-e7aacr457697) [BaseModel] (4c8f7ebc-257f-4ed1-b26b-e7aacr457697) {'id': '4c8f7ebc-257f-4ed1-b26b-e7aace457697', 'created_at': datetime.datetime(2021, 11, 13, 22, 19, 19, 447155), 'updated_at': datetime.datetime(2021, 11, 13, 22, 19, 19, 557257), 'name': 'My First Model', 'my_number': 45}"]
["[BaseMode
```

* count

> *Prints the number of instances of a given class.*

```bash
(hbnb) create City
4e01c33e-2564-42c2-b61c-47e512898dad
(hbnb) create City
e952b772-80a5-41e9-b728-6bc2dc5c21f4
(hbnb) count City
1
(hbnb)
```

* update

> *Updates an instance based on the class name, id, and kwargs passed.*
> *Update the file.json*
```
## Authors
<details>
    <summary>Victor Adly</summary>
    <summary>Maryam Amrani</summary>
    <ul>
    <li><a href="https://www.github.com/victor0089">Github</a></li>
    <li><a href="mailto:victor.mecdoors@gmail.com">e-mail</a></li>
    <li><a href="https://www.github.com/AMaaryam">Github</a></li>
    <li><a href="mailto:a.maaryam@gmail.com">e-mail</a></li>
    </ul>
</details>

## How to add Author file
`Bash script for generating the list of authors in git repo`
```
#!/bin/sh

git shortlog -se \
  | perl -spe 's/^\s+\d+\s+//' \
  | sed -e '/^CommitSyncScript.*$/d' \
  > AUTHORS
  ```
