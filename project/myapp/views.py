from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing(req):
    return render(req,'landing.html')

def register(req):
    print("hello......")
    print(req.POST)
    print(req.FILES)
    if req.method=='POST':
        n = req.POST.get('name')
        e = req.POST.get('email')
        p = req.POST.get('password')
        cp = req.POST.get('cpassword')
        i = req.FILES.get('image')
        a = req.FILES.get('audio')
        v = req.FILES.get('video')
        d = req.FILES.get('resume')
        print(n,e,p,cp,i,a,v,d,sep=',')
    return render(req,'register.html' )
