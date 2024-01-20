from django.shortcuts import render,HttpResponse

# Create your views here.


def home (request):
   try:
     name=request.session['Name']
     return render(request,'app/home.html',{'data':name})
   except:
      return render(request,'app/home.html')


def singup(request):
   return render(request,'app/singup.html')
def product(request):
    try:
     name=request.session['Name']
     return render(request,'app/product.html',{'data':name})
    except:
      return render(request,'app/product.html')
  

def about(request):
    try:
     name=request.session['Name']
     return render(request,'app/about.html',{'data':name})
    except:
      return render(request,'app/about.html')
   
def contact(request):
   return render(request,'app/contact.html')
def award(request):
   return render(request,'app/awrad.html')

def savedata(request):
   name=request.POST['nm']
   email=request.POST['em']
   password=request.POST['pass1']
   repassword=request.POST['pass2']
   request.session['Name']=name
   request.session['Email']=email
   request.session['Password']=password
   request.session['Repasswaord']=repassword
   return render(request,'app/login.html')



def login(req):
   
   return render (req,'app/login.html')

def register(request):
   email=request.POST['em']
   password=request.POST['pass']
   try:
      emailid=request.session['Email']
      password=request.session['Password']
      if email==emailid and password==password:
         name=request.session['Name']
         request.session.modified =True
         return render(request,'app/dashbord.html',{'data':name})
      else:
         return HttpResponse("<h1>*********** SESSION WILL BE EXPIRE********************D</h1>")
   except: 
     msg='!! session will be expierd !!'
     return render(request,'app/home.html' ,{'see':msg})

def dashbord(req):
   return render(req,'app/dashbord.html')
   
def logout(request):
    del request.session['Name']
    del request.session['Email']
    del request.session['Password']
    del request.session['Repasswaord']
    request.session.flush()
    return render(request, 'app/home.html') 
