# Generated by Django 3.2.2 on 2021-05-07 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('model', models.CharField(max_length=25)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color', models.CharField(choices=[('GREY', 'Grey'), ('RED', 'Red'), ('BLACK', 'Black'), ('PURPLE', 'Purple')], max_length=6)),
            ],
        ),
    ]
