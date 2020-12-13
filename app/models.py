from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Profile(models.Model):
  user = models.ForeignKey(User, related_name='user_profile', on_delete=models.CASCADE)
  name = models.CharField(max_length=50, blank=True, null=True)
  age = models.IntegerField(blank=True, null=True)

  def serialize(self):
    return {
      'user': self.user.__dict__, # user.serialize(),
      'name': self.name,
      'age': self.age
    }