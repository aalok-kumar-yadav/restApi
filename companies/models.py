from django.db import models


class Department(models.Model):         # Department class defined
    dep_num = models.IntegerField()
    dep_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.dep_name


class Employee(models.Model):           # Employee class defined
    dnum = models.ForeignKey(Department, on_delete=models.CASCADE)
    ssn = models.IntegerField()
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    sex = models.CharField(max_length=1)
    address = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
        return self.fname


class Projects(models.Model):               # Project class defined
    pro_num = models.IntegerField
    pro_name = models.CharField(max_length=30)
    pro_location = models.CharField(max_length=30)

    def __str__(self):
        return self.pro_name


class Dependent(models.Model):              # Dependent class defined
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    birth_date = models.DateField(max_length=8)
    sex = models.CharField(max_length=1)
    relationship = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Stock(models.Model):          # stock class defined

    ticker_name = models.CharField(max_length=10)
    open = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()

    def __str__(self):
        return self.ticker_name


class Workfor(models.Model):                # Workfor class defined
    e_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    dep_id = models.ForeignKey(Department, on_delete=models.CASCADE)




class Workson(models.Model):                  # Workon class defined
    em_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    proj_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    hour = models.IntegerField()




class Controls(models.Model):                 # Controls class defined
    dep_id = dep_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    proj_id = models.ForeignKey(Projects, on_delete=models.CASCADE)




class Dependent_of(models.Model):               # Dependent class defined
    ep_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    dependent_name = models.ForeignKey(Dependent, on_delete=models.CASCADE)


