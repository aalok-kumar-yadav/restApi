# restApi
Rest API in Django Framework for getting stock data

First we need to create a Djnago Project and then created a webapp namely
companies.

after this we need to install djangorestframework using command line 
"pip install djangorestframework" and then include those in installed
app. 

we need to create database(if not exist) in model and migrate all changes 
database

after this we have to create a serializers class for all class of database
this actually provides the wrapping in a specific format like JSON instead 
of simple python objects.

creating view is necessary for response for specfic url patterns so create
a generic view instead of simple view.

To complete all steps when we run a url in localhost we get JSON Fomat data
in browser.







