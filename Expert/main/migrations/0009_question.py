# Generated by Django 3.1.8 on 2022-10-15 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_mail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Вопрос')),
                ('answer', models.TextField(verbose_name='Ответ')),
                ('is_visible', models.BooleanField(verbose_name='Отображение')),
            ],
        ),
    ]
