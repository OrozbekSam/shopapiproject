from django.db import models
from product.models import NewProduct
from django.contrib.auth import get_user_model

User = get_user_model()


class Mark():
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5

    marks = (
        (one, 'Очень лохо!'),
        (two, 'Плохо'),
        (three, 'Удовлетворительно!'),
        (four, 'Хорошо!'),
        (five, 'Отлично!'),
    )


class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    product = models.ForeignKey(NewProduct, on_delete=models.CASCADE, related_name='ratings')
    mark = models.PositiveSmallIntegerField(choices=Mark.marks)

    def __str__(self):
        return f'{self.mark} -> {self.product}'

    class Meta:
        unique_together = ('owner', 'product')
