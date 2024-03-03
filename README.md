# SuperQuiz
![Alt text](<Screenshot 2024-02-28 at 8.11.46 PM.png>)

## What is it?

This Django app allows users to test their knowledge on randomized trivia questions.

Super Quiz allows users to:
* Create an account.
* Select the quiz difficulty.
* See which question they answered correctly or incorrecly as they go through the quiz.

# Usage

To use this template to start your own project:

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip3 install django
    
And then run the `django-admin.py` command to start the new project:

    $ django-admin.py startproject \
      --template=https://github.com/nikola-k/django-template/zipball/master \
      --extension=py,md \
      <project_name>

### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $ pip3 install django
    
And then:

    $ python3 -m django startproject \
      --template=https://github.com/nikola-k/django-template/zipball/master \
      --extension=py,md \
      <project_name>
      
      
After that just install the local dependencies, run migrations, and start the server.


# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/USERNAME/{{ project_name }}.git
    $ cd {{ project_name }}
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver

## Navigating The Project
### Data Models
#### Entity Relationship Diagram
![ERD](![Alt text](<Screenshot 2024-02-28 at 7.21.02 PM.png>))

#### User Model
- **Description:** This model is used to store user information.
- **Attributes:**
  - **id:** Automatically generated.
  - **username:** Any username selected by the user.
  - **password:** User's password
  - **datecreated:** Automatically generated.
  

#### Quiz Model
- **Description:** This model is used to store quiz information.
- **Attributes:**
  - **id:** Automatically generated.
  - **title:** Tracks which quiz the user selected.


#### Question Model
- **Description:** This model is used to generate the questions for the quiz.
- **Attributes:**
  - **id:** Automatically generated.
  - **text:** Question text.
  

#### Choice Model
- **Description:** This model is used to generate the choices for each question.
- **Attributes:**
  - **id:** Automatically generated.
  - **text:** Choice text.
  - **question_id:** Tracks the choice associated to a given question.
  - **is_correct:** Tracks if the choice selected by the user is correct or not.


### Routes
#### Users
- POST - /new Create a user
- GET - /:id - View a single user
- PUT - - edit/:id - Edit user account
- DELETE - delete/:id - Delete user account

#### Quiz
- GET - /:id - View a single quiz

#### Questions
- GET - /:id - View a single question


#### Templates
![Alt text](<Screenshot 2024-02-28 at 8.11.46 PM.png>)
![Alt text](<Screenshot 2024-02-28 at 8.00.40 PM.png>)
![Alt text](<Screenshot 2024-02-28 at 8.16.32 PM.png>)

#### Stretch Goals
![Alt text](<Screenshot 2024-02-28 at 7.47.10 PM.png>)