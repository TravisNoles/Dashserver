# Generated by Django 3.1 on 2020-08-14 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servermgr', '0003_auto_20200814_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='location',
            field=models.CharField(choices=[(2, 'Chicago'), (6, 'Atlanta'), (1, 'New Jersey'), (3, 'Dallas'), (5, 'Los Angeles'), (39, 'Miami'), (4, 'Seattle'), (8, 'London'), (22, 'Toronto'), (19, 'Sydney'), (34, 'Seoul'), (24, 'Paris'), (12, 'Silicon Valley'), (40, 'Singapore'), (7, 'Amsterdam'), (25, 'Tokyo'), (9, 'Frankfurt')], max_length=20),
        ),
    ]
