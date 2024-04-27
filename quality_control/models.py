from django.db import models
from tasks.models import Project, Task


class BugReport(models.Model):
    STATUS_CHOICES = [
        ('New', 'Новый'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершён')
    ]
    PRIORITY_CHOICES = [
        ('1', 'Низший'),
        ('2', 'Низкий'),
        ('3', 'Средний'),
        ('4', 'Высокий'),
        ('5', 'Наивысший')
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New'
    )
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY_CHOICES,
        default='1'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FeatureRequest(models.Model):
    STATUS_CHOICES = [
        ('Under_consideration', 'На рассмотрении'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено')
    ]
    PRIORITY_CHOICES = [
        ('1', 'Низший'),
        ('2', 'Низкий'),
        ('3', 'Средний'),
        ('4', 'Высокий'),
        ('5', 'Наивысший')
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    ) 
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='Under_consideration'
    )
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY_CHOICES,
        default='1'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)