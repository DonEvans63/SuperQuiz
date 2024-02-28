from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('questions/<int:question_id>/', views.question_detail, name="question_detail"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name='signup'),
    path('users/<username>/', views.profile, name='profile'),
    # -----------
    path('start_quiz/', views.start_quiz, name='start_quiz'),
    path('random_question/', views.random_question, name='random_question'),
    path('random/', views.random_question, name='random_question'),
    # path('completed_quiz/', views.completed_quiz, name='completed_quiz'),
]
