from django.urls import path , include
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name="blog"


urlpatterns = [
    path('fbv-index/',views.IndexViewf,name='fbv-index'),
    path('cbv-index/', TemplateView.as_view(template_name="index.html",extra_context={"name":"Masoud"})),
    path('cbv-index/',views.IndexView.as_view(),name='cbv-index'),
    path('test/', RedirectView.as_view(url='https://www.djangoproject.com/'), name='go-to-django'),
    path('create/',views.ContactFormView.as_view(),name='contact-form-view'),
    # path('post/',views.api_list_view,name='api_list_view'),
    path('api/v1/', include('blog.api.v1.urls')),
]



