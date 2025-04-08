from django.urls import path
from .views import (
    register, 
    user_logout, 
    post_question, 
    question_detail, 
    like_answer, 
    home
)

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('question/<int:pk>', question_detail, name='question-detail'),
    path('post_question/', post_question, name='post-question'),
    path('like_answer/<int:answer_id>/', like_answer, name='like-answer'),
]