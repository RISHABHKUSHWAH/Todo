from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.create,name='create'),
    path('currenttodo/',views.Currenttodo,name='currenttodo'),
    path('update/<int:pk>',views.Update,name='update'),
    path('complete/<int:pk>',views.Complete,name='complete'),
    path('delete/<int:pk>',views.Delete,name='delete'), 
    path('all_complete/',views.All_complete,name='all_complete'),
    ]