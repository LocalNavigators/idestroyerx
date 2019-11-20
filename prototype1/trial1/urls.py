from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns=[
        path('',views.SingleFile,name='home'),
        #path('genrep/',views.genrep,name='genrep')
        path('newsun', TemplateView.as_view(template_name="newsun.html"),
                   name='testgame'),
        path('bubble', TemplateView.as_view(template_name="bubble.html"),
                   name='bubble'),
        path('stopwords',TemplateView.as_view(template_name="stopwords.html"),
        		name='stopwords'),
        path('genric',TemplateView.as_view(template_name="genric.html"),
        		name='genric')
        ]