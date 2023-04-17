# Generated by Django 4.2 on 2023-04-16 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200)),
                ('due_date', models.DateField()),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.pet')),
            ],
        ),
    ]
