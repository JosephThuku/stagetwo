from django.db import models
"""
models for the person app
"""

class Person(models.Model):
    """
    Peron model with age,userid and name as attributes
    """
    userid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)


    def __str__(self):
        return self.name
    

    class Meta:
        ordering = ['userid']
        db_table = 'Person'