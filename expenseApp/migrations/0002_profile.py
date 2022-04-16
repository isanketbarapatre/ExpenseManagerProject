# Generated by Django 4.0.3 on 2022-03-29 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenseApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=25)),
                ('Gender', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=10)),
                ('Mobile', models.CharField(max_length=10)),
                ('State', models.CharField(max_length=30)),
                ('City', models.CharField(max_length=30)),
                ('Address', models.TextField(max_length=200)),
                ('Master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenseApp.master')),
            ],
            options={
                'db_table': 'profile',
            },
        ),
    ]
