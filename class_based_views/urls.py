from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.ReviewListApiView.as_view()),
    path('reviews/<int:id>/', views.ReviewUpdateDeleteApiView.as_view()),
    path('movie/', views.MovieListApiView.as_view()),
    path('movie/<int:id>/', views.MovieUpdateDeleteApiView.as_view()),
    path('director/', views.DirectorListApiView.as_view()),
    path('director/<int:id>/', views.DirectorUpdateDeleteApiView.as_view()),
    path('register/', views.RegisterApiView.as_view()),
    path('authorization/', views.AuthorizationApiView.as_view()),
]