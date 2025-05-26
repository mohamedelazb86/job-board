from django.shortcuts import render,redirect
from .forms import SignForm,ActivateForm
from django.core.mail import send_mail
from .models import Profile
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import ProfileForm




def signup(request):
    '''
     - create new user
     - send email to this
     - stop active this user
     - return rediect activate html
    '''
    if request.method=='POST':
        form=SignForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            user=form.save(commit=False)
            user.is_active=False
            form.save()  # create new user and create new profile
            profile=Profile.objects.get(user__username=username)

            # send email to this user
            send_mail(
            "Activate Code",
            f"Welcome Mr {username}\n pls use this code {profile.code}",
            "r_mido99@yahoo.com",
            [email],
            fail_silently=False,
        )
            # return redirect(f'/accounts/activate_code/{username}')
            return redirect(reverse('accounts:activate-code', args=[username]))
           


    else:
        form=SignForm()
    return render(request,'accounts/signup.html',{'form':form})

def activate_code(request,username):
    '''
     - get code if this code == profile code
     -  active this code
     -  rediect login
    '''
    profile=Profile.objects.get(user__username=username)
    if request.method=='POST':
        form=ActivateForm(request.POST)
        if form.is_valid():
            code=form.cleaned_data['code']
            if code == profile.code:
                profile.code =''

                user=User.objects.get(username=username)
                user.is_active=True
                user.is_staff=True
                user.save()

                profile.save()

                return redirect('/accounts/login')
                

    else:
        form=ActivateForm()

    return render(request,'accounts/activate_code.html',{'form':form})

def profile(request):
    profile=Profile.objects.get(user=request.user)

    context={
        'profile':profile
    }
    return render(request,'accounts/profile.html',context)

def edit_profile(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form=form.save(commit=False)
            form.user=request.user
            form.save()
            return redirect('/accounts/profile')
    else:
        form=ProfileForm(instance=profile)
    return render(request,'accounts/edit_profile.html',{'form':form})