# Generated by Django 2.2.2 on 2019-08-13 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_profile_email_uc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_type',
            field=models.CharField(choices=[('S', 'Estudiante'), ('T', 'Profesor'), ('F', 'Funcionario'), ('C', 'CAi')], default='S', max_length=2),
        ),
    ]
