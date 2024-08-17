from django.contrib.auth import get_user_model
from django.db import models

user = get_user_model()

NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)


class CardManager(models.Manager):
    def get_cards_by_owner(self, user_id):
        owner = user_id
        return self.filter(owner=owner)


class Card(models.Model):
    question = models.CharField(verbose_name='Вопрос', max_length=100)
    answer = models.CharField(verbose_name='Ответ', max_length=100)
    box = models.IntegerField(
        verbose_name='Коробка',
        choices=zip(BOXES, BOXES),
        default=BOXES[0],
    )
    date_created = models.DateTimeField(verbose_name='Дата', auto_now_add=True)
    owner = models.ForeignKey(user, on_delete=models.CASCADE, verbose_name='Владелец')
    objects = CardManager()

    def move(self, solved):
        new_box = self.box + 1 if solved else BOXES[0]
        if new_box in BOXES:
            self.box = new_box
            self.save()
        return self

    def __str__(self):
        return self.answer

    class Meta:
        ordering = ['box']
