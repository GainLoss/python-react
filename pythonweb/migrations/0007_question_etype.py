# Generated by Django 2.1 on 2018-09-04 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythonweb', '0006_question_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='etype',
            field=models.CharField(default='moren', max_length=45),
        ),
    ]
