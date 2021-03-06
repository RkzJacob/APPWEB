# Generated by Django 3.0.7 on 2022-05-04 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='medicamento',
            fields=[
                ('codigo', models.CharField(max_length=5, primary_key=True, serialize=False, verbose_name='codigo')),
                ('nombreMedicamento', models.CharField(max_length=40, verbose_name='NombreMedicamento')),
                ('DescripcionMedicamento', models.CharField(max_length=40, verbose_name='DescripcionMedicamento')),
                ('FabricanteMedicamento', models.CharField(max_length=40, verbose_name='FabricanteMedicamento')),
                ('ContenidoMedicamento', models.CharField(max_length=40, verbose_name='ContenidoMedicamento')),
                ('cantidad', models.IntegerField(verbose_name='cantidad')),
                ('gramaje', models.IntegerField(verbose_name='gramaje')),
            ],
        ),
    ]
