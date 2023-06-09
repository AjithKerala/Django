# Generated by Django 4.1.7 on 2023-04-17 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new1', '0002_departmentss_delete_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='docterdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='main')),
                ('docname', models.CharField(max_length=200)),
                ('specilisation', models.CharField(max_length=200)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new1.departmentss')),
            ],
        ),
    ]
