from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=255, verbose_name='Вопрос')
    pub_date = models.DateField(auto_now_add=True,verbose_name='Дата публикации')

    class Mete:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return f'Вопрос:{self.question_text}'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=255, verbose_name='Вариант ответа')
    votes = models.IntegerField(default=0)

    class Mete:
        verbose_name = 'Response'
        verbose_name_plural = 'Responses'

    def __str__(self):
        return f'Name of choice:{self.choice_text}'


class Item(models.Model):
    name = models.CharField(max_length=30, verbose_name='Наименование товара')
    price = models.IntegerField(verbose_name='Цена товара')

    def __str__(self):
        return f'Name of item:{self.name} - Price:{self.price}'


class Purchase(models.Model):
    name = models.CharField(max_length=30,verbose_name='ФИО клиента')
    age = models.IntegerField(verbose_name='Возраст клинта')
    item = models.ForeignKey(Item,on_delete=models.CASCADE,related_name='purchases')
    date_purchase = models.DateField(verbose_name='Дата покупки')

    def __str__(self):
        return f'Name of purchase:{self.name} - age:{self.age} - date_purchase:{self.date_purchase}'



