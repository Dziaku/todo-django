# Generated by Django 5.1.1 on 2024-09-12 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0004_alter_todolist_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='date',
            field=models.DateTimeField(default='django.utils.timezone.now', verbose_name='date-of-creation'),
        ),
    ]
