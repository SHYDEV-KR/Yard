# Generated by Django 4.0.2 on 2022-02-19 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='inputTags',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='나만의 해시태그를 작성해보세요 ex)#Yar:d 짱 #야드핫플'),
        ),
    ]
