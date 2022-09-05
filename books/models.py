from django.conf import settings
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

User = settings.AUTH_USER_MODEL


class Book(models.Model):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=128,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='books',
    )
    publication_date = models.DateField(
        verbose_name=_('Дата добавления'),
        default=now,
    )
    annotation = models.TextField(
        verbose_name=_('Аннотация'),
        max_length=1024,
    )

    class Meta:
        ordering = ('title',)
        verbose_name = _('Книга')
        verbose_name_plural = _('Книги')

    def __str__(self):
        return self.title
