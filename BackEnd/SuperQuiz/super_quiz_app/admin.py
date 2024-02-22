from django.contrib import admin
from .models import Quiz, Question, Choice, Answer

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4  # Number of extra choices fields to display

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1  # Number of extra answer fields to display

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline, AnswerInline]

admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Answer)