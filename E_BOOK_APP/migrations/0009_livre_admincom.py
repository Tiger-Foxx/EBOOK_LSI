# Generated by Django 4.2.7 on 2023-12-10 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_BOOK_APP', '0008_alter_livre_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='livre',
            name='AdminCom',
            field=models.TextField(blank=True, default="AUCUN COMMENTAIRE DE L'ADMINISTRATEUR POUR LE MOMENT", null=True),
        ),
    ]
