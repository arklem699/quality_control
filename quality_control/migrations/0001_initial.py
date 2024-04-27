# Generated by Django 5.0.4 on 2024-04-27 20:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BugReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('New', 'Новый'), ('In_progress', 'В работе'), ('Completed', 'Завершён')], default='New', max_length=50)),
                ('priority', models.CharField(choices=[('1', 'Низший'), ('2', 'Низкий'), ('3', 'Средний'), ('4', 'Высокий'), ('5', 'Наивысший')], default='1', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.project')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.task')),
            ],
        ),
        migrations.CreateModel(
            name='FeatureRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('Under_consideration', 'На рассмотрении'), ('Accepted', 'Принято'), ('Rejected', 'Отклонено')], default='Under_consideration', max_length=50)),
                ('priority', models.CharField(choices=[('1', 'Низший'), ('2', 'Низкий'), ('3', 'Средний'), ('4', 'Высокий'), ('5', 'Наивысший')], default='1', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.project')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.task')),
            ],
        ),
    ]
