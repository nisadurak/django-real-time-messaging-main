# Generated by Django 4.2.15 on 2024-08-22 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calisan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=100)),
                ('soyisim', models.CharField(max_length=100)),
                ('yas', models.IntegerField()),
                ('departman', models.CharField(max_length=100)),
                ('maas', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
