# Generated by Django 3.2.5 on 2021-09-02 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_subject_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='Student',
            new_name='student',
        ),
    ]