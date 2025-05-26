from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def contact(request):
    if request.method == 'POST':
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        # send email to this email
        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )


    return render(request,'contact/contact.html',{})
