from django.urls import path

from . import views

urlpatterns = [
    path('questions/<int:question_id>/', views.question_detail, name="question_detail"),
    path('home/', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name='signup'),
    path('users/<username>/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),

]