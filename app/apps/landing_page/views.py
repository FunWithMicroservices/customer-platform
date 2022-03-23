import json

from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from .forms import Contact

from apps.kafka import producer


class LandingPageView(TemplateView):
    template_name = "landing_page/index.html"


@require_http_methods(["POST", ])
def contact_view(request):
    form = Contact(request.POST)
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

    return HttpResponseRedirect(reverse('landing-page'))
