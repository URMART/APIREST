from django.views import View
from django.http.response import JsonResponse
from .models import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

class CompanieView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,id=0):
        
        if id > 0:

            companies=list(Company.objects.filter(id = id).values())
            if len(companies) > 0:
                company=companies[0]
                datos={'message':'success', 'company':company}
            else:
                datos={'message':'company not found'} 
            return JsonResponse(datos)

        else:
            companies=list(Company.objects.values())
            if len(companies) > 0:
                datos={'message':'success', 'companies':companies}
            else:
                datos={'message':'company not found'} 
            return JsonResponse(datos)     

    def post(self, request):

        jd= json.loads(request.body)
        Company.objects.create(name=jd['name'], website=jd['website'],function=jd['function']) 

        datos={'message':'success'}

        return JsonResponse(datos)

    def put(self, request,id):
        jd= json.loads(request.body)
        companies=list(Company.objects.filter(id = id).values())

        if len(companies) > 0:
            company=Company.objects.get(id=id)
            company.name=jd['name']
            company.website=jd['website']
            company.function=jd['function']
            company.save()
            datos={'message':'success'}
        else:

            datos={'message':'company not found'} 

        return JsonResponse(datos)    

    def delete(self, request,id):
        companies=list(Company.objects.filter(id = id).values())

        if len(companies) > 0:
            company=Company.objects.get(id=id)
            company.delete()
            datos={'message':'success'}
        else:    
            datos={'message':'company not found'}

        return JsonResponse(datos)    