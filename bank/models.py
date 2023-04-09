from django.db import models


class TestResult(models.Model):
    date = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    ip = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    test = models.ForeignKey(TestResult, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.ip


class Test(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TrainingWay(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()  # требования
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.CharField(max_length=255)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    detailed = models.BooleanField(default=False)  # развернутый или нет

    def __str__(self):
        return self.name


class Variant(models.Model):
    variant = models.CharField(max_length=255)
    is_right = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='variants')


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    test = models.ForeignKey(TestResult, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField(null=True)
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    training_way = models.ForeignKey(TrainingWay, on_delete=models.CASCADE, verbose_name='направление')
    name = models.CharField(max_length=255, verbose_name='имя')
    surname = models.CharField(max_length=255, verbose_name='фамилия')
    patronymic = models.CharField(max_length=255, verbose_name='отчество', null=True)
    birthday = models.DateField(verbose_name='дата рождения', null=True)
    birthday_place = models.CharField(max_length=255, verbose_name='место рождения', null=True)
    number = models.PositiveBigIntegerField(verbose_name='номер телефона', null=True)
    email = models.EmailField(verbose_name='почта', null=True)
    start_practice = models.DateField(verbose_name='дата начала практики', null=True)
    end_practice = models.DateField(verbose_name='дата конца пркатики', null=True)

