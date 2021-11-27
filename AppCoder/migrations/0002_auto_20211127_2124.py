# Generated by Django 3.2.9 on 2021-11-27 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion_retiro', models.CharField(max_length=20)),
                ('ubicacion_retorno', models.CharField(max_length=20)),
                ('conductor', models.CharField(max_length=20)),
                ('preferencia_aire_acondicionado', models.BooleanField()),
                ('preferencia_musica', models.BooleanField()),
                ('forma_de_pago', models.CharField(max_length=10)),
                ('numero', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Reserva',
        ),
        migrations.RemoveField(
            model_name='auto',
            name='anio',
        ),
    ]