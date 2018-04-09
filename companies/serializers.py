from rest_framework import serializers
from .models import Stock, Projects, Employee, Dependent,Department, Dependent_of, Workson, Workfor, Controls


class  EmployeeSerializers(serializers.ModelSerializer):

    class Meta:
        model =  Employee
        fields = '__all__'


class DependentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dependent
        fields = '__all__'


class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class Dependent_ofSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dependent_of
        fields = '__all__'


class StockSerializers(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = '__all__'


class WorksonSerializers(serializers.ModelSerializer):

    class Meta:
        model = Workson
        fields = '__all__'


class WorkforSerializers(serializers.ModelSerializer):

    class Meta:
        model = Workfor
        fields = '__all__'

class ControlsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Controls
        fields = '__all__'

class RepositorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


