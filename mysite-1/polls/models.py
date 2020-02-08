from django.db import models
from datetime
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self): # 주소값이 아니라 텍스트 값을 출력함
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.now() - datetime.timedelta(days=1)
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    #외래키(ForeignKey) - 질문항목을 받아서 선택지를 만듦//질문(1):선택지(N)의 관계를 형성한다
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

        