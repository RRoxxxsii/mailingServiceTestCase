from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from mailing.db.crud import MailingCRUD
from .serializers import MailingSerializer
from ..services.tasks import start_mailing


class CreateMailingAPIView(CreateAPIView):
    serializer_class = MailingSerializer
    queryset = MailingCRUD.get_all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        message = serializer.data.get('message')
        filter_ = serializer.data.get('filter')
        started_at = serializer.data.get('started_at')
        finished_at = serializer.data.get('finished_at')

        mailing = MailingCRUD.create(message=message, filter=filter_, started_at=started_at, finished_at=finished_at)
        start_mailing.apply_async(args=[mailing.pk], eta=mailing.started_at)

        serializer = MailingSerializer(mailing)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class ListMailingAPIView(ListAPIView):
    serializer_class = MailingSerializer
    queryset = MailingCRUD.get_all()

