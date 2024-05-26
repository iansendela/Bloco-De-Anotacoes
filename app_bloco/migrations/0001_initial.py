# Generated by Django 4.2.11 on 2024-04-19 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BlocaoNota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('assunto', models.CharField(max_length=255)),
                ('conclusao', models.TextField()),
                ('data_criada', models.DateField(auto_now_add=True)),
                ('tema', models.ManyToManyField(to='app_bloco.tema')),
            ],
            options={
                'verbose_name': 'BlocoNota',
                'verbose_name_plural': 'BlocosNotas',
                'ordering': ['-data_criada'],
            },
        ),
    ]
