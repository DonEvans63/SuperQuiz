from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Question, Choice
from django.utils import timezone
from django.views.generic import DetailView

#imports for authentication
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




def question_detail(request, question_id):
    """
    pull question from DB
    need model form
    if user submitted answer
        process request
        verify if answer is correct
        update total on quiz accordingly
        save quiz 
    else show the blank form
    render template
    """
    if request.method == 'POST':
        try:
            question = Question.objects.get(pk=question_id)
            choice_id = request.POST.get('choice_id');
            ch = Choice.objects.get(pk=choice_id)
        except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
             return render(request, 'quiz/question_detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
            }) 
        return render(request, "quiz/question_detail.html", {"question": question, "isCorrect": ch.is_correct})
    else:
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            raise Http404("Question does not exist")
        return render(request, "quiz/question_detail.html", {"question": question})


def home(request):
    return render(request, "home.html")

def login(request):
    """ login to app"""
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    print(f'{u} - account is active')
                    return HttpResponseRedirect('/home')
                else:
                    print(f'{u} - account has been disabled')
                    return HttpResponseRedirect('/login')
            else:
                print('The username and/or password is none')
                return HttpResponseRedirect('/login')
        else:
            print('The username and/or password is not valid')
            return HttpResponseRedirect('/login')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', { 'form': form })
    
def logout(request):
    return HttpResponseRedirect('/login')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')
        else:
            return render(request, 'signup.html', { 'form': form })
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', { 'form': form })