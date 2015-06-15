from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from colorful.fields import RGBColorField
# Create your models here.

class GlobalSettingsManager(models.Manager):
      def get_setting(self, key):
          try:
              setting = GlobalSettings.objects.get(key=key)
          except:
              return "N/A"
          return setting

class GlobalSettings(models.Model):
      key = models.CharField(unique=True, max_length=255)
      value = models.CharField(max_length=255)
      objects = GlobalSettingsManager()

      def __unicode__(self):
          return "${0} = {1}".format(self.key.upper(), self.value)

class Policy(models.Model):
    text = models.CharField(max_length=9000)
    color = RGBColorField(default='#123445')
    author = models.ForeignKey('User')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text

class UserManager(BaseUserManager):
    def create_user(self, email, password, commit=True):
        if not email or not password:
            raise ("Users must have an email and password")

        user = self.model(
            email=self.normalize_email(email),
        )
        user.is_active = False
        user.set_password(password)
        if commit:
            user.save(using=self._db)

        return user

    def create_superuser(self, email, password, commit=True):
        user = self.create_user(email, password)

        user.is_active = True
        user.is_admin = True

        if commit:
            user.save(using=self._db)

        return user

    def get_by_email(self, email):
        try:
            return self.get(email=email)
        except User.DoesNotExist:
            return None


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_full_Name(self):
        return self.email

    def get_short_name(self):
        return self.email

    @staticmethod
    def has_perm(perm, obj=None):
        return True

    @staticmethod
    def has_perms(perm, obj=None):
        return True

    @staticmethod
    def has_module_perms(app_label):
        return True

    def is_staff(self):
        return self.is_admin

    def __unicode__(self):
        value = "Super: {0}" if self.is_admin else "User: {0}"
        return value.format(self.email)