# Generated by Django 4.0.2 on 2022-02-11 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_feed_createddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='createdDate',
            field=models.DateField(verbose_name='피드 생성일'),
        ),
    ]
