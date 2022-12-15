from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import ContactForm

# Create your views here.
def IndexViewf(request):
    """
    a functions for view test
    """
    return render(request,'index.html',{})



class IndexView(TemplateView):
    """
    class Based View show index page
    """

    template_name= 'index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name']="reza"
        return context

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/blog/cbv-index/'


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


