# Generated by Django 4.1 on 2022-09-03 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_alter_job_jobtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='jobLink',
            field=models.TextField(default=''),
        ),
    ]