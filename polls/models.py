from django.db import models

# Create your models here.
# class user(models.Model) :
#     name = models.CharField(max_length=100)
#     amount = models.CharField(max_length=100)

#     def get_all_user_data() :
#         return user.objects.all()
    
#     def get_all_user_ids() :
#         return user.objects.values_list('id',flat=True)
    
# class luckyuser(models.Model) :
#     name = models.CharField(max_length=100)
#     amount = models.CharField(max_length=100)       


class Registration(models.Model) :
    name = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    pswd = models.CharField(max_length=12)

    def register(self) :
        self.save()
    
    def isExists(self) :
        if Registration.objects.filter(mail=self.mail) :
            return True
        else :
            return False

class Customer(models.Model) :
    name = models.CharField(max_length=50, blank=True, null=True)
    amount = models.CharField(max_length=50)
    create_at_Date = models.DateField(auto_now_add=True, null=True)

    def get_all_user_data() :
        return Customer.objects.all()
    
    def get_all_user_ids() :
        return Customer.objects.values_list('id', flat=True)

class Win(models.Model) : 
    Date = models.DateField(unique=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    amount = models.CharField(max_length=50)

    def get_all_win_user_data() :
        return Win.objects.all()    
    
class Admins(models.Model) :
    name = models.CharField(max_length=30, blank=True, null=True) 
    mail = models.CharField(max_length=30, blank=True, null=True)
    
    class Meta :
        permissions = [
            ("withdraw", "withdraw"),
        ]        

    def get_all_Admins_Data() :
        return Admins.objects.all()         