from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

"""Create your models here."""


class UserProfileManager(BaseUserManager):
    """ Helps Django work with our custom user model.  """

    def create_user(self, email, name, bio,password=None):
        """Create a new user profile objects."""

        if not email:
            raise ValueError('User must have an email address.')

        """normalize the email to all lowercase"""
        email = self.normalize_email(email)
        """User object is created."""
        user = self.model(email=email, name=name, bio=bio)

        """set_password is use to encrypt the password"""
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """creates and save a new superuser with given details."""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ This class represents a 'User profile' inside our system. """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    bio = models.TextField(max_length=1000, default='')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    """ get helper function """
    def get_full_name(self):
        """Used to get User's full name"""

        return self.name

    def get_short_name(self):
        """Used to get User's short name"""
        return self.name

    def __str__(self):
        """ Django uses this when it needs to convert the object to a string """
        return self.email


class ProfileFeedItem(models.Model):
    """This is a New Model object which is related to UserProfile"""
    """Profile status update."""

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as string"""

        return self.status_text
