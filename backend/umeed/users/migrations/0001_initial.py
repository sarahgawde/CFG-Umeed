# Generated by Django 3.0.2 on 2020-07-25 21:30

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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=100)),
                ('image', models.ImageField(default='default.jpg', null=True, upload_to='user_images')),
                ('skills', models.TextField()),
                ('user_acc', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phn_number', models.CharField(max_length=12, null=True)),
                ('image', models.ImageField(default='default.jpg', null=True, upload_to='manager_images')),
                ('area', models.CharField(max_length=100)),
                ('unset', models.BooleanField(default=True)),
                ('user_acc', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
