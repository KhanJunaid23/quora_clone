from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import AnswerForm, QuestionForm, UserRegistrationForm
from .models import Question, Answer

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'core/register.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

@login_required
def post_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            messages.success(request, 'Question posted successfully!')
            return redirect('question-detail', pk=question.pk)
    else:
        form = QuestionForm()
    return render(request, 'core/post_question.html', {'form': form})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answers.all().order_by('-created_at')
    if request.method == 'POST' and request.user.is_authenticated:
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            messages.success(request, 'Answer posted successfully!')
            return redirect('question-detail', pk=pk)
    else:
        answer_form = AnswerForm()
    return render(request, 'core/question_detail.html', {'question': question, 'answers': answers, 'answer_form': answer_form})

@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    if request.user in answer.likes.all():
        answer.likes.remove(request.user)
    else:
        answer.likes.add(request.user)
    return redirect('question-detail', pk=answer.question.pk)

def home(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'core/home.html', {'questions': questions})
