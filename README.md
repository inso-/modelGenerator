# modelGenerator

Tired to loose time to create all your model object class, stop loosing your time !  
Generate it directly from your database in only 2 minutes !  

Source (Type of Database/file) supported: 

- mysql
- postgresql
- sqlite3
- oracle
- JSON
- RAML
- JAPI (JSON API DESC)

Destination (Language of Generated Object) avalaible: 

- Objective-C (.h/.m)
Optional generation of API framework with AFNetworking from RAML file
- Swift (.swift)
With init from Dictionary keyObjectMapping
- Java (.java)  
With Json Constructor/Serializer Getter an Setter for each model's object attributes
- C++ (.cpp/.hh)
- C# (.cs)
- NodeJS sequelize (.js)
- Python Django (.py)

Dependencies:  
- python
- virtualenv

OS Supported:  
- unix(osx)/linux

Easy to Use: 

- ./install  
  To initialise modelCreator and install dependencies (the project create and use a virtualenv, so nothing will be install outside of the project directory).
- ./configure  
  To configure your Source Database and Destination paramaters.
- ./run  
  To generate your file.
- ./uninstall  
  To uninstall all depencies and temporary output folder containing generated file (virtualenv)
  
