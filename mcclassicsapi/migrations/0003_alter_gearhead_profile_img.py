# Generated by Django 4.0.3 on 2022-03-16 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcclassicsapi', '0002_alter_projects_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gearhead',
            name='profile_img',
            field=models.ImageField(upload_to=''),
        ),
    ]
