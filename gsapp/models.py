from django.db import models

GENDER_Choice = (('MALE','MALE'),('FEMALE','FEMALE'),('OTHER','OTHER'))

class Register_std(models.Model):
    name = models.CharField(max_length=255,blank=True ,null=True)
    father_name = models.CharField(max_length=255,blank=True ,null=True)
    mobile_no = models.IntegerField(blank=True ,null=True)
    email = models.EmailField(max_length=255,blank=True ,null=True)
    gender = models.CharField(choices=GENDER_Choice,default='MALE',max_length=255)
    address = models.CharField(max_length=255,blank=True ,null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class IsFormActive(models.Model):
    active_status = models.BooleanField(default=True)    