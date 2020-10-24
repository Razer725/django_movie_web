from django.db import models


class Contact(models.Model):
    """Форма подписки по email"""
    email = models.EmailField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.email


