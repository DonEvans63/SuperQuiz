# Generated by Django 5.0.1 on 2024-02-25 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_quiz_app', '0002_quiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='choice',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
