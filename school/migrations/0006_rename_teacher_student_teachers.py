# Generated by Django 4.1.4 on 2022-12-09 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_rename_teachers_student_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teacher',
            new_name='teachers',
        ),
    ]
