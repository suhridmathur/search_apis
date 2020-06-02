from django.contrib import admin
from django.urls import path

from rest_framework.authtoken import views

from . import apis

urlpatterns = [
    path('api/v1/login/', views.obtain_auth_token, name='login_api'),
    path('api/v1/search/', apis.SearchAPI.as_view(), name='search_api'),
    path('api/v1/questions/<int:question_id>/', apis.QuestionDetailAPI.as_view(), name='question_api'),
    path('api/v1/questions/<int:question_id>/answers/', apis.AnswersAPI.as_view(), name='answers_api'),
]
