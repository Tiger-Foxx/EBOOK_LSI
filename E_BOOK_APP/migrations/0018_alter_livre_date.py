# Generated by Django 5.0 on 2023-12-28 06:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_BOOK_APP', '0017_alter_lecture_date_alter_livre_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livre',
            name='date',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2023, 12, 28, 7, 26, 46, 186163)),
        ),
    ]