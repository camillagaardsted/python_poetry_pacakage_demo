# python_poetry_pacakage_demo


create virtual environment with poetry installed
activate the environment


# create the package files
poetry new mypackage-demo


# add a version file and some custom files 
# import the files in __init__.py

# increment minor version number for the project with
poetry version minor

# add an include section if you need further files in the package 

# stand where the toml file is 
poetry build 