from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Post(models.Model):
    """Blog post modeli."""
    
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name=_("Muallif")
    )
    title = models.CharField(
        max_length=100,
        verbose_name=_("Sarlavha")
    )
    body = models.TextField(
        verbose_name=_("Matn")
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Yaratilgan sana")
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=_("O'zgargan sana")
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Post")
        verbose_name_plural = _("Postlar")

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self) -> str:
        return reverse("posts:detail", kwargs={"pk": self.pk})