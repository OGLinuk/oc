# Open-source Collection Module

## Start collecting data for ML application!

## Use or sell the data you collect

<hr>

# Installation
1. Install [Python](https://www.python.org/ftp/python/3.6.3/python-3.6.3.exe) 3.X.X (Linux has python2 and 3 installed by default)
2. Install [Git](https://git-scm.com/download/win) (windows) | ```sudo apt install git -y``` (linux)
3. Clone the oc repo -  ```git clone https://github.com/oglinuk/oc.git```
4. Navigate to the directory that has oc
5. ```python run.py``` (windows) | ```python3 run.py``` (linux)

<hr>

# How to use
1. ```python run.py``` (windows) | ```python3 run.py``` (linux)
2. Input the number of entities to be queued/executed
3. Input a name (typically the abbreviation of the site + the data collected)
4. Input an entity type
5. Input an API string

<hr>

# Creating a new entity
1. Duplicate the temp directory - ../entities/temp
2. Rename the directory to the abbreviation of the target (ie coinmarketcap -> cmc)
3. In the ```__init__.py``` file change the name of the class to the abbreviation
4. Rename the ```tempJSONp.py``` file and implement the parse() method
    - Use the example entities (cmc, ccap, wci) when defining the parse() method
5. Add the new entity to the factory pattern class in managers/InitM/fp.py

<hr>

# Milestones
* Implement the ability to load pre-defined entities through csv file or another format
* Include more open-source entities
* Add API endpoint to the module to expose the mined/parsed data
* Change the entities to accept ```*args``` && ```**kwargs```
* Find way to update fp.py when a new entity is used/loaded from file
