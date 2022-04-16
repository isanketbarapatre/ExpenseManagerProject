from django.db import models

# Create your models here.
class Master(models.Model):
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=12)
    IsActive = models.BooleanField(default=False)

    class Meta:
        db_table = 'master'

gender_choices = (
    ('m', 'male'),
    ('f', 'female'),
    ('o', 'other'),
)

class Profile(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    FullName = models.CharField(max_length=25, default='')
    Gender = models.CharField(max_length=10, choices=gender_choices)
    Mobile = models.CharField(max_length=10, default='')
    State = models.CharField(max_length=30, default='')
    City = models.CharField(max_length=30, default='')
    Address = models.TextField(max_length=200, default='')

    class Meta:
        db_table = 'profile'

month_choices = (
    (1, 'jan'),
    (2, 'feb'),
    (3, 'mar'),
    (4, 'apr'),
    (5, 'may'),
    (6, 'jun'),
    (7, 'jul'),
    (8, 'aug'),
)
class Budget(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Amount = models.FloatField()
    BudgetMonth = models.IntegerField(choices=month_choices)

    class Meta:
        db_table = 'budget'
    
class Saving(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    BudgetMonth = models.IntegerField(choices=month_choices)
    Amount = models.FloatField()

    class Meta:
        db_table = 'saving'

class ExpenseCategory(models.Model):
    Icon = models.FileField(upload_to='categories/', default='icon.png')
    Name = models.CharField(max_length=25)

    class Meta:
        db_table = 'expensecategory'

    def __str__(self):
        return self.Name

class Expense(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    ExpenseCategory = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    Amount = models.FloatField()
    DateCreated = models.DateTimeField(auto_created=True)
    Description = models.TextField(max_length=100)

    class Meta:
        db_table = 'expense'