from django.db import models


class Stock(models.Model):

    ticker = models.CharField(max_length=10)
    open = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()

    def __str__(self):
        return self.ticker


class Repository(models.Model):
    repo_name = models.CharField(max_length=40)
    language = models.CharField(max_length=20)
    contributor = models.CharField(max_length=40)
    forks = models.IntegerField()

    def __str__(self):
        return self.repo_name

