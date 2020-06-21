from django.db import models
from django.conf import settings
from django.utils import timezone
from django.shortcuts import reverse

# Create your models here.

class Request(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('request_merge')

class vendor(models.Model):
    매출처명 = models.TextField()
    쇼핑몰 = models.TextField()
    생산처 = models.TextField()
    상품명 = models.TextField()
    수량 = models.IntegerField()
    박스수량 = models.IntegerField()
    선불비 = models.IntegerField()
    착불비 = models.IntegerField()
    주문자명 = models.TextField()
    주문자전화 = models.TextField()
    주문자휴대폰 = models.TextField()
    수취인명 = models.TextField()
    수취인전화 = models.TextField()
    수취인휴대폰 = models.TextField()
    수취인주소 = models.TextField()
    배송메시지 = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.수취인명
    
