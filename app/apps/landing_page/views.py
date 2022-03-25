import json
import logging

from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from .forms import Contact

from apps.kafka import producer


logger = logging.getLogger(__name__)


class LandingPageView(TemplateView):
    template_name = "landing_page/index.html"


def process_message_to_kafka(msg_dict):
    producer.produce(
            "customer-platform-contact-form",
            json.dumps(msg_dict).encode()
        )
    producer.flush()
    logger.info(
        f"Contactform sent to kafka topic `customer-platform-contact-form` with msg {msg_dict}"
    )
    


@require_http_methods(["POST", ])
def contact_view(request):
    form = Contact(request.POST)
    logger.info("Contactform received from website")
    if form.is_valid():
        json_message = {
            "type": form.cleaned_data['type'],
            "message": form.cleaned_data['message'],
            "email": form.cleaned_data['email']
        }
        process_message_to_kafka(json_message)
        logger.info(
            f"Contactform sent to kafka topic `customer-platform-contact-form` with msg {json_message}"
        )

    return HttpResponseRedirect(reverse('landing-page'))


class FormApi(CreateAPIView):
    def post(self, request, *args, **kwargs):
        logger.info("Contactform received from api")
        process_message_to_kafka(request.data)
        return Response(status=status.HTTP_201_CREATED)
