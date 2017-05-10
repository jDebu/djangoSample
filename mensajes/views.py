from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import FormView
import requests,json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import Services

from django.contrib import messages
from mensajes import forms,models
from .multiple_forms import MultipleFormsView


class TestView(APIView):

    def call_api(self, request, *args, **kwargs):
        headers = {}
        url = 'http://jsonplaceholder.typicode.com/users/'+ self.kwargs['pk']
        method = request.method.lower()
        method_map = {
            'get': requests.get,
            'post': requests.post,
            'put': requests.put,
            'patch': requests.patch,
            'delete': requests.delete
        }
        return Response(method_map[method](url, headers=headers, data=json.dumps(request.data)).json())

    def get(self, request, *args, **kwargs):
        return self.call_api(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.call_api(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.call_api(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.call_api(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.call_api(request, *args, **kwargs)

class IndexView(MultipleFormsView):
    template_name = 'mensajes/index.html'
    success_url = '/mensajes/'
    forms_classes = [
        forms.DniForm,
        forms.NameForm
    ]


    def form_valid(self, form):
        messages.success(self.request, "Submitted {}".format(form.__class__.__name__))
        #print(self.request.POST['dni'])
        if isinstance(form, forms.DniForm):
            s=Services()
            print(self.request.POST['dni'])
            data=s.get_data_dni(self.request.POST['dni'])
            if data:
                print(data['Nombres']) 
                form=forms.NameForm({'names':data['Nombres'],'last_names':data['ApellidoP']})   
                print(form)
                return super(IndexView, self).form_valid(form)
        return super(IndexView, self).form_valid(form)



def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        
        print request.POST
        if 'names' in request.POST:
            print('names present')
            formDni = forms.DniForm({'dni':request.POST['dni_']})
            formName=forms.NameForm(request.POST)
            if formName.is_valid():
                paciente=models.Paciente(dni=request.POST['dni_'],nombres=request.POST['names'],apellidos=request.POST['last_names'])
                paciente.save()  

        if 'dni' in request.POST:
            print('dni present')
            formDni = forms.DniForm(request.POST)
            # check whether it's valid:
            if formDni.is_valid():
                s=Services()
                data=s.get_data_dni(request.POST['dni'])
                if data:
                    formName=forms.NameForm({'dni_':request.POST['dni'],'names':data['Nombres'],'last_names':data['ApellidoP']+' '+data['ApellidoM']})
                else:
                    formName = forms.NameForm()

            #return render(request, 'mensajes/index2.html', {'formName': formName, 'formDni': formDni})
        '''
        if  request.POST['names'] :
            print(request.POST['dni'])
            print(request.POST['names'])
            print(request.POST['last_names'])'''
            #return HttpResponseRedirect('/mensajes/')
    else:
        formName = forms.NameForm()
        formDni = forms.DniForm()
    
    return render(request, 'mensajes/index2.html', {'formName': formName, 'formDni': formDni})

