from django.db import models
from django.contrib.auth.models import User
from Quiz.models import Aquiz
# Create your views here.


class Result(models.Model):
    quiz = models.ForeignKey(Aquiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk)
