from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=100, default="default quiz")
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.title

    def get_questions(self):
        return self.question_set.all()

class Question(models.Model):
    # title = models.CharField(max_length = 100)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text


