# Generated by Django 4.2.7 on 2023-12-06 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_BOOK_APP', '0006_alter_livre_image1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livre',
            name='pdf',
            field=models.FileField(upload_to='livres_pdf'),
        ),
    ]