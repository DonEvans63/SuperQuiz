from django.shortcuts import render
from django.http import HttpResponse

from .models import Question, Choice
from django.utils import timezone
from django.views.generic import DetailView



class QuestionDetailView(DetailView):
    model = Question
    template_name = 'quiz/question_detail.html'
    context_object_name = 'question'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
    
    # def question_list(request):
    # questions = Question.objects.all()
    # return render(request, 'quizes/question_list.html', {'questions': questions})
