# Generated by Django 4.2.7 on 2023-12-11 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_BOOK_APP', '0014_lecture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='date',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
    ]