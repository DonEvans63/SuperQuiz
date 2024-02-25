from django.urls import path

from . import views

app_name = "super_quiz_app"

urlpatterns = [
    path("", views.home, name="home"),
    # path("super_quiz_app", IndexView.as_view, name="index"),
    path('questions/<int:question_id>/', views.question_detail, name="question_detail"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name='signup')
]
