# Generated by Django 5.0.3 on 2024-04-22 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0002_remove_event_event_remove_person_people_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventdetail',
            name='event_text',
        ),
        migrations.RemoveField(
            model_name='persondetail',
            name='person_text',
        ),
    ]
