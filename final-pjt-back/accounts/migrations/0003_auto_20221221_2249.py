# Generated by Django 3.2.13 on 2022-12-21 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_sociallogin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SocialLogin',
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='mbti',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
