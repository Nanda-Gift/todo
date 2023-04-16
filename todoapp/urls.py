
from django.urls import path,include
from todoapp import views

urlpatterns = [
    
    path('', views.todoviews,name='todoviews'),
    path('entry/', views.entry,name='entry'),
    path('email/', views.email,name='email'),
    path('delete/<int:id>', views.delete,name='delete'),
    path('search_club', views.search_club,name='search_club'),
]
