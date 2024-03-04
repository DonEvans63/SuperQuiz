
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from .forms import EditProfileForm
import random

from .models import Question

#imports for authentication
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login 

def generate_quiz(num_questions):
    total_questions = Question.objects.count()
    num_questions = min(num_questions, total_questions)
    random_questions = random.sample(list(Question.objects.all()), num_questions)
    return random_questions

def start_quiz(request):
    return redirect('random_question')

def quiz_completed(request, score):
    return render(request, 'quiz/quiz_completed.html', {
        'score': score
    })  

def random_question(request):

    if request.method == "POST":
        id = request.session.get('current_question_id')
        question = get_object_or_404(Question, pk=id)
        selected_choice_id = request.POST.get('choice')
        selected_choice = get_object_or_404(question.choice_set, pk=selected_choice_id)
        feedback = None
        if selected_choice.is_correct:
            feedback = "Correct!"
            request.session['correct_answer_count'] = request.session.get('correct_answer_count') + 1
        else:
            feedback = "Incorrect."
        return render(request, 'quiz/random_question.html', {
            'question': question,
            'feedback': feedback,
            'answer_disabled' : True
        })
    
    if request.session.get('session_end'):
        request.session['session_end'] = False
        score = request.session.get('correct_answer_count')
        request.session['correct_answer_count'] = 0,
        return quiz_completed(request, score)

    if not request.session.get('quiz_questions'):
        request.session['session_end'] = False
        request.session['correct_answer_count'] = 0
        question_ids = list(Question.objects.values_list('id', flat=True))
        question_ids = random.sample(question_ids, 5)
        random.shuffle(question_ids)
        request.session['quiz_questions'] = question_ids
    
    question_ids = request.session.get('quiz_questions', [])
    next_question_id = question_ids.pop()
    request.session['current_question_id'] = next_question_id
    request.session['quiz_questions'] = question_ids
    question = get_object_or_404(Question, pk=next_question_id)
    if not question_ids:
        request.session['session_end'] = True
    return render(request, 'quiz/random_question.html', {
        'question': question,
        'feedback': None,
        'answer_disabled':False
    })


# ---------------------------------------------------------------------------
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
                    auth_login(request, user)
                    return redirect('/', username=u)
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
    
@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'profile.html', { 'user': user })

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile', kwargs={'username': request.user.username}))  # Redirect to the user's profile page
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

def delete_profile(request):
    if request.method == 'POST':
        deleteUser = User.objects.get(username=request.user)
        deleteUser.delete()
        return redirect('/signup')
    return render(request, 'delete_account.html')
