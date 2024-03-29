from django.contrib import admin
from django.urls import path, include
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/test/', views.test),
    path('api/v1/director_list/', views.director_list_view),
    path('api/v1/director_list/<int:id>', views.director_detail_view),
    path('api/v1/movie_list/', views.movie_list_view),
    path('api/v1/movie_list/<int:id>', views.movie_detail_view),
    path('api/v1/review_list/', views.review_list_view),
    path('api/v1/review_list/<int:id>', views.review_detail_view),
    path('api/v1/login/', views.authorization),
    path('api/v1/register/', views.registration),
    path('api/v1/user/reviews/', views.user_reviews),
    path('api/v1/cbv/', include("class_based_views.urls")),
]
