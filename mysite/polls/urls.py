from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'), #클래스형 뷰
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), #디테일뷰
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'), #리저트뷰
    path('<int:question_id>/vote/', views.vote, name='vote'),
]