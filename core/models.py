from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Question(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Questions"
        verbose_name = "Question"
        db_table = "questions"

    def get_absolute_url(self):
        return reverse('question-detail', kwargs={'pk': self.pk})
    
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_answers', blank=True)

    def __str__(self):
        return f"Answer to {self.question.title}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Answers"
        verbose_name = "Answer"
        db_table = "answers"

    def total_likes(self):
        return self.likes.count()
