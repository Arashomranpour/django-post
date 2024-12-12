from django.shortcuts import render,redirect
from .forms import RegisterForm,PostForm
from django.contrib.auth import login,logout,authenticate
from .models import post
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import permission_required,login_required
from django.contrib import messages

# from .tokens import account_act_token
# from django.template.loader import render_to_string
# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
# from django.utils.encoding import force_bytes,force_str
# from django.core.mail import EmailMessage
# from django.contrib.auth import get_user_model

# def activateview(request,uidb64,token):
#     User=get_user_model()
#     try:
#         uid=force_str(urlsafe_base64_decode(uidb64))
#         user=User.objects.get(pk=uid)
#     except:
#         user=None
#     if user is not None and account_act_token.check_token(user,token):
#         user.is_active=True
#         user.save()
#         messages.success(request,"Done you can login now")
#         return redirect("login")
#     else:
#         messages.error(request,"not activated")
#     return redirect("/home")



# def activateEmail(request,user,to_email):
    
#     mail_subject="activate"
#     message=render_to_string("email_template.html",
#                              {"user":user.username, 
#                             'domain':get_current_site(request).domain,
#                             "uid":urlsafe_base64_encode(force_bytes(user.pk)),
#                             "token":account_act_token.make_token(user),
#                             "protocol":"https" if request.is_secure() else "http"})
    
    
#     email=EmailMessage(mail_subject,message,to=[to_email])
#     if email.send():
    
#         messages.success(request,f"dear {user} please check your {to_email} email inbox if there was not activation link check your spam folder")
#     else:
#         messages.error(request,"problem in email server")


@login_required(login_url="/login")
def home(request):
    
    all_post=post.objects.all()
    
    if request.method=="POST":
        user_id=request.POST.get("user_id")
        post_id = request.POST.get('post_id')
        # print(user_id)
        if post_id:
            Dpost=post.objects.filter(id=post_id).first()
            if Dpost and (Dpost.author==request.user or request.user.has_perm("post_module.delete_post")):
                Dpost.delete()
        elif user_id:
            user=User.objects.filter(id=user_id).first()
            
            if user and request.user.is_staff:
                try:
                    group=Group.objects.filter(user=user)
                    
                    for g in group:
                        g.user_set.remove(user)
                        print("banned")
                  
               
                except:
                    pass
    
    context={"all_post":all_post}
    return render(request,"post_module/hello.html" ,context)

def sign_up(request):
    if request.method=="POST":
        form =RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            # user.is_active=False
            # user.save()
            # activateEmail(request.user,form.cleaned_data.get("email"))
            
        
            login(request=request,user=user)
            return redirect("/home")
            
    else:
        form=RegisterForm()
    return render(request,"registration/sign_up.html",{"form":form})




def LogOut(request):
    logout(request)
    return redirect("/login/")




@login_required(login_url="/login")
@permission_required("post_module.add_post",login_url="login",raise_exception=True)
def createpost(request):
    if request.method == "POST":
        form =PostForm(request.POST)
        
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect("/home")

    else:
        form=PostForm()
    return render(request,"post_module/createpost.html",{"form":form})
