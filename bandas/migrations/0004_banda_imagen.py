# Generated by Django 4.0.6 on 2022-09-04 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0003_banda_fecha_del_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='banda',
            name='imagen',
            field=models.ImageField(null=True, upload_to='posteos'),
        ),
    ]