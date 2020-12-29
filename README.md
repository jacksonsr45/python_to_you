# Python To You 
### This is simple project in Python with Flask 

# Command Line RunServer
    python manage.py runserver


# Command Line exec Tests

run behave:
    
    behave tests/behavior/features/ -D debug=True

run testes:
    
    python -m unittest discover tests/ -v

run tests with coverage:
    
    coverage run --source=python_to_you -m unittest discover tests/ -v

show report coverage: 
    
    coverage report

show report coverage html:
    
    coverage html

# WebPage from generate .gitignore
generate gitignore -> https://www.toptal.com/developers/gitignore


# Commands Line DB

    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    python manage.py db --help