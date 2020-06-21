from django import forms
from .models import Request
from django.utils.translation import gettext_lazy as _

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['author', 'name','address','phone_number','text' ]
        labels = {
            'author':_('작성자'),
            'name':_('수취인'),
            'address':_('주소'),
            'phone_number':_('전화번호'),
            'text':_('클레임 사항')
        }

 