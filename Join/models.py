from django.db import models

class Join(models.Model):
    varEmail = models.EmailField()
    varName = models.CharField(max_length=30)
    varUser = models.CharField(max_length=30)
    varTimestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    varUpdated = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return '%s' % self.varEmail
