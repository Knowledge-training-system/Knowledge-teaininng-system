# Generated by Django 3.0.7 on 2020-06-17 05:06

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('modelsApp', '0004_auto_20200617_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionslist',
            name='answer',
            field=jsonfield.fields.JSONField(),
        ),
    ]
