from django.contrib import admin
from .models import Stock, Projects, Dependent_of, Department, Dependent, Employee, Workson,Workfor, Controls

# Register your models here.
admin.site.register(Stock)
admin.site.register(Projects)
admin.site.register(Dependent)
admin.site.register(Dependent_of)
admin.site.register(Department)
admin.site.register(Controls)
admin.site.register(Employee)
admin.site.register(Workfor)
admin.site.register(Workson)




