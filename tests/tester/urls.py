from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns =[
    path('',polls_page,name='polls'),
    path('questions/<int:poll_id>/',questions_page,name='questions'),
    path('answer/<int:question_id>/',choiceanswer_page,name='answer'),
]