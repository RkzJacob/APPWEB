# Generated by Django 3.0.7 on 2022-05-08 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0004_auto_20220508_1615'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Consulta',
        ),
        migrations.AlterField(
            model_name='medicamento',
            name='codigo',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
