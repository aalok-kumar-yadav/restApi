# restApi

This project contains a company's database and we will retrieve all the useful and wanted 
data in **JSON** format.First we need to create a Djnago Project and then created a webapp
namely companies.

after this we need to install djangorestframework using command line -

``` bash
pip install djangorestframework
```
after installing include in the installed apps


we need to create database(if not exist) in model and migrate all changes 
database

# RDBMS TABLES

- Employee
- Department
- Projects
- Dependent
- Workson
- Worksfor
- Dependent_Of
- Controls


1. after this we have to create a serializers class for all class of database this actually
provides the wrapping in a specific format like **JSON** instead of simple python objects.



2. creating view is necessary for response for specfic url patterns so create a generic view
 simple view.


3. To complete all steps when we run a url in localhost we get **JSON** Fomat data in browser.


Here is the sample output of the retrived data of all Employee with their attibutes like name, address,
sex etc and this information we can easily send over the newtwork.


![alt text](https://i.imgur.com/7JdN4bW.png?1)



Here is the sample output of the retrived data of all Project with their attibutes like location,
project name etc and this information we can easily send over the newtwork in JSON format.


![alt text](https://i.imgur.com/W4rtpId.png?1)








