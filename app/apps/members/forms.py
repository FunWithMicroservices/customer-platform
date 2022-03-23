from django.forms import ModelForm
from .models import Car


class AddCar(ModelForm):
    class Meta:
        model = Car
        fields = ("brand", "type", )

    def save(self, user, *args, **kwargs):
        instance = super(AddCar, self).save(commit=False, **kwargs)
        instance.user = user
        instance.save()
        return instance
