from rest_framework import serializers

from mailing.db.models import Mailing


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = "__all__"
