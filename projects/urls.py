from django.urls import path
from . import views

urlpatterns = [
    path('',views.projects,name='projects'), # leaving the url path makes it the default page in this case when u open http://127.0.0.1:8000/ it opens projects page
    path('projectpage/<str:pk>',views.project,name='project')
]