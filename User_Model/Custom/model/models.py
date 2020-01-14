from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class InfoManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if not email:
            raise ValueError('user must have an email address')
        email = self.normalize_email(email)
        user = self.model(
            username =  username,
            email = self.normalize_email(email)
            )
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,username,email,password=None):
        user = self.create_user(
            username,email,password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
        if user.is_staff is not True:
            raise ValueError('superuser must have is_staff=True.')
        if user.is_superuser is not True:
            raise ValueError('superuser must have is_superuser=True')





class Info(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=254, unique = True)
    username = models.CharField(max_length=50,unique= True)
    is_admin = models.BooleanField('manager',default= False)
    is_active = models.BooleanField('active status',default = True)
    is_staff = models.BooleanField('staff status',default = False)
    is_superuser = models.BooleanField('superuser',default = False)

    objects = InfoManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]
