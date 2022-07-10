import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # Field명은 기계가 읽기 좋은 형식(machine-friendly format)
    # 데이터베이스 필드 이름(컬럼명으로 사용됨)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') # 사람이 읽기 좋은(human-readable) 이름을 지정할 수 있음

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # CASCADE -> 연결된 Question이 삭제되면 해당 Choice도 삭제하겠다.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

