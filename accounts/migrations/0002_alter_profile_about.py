# Generated by Django 3.2.3 on 2021-11-30 19:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=ckeditor.fields.RichTextField(blank=True, max_length=1000, null=True),
        ),
    ]
