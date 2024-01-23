from django.db import models


class Mailing(models.Model):
    message = models.TextField("Текст")
    filter = models.JSONField("Фильтр клиента")

    started_at = models.DateTimeField("Начало")
    finished_at = models.DateTimeField("Окончание")

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"

    def __str__(self):
        return self.message


class Client(models.Model):
    mobile = models.CharField("Номер телефона", max_length=11, unique=True)
    mobile_operator_code = models.CharField("Код мобильного оператора")
    tag = models.CharField("Метка", null=True, blank=True)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return self.mobile


class Message(models.Model):
    created_at = models.DateTimeField("Время отправки", auto_now_add=True)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name="messages")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="clients")

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return self.client
