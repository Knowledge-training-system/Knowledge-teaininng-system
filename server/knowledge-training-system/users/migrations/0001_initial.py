# Generated by Django 3.0.7 on 2020-06-21 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=5, null=True)),
                ('name', models.CharField(max_length=20, null=True)),
                ('age', models.IntegerField(null=True)),
                ('identity', models.CharField(max_length=20, null=True)),
                ('phonenum', models.CharField(max_length=20, null=True)),
                ('theUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extra', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ExtraUser',
            },
        ),
    ]
