# Generated by Django 3.1.1 on 2020-10-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0012_addsubject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addusers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Entername', models.CharField(max_length=50)),
                ('Emailid', models.EmailField(max_length=50)),
                ('Contactno', models.IntegerField(null=True)),
                ('EnterAddress', models.CharField(max_length=20)),
                ('SelectGender', models.CharField(max_length=20)),
                ('EnterDesignation', models.CharField(max_length=20)),
                ('Enterpassword', models.CharField(max_length=20, null=True)),
                ('confirmpassword', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
