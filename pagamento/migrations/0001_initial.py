# Generated by Django 3.2.8 on 2021-10-21 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=50)),
                ('parcelas', models.IntegerField()),
                ('v_parcelas', models.FloatField(max_length=100)),
                ('v_total', models.FloatField(max_length=100)),
                ('ent_rua', models.CharField(max_length=100)),
                ('ent_numero', models.IntegerField()),
                ('ent_complemento', models.CharField(max_length=100)),
                ('ent_bairro', models.CharField(max_length=100)),
                ('ent_cidade', models.CharField(max_length=100)),
                ('ent_estado', models.CharField(max_length=100)),
                ('ent_pais', models.CharField(default='Brasil', max_length=100)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]