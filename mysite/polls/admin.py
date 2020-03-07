from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2
    
class QuestionAdmin(admin.ModelAdmin):
    # field = ['pub_date','question_text'] 필드 순서 변경하기
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('Date Information', {'fields':['pub_date'], 'classes':['collapse']}), #필드 나누기 및 필드 접기 기능 추가
    ]
    inlines = [ChoiceInline] #Choice 모델 클래스 같이 보기
    list_display = ('question_text', 'pub_date') #레코드 리스트 컬럼 지정
    list_filter = ['pub_date'] # 시간 필터
    search_fields = ['question_text'] # 검색 기능 추가

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

