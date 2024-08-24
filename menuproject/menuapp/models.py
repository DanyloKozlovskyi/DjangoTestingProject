from django.db import models as md


# Create your models here.
class Question(md.Model):
    question_text = md.CharField(max_length=300)
    pub_date = md.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(md.Model):
    question = md.ForeignKey(Question, on_delete=md.CASCADE)
    choice_text = md.CharField(max_length=200)
    votes = md.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
