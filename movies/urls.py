
from django.urls import path
from . import views

app_name='movies'

urlpatterns=[
    path('', views.test,name='test'),
    path(r'<int:movie_id>', views.detail, name='detail')
]