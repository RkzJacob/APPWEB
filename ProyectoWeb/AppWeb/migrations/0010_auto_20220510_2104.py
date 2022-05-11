# Generated by Django 3.0.7 on 2022-05-11 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0009_auto_20220510_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='medicamentoRecetado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppWeb.Medicamento'),
        ),
        migrations.AlterField(
            model_name='retiromedicamento',
            name='medicamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppWeb.Medicamento'),
        ),
    ]
