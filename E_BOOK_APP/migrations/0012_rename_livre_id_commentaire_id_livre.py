# Generated by Django 4.2.7 on 2023-12-11 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('E_BOOK_APP', '0011_commentaire'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentaire',
            old_name='livre_id',
            new_name='id_livre',
        ),
    ]
