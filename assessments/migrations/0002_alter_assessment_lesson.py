# Generated by Django 5.1.6 on 2025-02-27 22:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0001_initial'),
        ('courses', '0004_userprogress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='courses.lesson'),
        ),
    ]
