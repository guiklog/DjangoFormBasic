from django.db import models

# Create your models here.

class basicform(models.Model):
    firstname = models.CharField(max_length=50, verbose_name='First Name') 
    lastname = models.CharField(max_length=50, verbose_name='Last Name')
    email = models.EmailField(max_length=50, verbose_name='Email')
    phone = models.CharField(max_length=50, verbose_name='Your Phone Number')
    subject = models.CharField(max_length = 255, verbose_name='Subject')
    message = models.TextField(default = 'Your message', verbose_name='Your Message')
    checkbox =models.BooleanField(default = True, verbose_name='I agree to be contacted back')
    
    
    
    