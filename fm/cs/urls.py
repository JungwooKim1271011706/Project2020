from django.urls import path
from . import views

urlpatterns =[
    path('', views.vendorview.as_view(), name='vendor'),
    path('request/', views.Requestview.as_view(), name='request_merge'),
    path('request/text/', views.text, name='text_table'),
    
    # path('request/<int:pk>/delete', views.RequestDelete.as_view(), name='request_delete'),
]