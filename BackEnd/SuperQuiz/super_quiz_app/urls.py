from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('questions/<int:question_id>/', views.question_detail, name="question_detail"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name='signup')
]
