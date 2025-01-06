from django.views import generic


class Home(generic.TemplateView):
    template_name = 'adult/home.html'