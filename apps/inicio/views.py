from django.shortcuts import render_to_response
from django.views.generic import TemplateView

class index(TemplateView):
	template_name='inicio/index.html'


class index2(TemplateView): #Hereda todo lo que tiene TemplateView
	template_name='inicio/index2.html'