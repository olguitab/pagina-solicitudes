# Generated by Django 2.2.2 on 2019-07-03 12:14

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email_uc', models.EmailField(max_length=254)),
                ('profile_type', models.CharField(choices=[('S', 'Estudiante'), ('T', 'Profesor'), ('F', 'Funcionario')], default='S', max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
