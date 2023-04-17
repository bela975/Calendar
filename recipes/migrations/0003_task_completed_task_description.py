# Generated by Django 4.2 on 2023-04-16 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.CharField(default='No description', max_length=200),
        ),
    ]