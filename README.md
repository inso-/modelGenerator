# modelGenerator

Tired to loose time to create all your model object class, stop loosing your time !  
Generate it directly from your database in only 2 minutes !  

Source (Type of Database) supported: 

- mysql
- postgresql
- sqlite3
- oracle

Destination (Language of Generated Object) avalaible: 

- Objective-C (.h/.m)
- Swift (.swift)
- Java (.java)  
With Json Constructor/Serializer Getter an Setter for each model's object attributes
- C++ (.cpp/.hh)
- C# (.cs)

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
  
