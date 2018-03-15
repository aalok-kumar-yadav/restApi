from rest_framework import serializers
from .models import Stock, Repository


class StockSerializers(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = '__all__'


class RepositorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = '__all__'


