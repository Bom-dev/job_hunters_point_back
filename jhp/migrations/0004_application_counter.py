# Generated by Django 4.1.1 on 2022-09-05 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jhp', '0003_alter_application_date_alter_user_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='counter',
            field=models.IntegerField(default=1),
        ),
    ]
