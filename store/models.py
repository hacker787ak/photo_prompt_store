from django.db import models
from django.contrib.auth.models import User

class PromptItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='prompts/')
    prompt_text = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=2.00)

    def __str__(self):
        return self.title

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prompt_item = models.ForeignKey(PromptItem, on_delete=models.CASCADE)
    utr_number = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
