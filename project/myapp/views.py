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
        i = req.FILES.get('profile')
        a = req.FILES.get('audio')
        v = req.FILES.get('video')
        d = req.FILES.get('resume')
        e = req.POST.get('email')
        p = req.POST.get('password')
        cp = req.POST.get('cpassword')
        g = req.POST.get('gender')
        s = req.POST.get('state')
        q = req.POST.getlist('qualification')
        print(n,e,p,cp  ,i,a,v,d,g,q,s,sep=',')
        response=render(req,'login.html')
        response.set_cookie('name',n)
        response.set_cookie('profile',i)
        response.set_cookie('audio',a)
        response.set_cookie('video',v)
        response.set_cookie('resume',d)
        response.set_cookie('email',e)
        response.set_cookie('password',p)
        response.set_cookie('cpassword',cp)
        response.set_cookie('gender',g)
        response.set_cookie('state',s)
        response.set_cookie('qualification',q)
        return response
    else:
        return render(req,'register.html')
def login(req):
    return render(req,'login.html')

def get_cookie(req):
    print(req.COOKIES)
    n=req.COOKIES.get('name')
    i=req.COOKIES.get('profile')
    a=req.COOKIES.get('audio')
    v=req.COOKIES.get('video')
    d=req.COOKIES.get('resume')
    e=req.COOKIES.get('email')
    p=req.COOKIES.get('password')
    cp=req.COOKIES.get('cpassword')
    g=req.COOKIES.get('gender')
    s=req.COOKIES.get('state')
    q=req.COOKIES.get('qualification')
    print(n,e,p,cp,i,a,v,d,g,q,s,sep=',')