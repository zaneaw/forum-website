# Generated by Django 3.2.3 on 2021-12-01 04:26

from django.db import migrations, models
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/projects', validators=[projects.models.file_size]),
        ),
    ]
