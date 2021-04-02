# Generated by Django 2.2 on 2021-03-31 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_TP', models.CharField(max_length=30)),
                ('pasal_TP', models.CharField(max_length=30)),
                ('kategori_TP', models.CharField(choices=[('AP1', 'AP1'), ('AP2', 'AP2'), ('AP3', 'AP3')], default='AP1', max_length=3)),
            ],
        ),
    ]
