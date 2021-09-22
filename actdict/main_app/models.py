from django.db import models

# Create your models here.
class Languages(models.Model):
    language = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.language

class Users(models.Model):
    user = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.user

class Words(models.Model):
    word = models.CharField(max_length=128, verbose_name='Word')
    language_id = models.ForeignKey('Languages', on_delete=models.PROTECT)
    score = models.IntegerField(blank=True, null=True, verbose_name='Current score')
    max_score = models.IntegerField(blank=True, null=True, verbose_name='Naximum score')
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Words'
        verbose_name = 'Word'