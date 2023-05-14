from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('dtl',views.DTL, name="DTL"),
    path('test/',views.test,name="test"),
    path('test/result',views.RESULT,name="result"),
]

