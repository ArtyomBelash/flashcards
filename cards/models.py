from django.db import models

NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)


class Card(models.Model):
    question = models.CharField(verbose_name='Вопрос', max_length=100)
    answer = models.CharField(verbose_name='Ответ', max_length=100)
    box = models.IntegerField(
        verbose_name='Коробка',
        choices=zip(BOXES, BOXES),
        default=BOXES[0],
    )
    date_created = models.DateTimeField(verbose_name='Дата', auto_now_add=True)

    def __str__(self):
        return self.question

    def move(self, solved):
        new_box = self.box + 1 if solved else BOXES[0]
        if new_box in BOXES:
            self.box = new_box
            self.save()

        return self
