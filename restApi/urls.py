from django.contrib import admin
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from companies import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^stock$', views.StockList.as_view()),
    url(r'^project$', views.ProjectList.as_view()),
    url(r'^employee$', views.EmployeeList.as_view()),
    url(r'^department$', views.DepartmentList.as_view()),
    url(r'^$', views.home)
]

urlpatterns = format_suffix_patterns(urlpatterns)
