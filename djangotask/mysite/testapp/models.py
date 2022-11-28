from django.db import models

class list(models.Model):
    list_text=models.CharField(max_length=260)
    def __str__(self) :
        return self.list_text

