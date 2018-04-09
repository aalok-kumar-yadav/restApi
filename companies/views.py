from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StockSerializers, RepositorySerializers, DepartmentSerializers, DependentSerializers
from .serializers import Dependent_ofSerializers, ControlsSerializers,EmployeeSerializers
from .serializers import WorkforSerializers,WorksonSerializers
from .models import Stock, Projects, Workson, Workfor, Employee, Department, Dependent_of, Dependent, Controls
from django.http import HttpResponse


class StockList(APIView):       # StockList view function
    def get(self,request):
        st_obj=Stock.objects.all()
        ser = StockSerializers(st_obj, many=True)

        return Response(ser.data)

    def post(self):
        pass


class ProjectList(APIView):         # ProjectList view function
    def get(self, request):
        repo_obj = Projects.objects.all()
        serial = RepositorySerializers(repo_obj, many=True)
        return Response(serial.data)

    def post(self):
        pass


class WorksonList(APIView):           # WorksonList view function
    def get(self,request):
        wrkon_obj=Workson.objects.all()
        ser = WorksonSerializers(wrkon_obj, many=True)
        return Response(ser.data)

    def post(self):
        pass


class WorksforList(APIView):           # WorksforList view function
    def get(self,request):
        wrk_obj = Workfor.objects.all()
        ser = WorkforSerializers(wrk_obj, many=True)
        return Response(ser.data)

    def post(self):
        pass


class EmployeeList(APIView):           # EmployeeList view function
    def get(self,request):
        emp_obj = Employee.objects.all()
        ser = EmployeeSerializers(emp_obj, many=True)
        return Response(ser.data)

    def post(self):
        pass


class DepartmentList(APIView):           # DepartmentList view function
    def get(self,request):
        dep_obj = Department.objects.all()
        ser = DepartmentSerializers(dep_obj, many=True)
        return Response(ser.data)

    def post(self):
        pass


class Dependent_ofList(APIView):           # Dependent_ofList view function
    def get(self,request):
        depe_obj = Dependent_of.objects.all()
        ser = Dependent_ofSerializers(depe_obj, many=True)
        return Response(ser.data)

    def post(self):
        pass


class DependentList(APIView):           # Dependent_ofList view function
    def get(self,request):
        de_obj = Dependent.objects.all()
        ser = DependentSerializers(de_obj, many=True)
        return Response(ser.data)

    def post(self):
        pass


class ControlsList(APIView):           # ControlsList view function
    def get(self,request):
        co_obj = Controls.objects.all()
        ser = ControlsSerializers(co_obj, many=True)
        return Response(ser.data)

    def post(self):
        pass

def home(request):
    return HttpResponse("<h3>This is Home Page: ")
