# Generated by Django 4.0.3 on 2022-04-05 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenseApp', '0003_alter_profile_address_alter_profile_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.FloatField()),
                ('BudgetMonth', models.IntegerField(choices=[(1, 'jan'), (2, 'feb'), (3, 'mar'), (4, 'apr'), (5, 'may'), (6, 'jun'), (7, 'jul'), (8, 'aug')])),
            ],
            options={
                'db_table': 'budget',
            },
        ),
        migrations.CreateModel(
            name='ExpenseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Icon', models.FileField(default='icon.png', upload_to='categories/')),
                ('Name', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'expensecategory',
            },
        ),
        migrations.CreateModel(
            name='Saving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BudgetMonth', models.IntegerField(choices=[(1, 'jan'), (2, 'feb'), (3, 'mar'), (4, 'apr'), (5, 'may'), (6, 'jun'), (7, 'jul'), (8, 'aug')])),
                ('Amount', models.FloatField()),
            ],
            options={
                'db_table': 'saving',
            },
        ),
        migrations.AlterField(
            model_name='profile',
            name='Gender',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female'), ('o', 'other')], max_length=10),
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateCreated', models.DateTimeField(auto_created=True)),
                ('Amount', models.FloatField()),
                ('Description', models.TextField(max_length=100)),
                ('ExpenseCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenseApp.expensecategory')),
            ],
            options={
                'db_table': 'expense',
            },
        ),
    ]
