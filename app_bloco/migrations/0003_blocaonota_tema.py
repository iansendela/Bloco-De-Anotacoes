# Generated by Django 4.2.11 on 2024-04-19 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_bloco', '0002_remove_blocaonota_tema'),
    ]

    operations = [
        migrations.AddField(
            model_name='blocaonota',
            name='tema',
            field=models.ManyToManyField(to='app_bloco.tema'),
        ),
    ]