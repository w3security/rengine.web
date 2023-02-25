# Generated by Django 3.2.4 on 2022-03-10 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0012_auto_20220310_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directoryscan',
            name='dir_subscan_ids',
            field=models.ManyToManyField(blank=True, related_name='dir_subscan_ids', to='startScan.SubScan'),
        ),
        migrations.AlterField(
            model_name='directoryscan',
            name='directory_files',
            field=models.ManyToManyField(blank=True, related_name='directory_files', to='startScan.DirectoryFile'),
        ),
    ]
