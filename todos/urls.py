from django.urls import path, include
from . import views

app_name = 'todos'

urlpatterns = [
    path('todos/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:id>/', views.detail, name="detail"),
    path('<int:id>/delete', views.delete, name='delete'),
    path('<int:id>/update', views.update, name='update'),
    path('<int:id>/comment_create', views.comment_create, name='comment_create'),
    path('<int:id1>/comment_delete/<int:id2>/',
         views.comment_delete, name='comment_delete'),
    path('search/', views.search, name="search"),
    path('<int:id>/like/', views.like, name="like"),
    path('<int:write_id>/comment_like/<int:comment_id>',
         views.comment_like, name="comment_like"),
]
