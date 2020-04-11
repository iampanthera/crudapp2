from django.db import models

# Create your models here.
class person(models.Model):
    degree=(
        (0,'Bs'),
        (1,'Ms'),
        (2,'PhD')
        )

    name  = models.CharField(max_length=50)
    email  = models.EmailField()
    password  = models.CharField (max_length=10,null=False)
    # degree  = models.Char (choices=degree,max_length=3)
    isStudent = models.BooleanField(max_length=1)
    date  = models.DateField(null=False,auto_now=True)
    dateTime  = models.DateTimeField()
    age  = models.IntegerField()
    cv  = models.FileField(upload_to='uploads/')
    sallary  = models.DecimalField(decimal_places=2,max_digits=4)
    info  = models.TextField(blank=True)
    image  = models.ImageField(upload_to='covers/',blank=True)