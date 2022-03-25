import json
import logging

from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from .forms import Contact

from apps.kafka import producer


logger = logging.getLogger(__name__)


class LandingPageView(TemplateView):
    template_name = "landing_page/index.html"


@require_http_methods(["POST", ])
def contact_view(request):
    form = Contact(request.POST)
    logger.info("Contactform received")
    if form.is_valid():
        json_message = {
            "type": form.cleaned_data['type'],
            "message": form.cleaned_data['message'],
            "email": form.cleaned_data['email']
        }
        producer.produce(
            "customer-platform-contact-form",
            json.dumps(json_message).encode()
        )
        producer.flush()
        logger.info(
            f"Contactform sent to kafka topic `customer-platform-contact-form` with msg {json_message}"
        )

    return HttpResponseRedirect(reverse('landing-page'))
