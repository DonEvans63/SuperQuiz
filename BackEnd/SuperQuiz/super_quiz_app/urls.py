from django.urls import path

from . import views

urlpatterns = [
    # path('questions/<int:question_id>/', views.question_detail, name="question_detail"),
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name='signup'),
    path('users/<username>/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/delete/', views.delete_profile, name='delete_profile'),
    path('random/', views.random_question, name='random_question'),
    # -----------
    path('start_quiz/', views.start_quiz, name='start_quiz'),
    # path('completed_quiz/', views.completed_quiz, name='completed_quiz'),
]

