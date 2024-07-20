from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    passport_serial_number = models.CharField(max_length=9, unique=True)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()
    correct_answer = models.IntegerField(blank=True, null=True)
    wrong_answer = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    is_calling = models.BooleanField(default=False)
    received_a_certificate = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        ordering = ['-created_time']

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # def __str__(self):
    #     return self.full_name
