# from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponseRedirect, HttpResponse,  Http404
# from django.urls import reverse

# # from django.http import Http404

# from .models import Question, Choice
# # -------
# import random
# # -----
# from django.utils import timezone
# from django.views.generic import DetailView

# #imports for authentication
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator



# # class QuestionDetailView(DetailView):
# #     model = Question
# #     template_name = 'quiz/question_detail.html'
# #     context_object_name = 'question'

# #     def get_queryset(self):
# #         """
# #         Excludes any questions that aren't published yet.
# #         """
# #         return Question.objects.filter(pub_date__lte=timezone.now())
    
#     # def question_list(request):
#     # questions = Question.objects.all()
#     # return render(request, 'quizes/question_list.html', {'questions': questions})

# def question_detail(request, question_id):
#     """
#     pull question from DB
#     need model form
#     if user submitted answer
#         process request
#         verify if answer is correct
#         update total on quiz accordingly
#         save quiz 
#     else show the blank form
#     render template
#     """
#     if request.method == 'POST':
#         try:
#             question = Question.objects.get(pk=question_id)
#             choice_id = request.POST.get('choice_id');
#             ch = Choice.objects.get(pk=choice_id)
#         except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#              return render(request, 'quiz/question_detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#             }) 
#         return render(request, "quiz/question_detail.html", {"question": question, "isCorrect": ch.is_correct})
#     else:
#         try:
#             question = Question.objects.get(pk=question_id)
#         except Question.DoesNotExist:
#             raise Http404("Question does not exist")
#         return render(request, "quiz/question_detail.html", {"question": question})
    
    
# def random_question(request):
#     feedback = None  # Initialize feedback
#     if request.method == "POST":
#         # Extracting 'question_id' from the form
#         question_id = request.POST.get('question_id')
#         selected_choice_id = request.POST.get('choice')

#         if question_id and selected_choice_id:
#             question = get_object_or_404(Question, pk=question_id)
#             selected_choice = question.choice_set.filter(pk=selected_choice_id).first()

#             if selected_choice and selected_choice.is_correct:
#                 feedback = "Correct!"
#             else:
#                 feedback = "Incorrect. Please try again."

#     # Select a new random question different from the last question
#     last_question_id = request.session.get('last_question_id')
#     question_ids = Question.objects.exclude(id=last_question_id).values_list('id', flat=True)
#     if question_ids:
#         random_id = random.choice(list(question_ids))
#         question = Question.objects.get(id=random_id)
#         request.session['last_question_id'] = question.id  # Update the session
#     else:
#         question = None  # Handle the case when there are no questions

#     return render(request, 'quiz/random_question.html', {
#         'question': question,
#         'feedback': feedback
#     })

    
# def home(request):
#     return render(request, "home.html")

# def login(request):
#     """ login to app"""
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             u = form.cleaned_data['username']
#             p = form.cleaned_data['password']
#             user = authenticate(username=u, password=p)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('home', username=u)
#                 else:
#                     print(f'{u} - account has been disabled')
#                     return HttpResponseRedirect('/login')
#             else:
#                 print('The username and/or password is incorrect')
#                 return HttpResponseRedirect('/login')
#         else:
#             return HttpResponseRedirect('/login')
#     else:
#         form = AuthenticationForm()
#         return render(request, 'login.html', { 'form': form })
    
# def logout(request):
#     logout(request)
#     return HttpResponseRedirect('/')

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return HttpResponseRedirect('/')
#         else:
#             return HttpResponseRedirect('signup/')
#     else:
#         form = UserCreationForm()
#         return render(request, 'signup.html', { 'form': form })


# #  get_object_or_404

# ------------------------------------------------------

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from .forms import EditProfileForm
import random

from .models import Question, Choice
from django.utils import timezone
from django.views.generic import DetailView

#imports for authentication
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login as auth_login 




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
    
# Place this in views.py or a separate utils.py file

def generate_quiz(num_questions):
    total_questions = Question.objects.count()
    num_questions = min(num_questions, total_questions)
    random_questions = random.sample(list(Question.objects.all()), num_questions)
    return random_questions



def start_quiz(request):
    # Generate a random quiz of 10 questions
    random_questions = generate_quiz(10)
    request.session['quiz_questions'] = [q.id for q in random_questions]  # Save question IDs in session
    request.session['current_question_index'] = 0  # Initialize question index

    return redirect('random_question')  # Redirect to show the first question

# Updated random_question view in views.py

def random_question(request):
    feedback = None
    question_ids = request.session.get('quiz_questions', [])
    current_index = request.session.get('current_question_index', 0)

    # Check if we have gone through all questions
    if current_index >= len(question_ids):
        # return render(request, 'quiz_completed.html')  # Or any other completion template
        # del request.session['quiz_questions']
        # del request.session['current_question_index']
        # Redirect to the quiz completed page
        return render(request, 'quiz/quiz_completed.html')

    # Fetch the current question
    current_question_id = question_ids[current_index]
    question = get_object_or_404(Question, id=current_question_id)

    if request.method == "POST":
        selected_choice_id = request.POST.get('choice')
        selected_choice = question.choice_set.filter(pk=selected_choice_id).first()

        if selected_choice and selected_choice.is_correct:
            feedback = "Correct!"
        else:
            feedback = "Incorrect."

        # Prepare for next question
        request.session['current_question_index'] = current_index + 1
        # return redirect('random_question')
    return render(request, 'quiz/random_question.html', {
        'question': question,
        'feedback': feedback
    })



# ---------------------------------- origional random ---------------------------
# def random_question(request):
#     feedback = None  # Initialize feedback
#     if request.method == "POST":
#         # Extracting 'question_id' from the form
#         question_id = request.POST.get('question_id')
#         selected_choice_id = request.POST.get('choice')

#         if question_id and selected_choice_id:
#             question = get_object_or_404(Question, pk=question_id)
#             selected_choice = question.choice_set.filter(pk=selected_choice_id).first()

#             if selected_choice and selected_choice.is_correct:
#                 feedback = "Correct!"
#             else:
#                 feedback = "Incorrect!"

#     # Select a new random question different from the last question
#     last_question_id = request.session.get('last_question_id')
#     question_ids = Question.objects.exclude(id=last_question_id).values_list('id', flat=True)
#     if question_ids:
#         random_id = random.choice(list(question_ids))
#         question = Question.objects.get(id=random_id)
#         request.session['last_question_id'] = question.id  # Update the session
#     else:
#         question = None  # Handle the case when there are no questions

#     return render(request, 'quiz/random_question.html', {
#         'question': question,
#         'feedback': feedback
#     })
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
                    return redirect('profile', username=u)
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
    pass

