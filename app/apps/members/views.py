from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import AddCar as AddCarForm


class AddCarView(FormView):
    template_name = "add_car/index.html"
    success_url = reverse_lazy("add-car")
    form_class = AddCarForm

    def form_valid(self, form):
        self.object = form.save(user=self.request.user)
        return super().form_valid(form)
