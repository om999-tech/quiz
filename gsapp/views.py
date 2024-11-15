from django.shortcuts import render
from django.http import HttpResponse

def Regiser_user(request):
    return render(request,'register_user.html')


def save_std_details(request):
    if request.method =='POST':
        name = request.POST.get('name')        
        father_name = request.POST.get('father_name')        
        mobile_no = request.POST.get('mobile_no')       
        email = request.POST.get('email')        
        address = request.POST.get('address')        
        return HttpResponse('ok')