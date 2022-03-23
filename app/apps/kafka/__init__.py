from django.conf import settings
from confluent_kafka import Producer

producer = Producer(**{
    "bootstrap.servers": settings.KAFKA_HOST
})
