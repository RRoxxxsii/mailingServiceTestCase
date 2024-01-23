from django.db.models import Q, QuerySet

from .models import Client, Mailing


class MailingCRUD:
    @staticmethod
    def get_by_id(id_: int) -> Mailing | None:
        try:
            mailing = Mailing.objects.get(pk=id_)
        except Mailing.DoesNotExist:
            return None
        else:
            return mailing

    @staticmethod
    def get_all() -> QuerySet[Mailing]:
        return Mailing.objects.all()

    @staticmethod
    def create(**kwargs) -> Mailing:
        mailing = Mailing.objects.create(**kwargs)
        return mailing


class ClientCRUD:
    @staticmethod
    def filter_on_tag_and_mobile_operator_code(tag: str, mobile_operator_code: str) -> QuerySet[Client]:
        clients = Client.objects.filter(Q(tag=f"{tag}") & Q(mobile=f"{mobile_operator_code}"))
        return clients
