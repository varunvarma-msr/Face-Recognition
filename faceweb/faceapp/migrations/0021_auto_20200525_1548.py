# Generated by Django 2.2.4 on 2020-05-25 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faceapp', '0020_auto_20200525_0653'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='teacherclass',
            unique_together={('user', 'classRoom', 'subject')},
        ),
    ]
