# Generated by Django 4.2.6 on 2023-12-01 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=100, verbose_name='Пароль'),
        ),
    ]