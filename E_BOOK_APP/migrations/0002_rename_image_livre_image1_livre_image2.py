# Generated by Django 4.2.7 on 2023-12-05 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_BOOK_APP', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livre',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='livre',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='Images_Livres'),
        ),
    ]