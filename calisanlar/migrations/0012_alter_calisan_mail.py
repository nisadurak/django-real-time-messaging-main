# Generated by Django 4.2.15 on 2024-08-25 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calisanlar', '0011_alter_calisan_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calisan',
            name='mail',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
    ]
