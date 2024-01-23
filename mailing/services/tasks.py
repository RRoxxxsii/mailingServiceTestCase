from datetime import datetime

from celery import shared_task

from mailing.db.crud import ClientCRUD, MailingCRUD
from mailing.services.service import send_message


@shared_task
def start_mailing(mailing_id: int) -> None:
    mailing = MailingCRUD.get_by_id(mailing_id)
    if not mailing:
        return None

    clients = ClientCRUD.filter_on_tag_and_mobile_operator_code(
        tag=mailing.filter.get("tag"), mobile_operator_code=mailing.filter.get("mobile_operator_code")
    )
    if not clients:
        return None
    for _ in clients:
        current_datetime = datetime.now()
        if mailing.started_at < current_datetime < mailing.finished_at:
            send_message(mailing.message)
        else:  # Если не успели разослаться все сообщения - выход из ф-ции
            break
