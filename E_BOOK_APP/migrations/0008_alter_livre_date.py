# Generated by Django 4.2.7 on 2023-12-06 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_BOOK_APP', '0007_alter_livre_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livre',
            name='date',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
    ]