from django.shortcuts import render,redirect

from django.http import HttpResponse ,JsonResponse

def index_page(request):
    # return render(request,'web/index.html')
    return render(request,'index.html')

def account_page(request):
    return render(request,'my-account.html')

def contact_page(request):
    return render(request,'contact.html')