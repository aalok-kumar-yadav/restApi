from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StockSerializers, RepositorySerializers
from .models import Stock, Repository
from django.http import HttpResponse


class StockList(APIView):
    def get(self,request):
        st_obj=Stock.objects.all()
        ser = StockSerializers(st_obj, many=True)
        return Response(ser.data)

    def post(self):
        pass


class RepositoryList(APIView):
    def get(self, request):
        repo_obj = Repository.objects.all()
        serial = RepositorySerializers(repo_obj, many=True)
        return Response(serial.data)

    def post(self):
        pass


def home(request):
    return HttpResponse("<h3>This is Home Page: ")
