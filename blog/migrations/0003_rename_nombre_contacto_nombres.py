# Generated by Django 4.1.2 on 2022-11-24 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_info_nosotros'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacto',
            old_name='nombre',
            new_name='nombres',
        ),
    ]
