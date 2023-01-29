from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class User(AbstractUser):
    RECRUITER = 'RECRUITER'
    COWORKER = 'COWORKER'
    FRIEND = 'FRIEND'

    ROLE_CHOICES = (
        (RECRUITER, 'Recruteurs'),
        (COWORKER, 'Collègues'),
        (FRIEND, 'Amis')
    )
    profile_photo = models.ImageField(verbose_name='Photo de profil')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
    follows = models.ManyToManyField(
        'self',
        limit_choices_to={'role': COWORKER},
        symmetrical=False,
        verbose_name='suit',
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role == self.COWORKER:
            group = Group.objects.get(name='coworkers')
            group.user_set.add(self)
        elif self.role == self.RECRUITER:
            group = Group.objects.get(name='recruiters')
            group.user_set.add(self)
