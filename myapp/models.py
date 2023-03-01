from django.db import models

# Create your models here.
class Client(models.Model):
    branc =[('Aluva','Aluva'),('Edapally','Edapally'),('Vazhakala','Vazhakala'),('Kakkanad','Kakkanad'),('Mattancheri','Mattancheri')]
    choice = [('male','Male'),('female','Female'),('trans','Transgender')]
    account = [('Savings account','Savings account'),('Current account','Current account'),('Salary account','Salary account'),('Fixed deposit account','Fixed deposit account'),('Recurring deposit account','Recurring deposit account'),('NRI account','NRI account')]
    meterial = [('Credit card','Credit card'),('Debit card','Debit card'),('Pass book','Pass book'),('Cheque book','Cheque book')]
    locatn = [('Trivandrum','Trivandrum'),('Kottayam','Kottayam'),('Ernakulam','Ernakukulam'),('Wayanad','Wayanad'),('Kozhikode','Kozhikode')]
    Name = models.CharField(max_length=30,null=True)
    username = models.CharField(max_length=30,null=True)
    password = models.CharField(max_length=20,default='drisya1234',null=True)
    Confirm_password = models.CharField(max_length=20,null=True)
    Date_of_birth = models.DateField(null=True)
    Age = models.IntegerField(null=True)
    Gender = models.CharField(choices=choice,max_length=20,null=True)
    Mobile_number = models.IntegerField(null=True)
    Email_id = models.EmailField(null=True)
    District = models.CharField(choices=locatn,max_length=30,null=True)
    Address = models.CharField(max_length=50,null=True)
    Branch = models.CharField(choices= branc ,max_length=30,null=True)
    Account_type = models.CharField(choices= account, max_length=50,null=True)
    Meterials_provide = models.CharField(choices= meterial, max_length=50,null=True)
    

    class Meta:
        verbose_name_plural = "Client details"
    def __str__(self):
        return self.username