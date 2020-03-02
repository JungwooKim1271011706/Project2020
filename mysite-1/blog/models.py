from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    comments = models.Manager() #에러 제거
    objects = models.Manager() #에러 제거
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self): #Post 1, 2, 3, etc에 해당하는 승인된 코멘트의 수를 표시하기 위해서 존재
        return self.comments.filter(approved_comment=True)

    def approved_comments_counts(self):
        return len(self.comments.filter(approved_comment=True))
    

    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    approved_comment=models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()
        
    def __str__(self):
        return self.text


