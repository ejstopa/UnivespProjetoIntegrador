# Generated by Django 3.2.7 on 2021-10-10 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'theme',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('answer', models.CharField(max_length=500)),
                ('image', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('theme_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.theme')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'questions',
            },
        ),
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempt_number', models.IntegerField()),
                ('attempt_date', models.DateTimeField(auto_now_add=True)),
                ('difficult', models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Difficult')])),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.question')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'attempts',
            },
        ),
    ]
