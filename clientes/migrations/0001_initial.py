# Generated by Django 3.2.8 on 2021-10-21 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomecompleto', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('telefone', models.IntegerField()),
                ('cpf', models.IntegerField()),
                ('rua', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('pais', models.CharField(default='Brasil', max_length=100)),
                ('foto', models.ImageField(upload_to='fotos/clientes')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
