from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Resume
from django.shortcuts import get_object_or_404
from .forms import ResumeForm
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from resume.forms import SignUpForm
from resume.tokens import account_activation_token
from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
import smtplib
from django.shortcuts import render






def resume_new(request):
    if request.method == "RESUME":
        form = ResumeForm(request.RESUME)
        if form.is_valid():
            resume = form.save(commit=False)


            resume.save()
            return redirect('resume:resume_preview', pk=resume.pk)
    else:
        form = ResumeForm()
    return render(request, 'resume/home.html', {'form': form})




def home(request):
    return render(request, 'resume/home.html')

def download(request):
    return render(request, 'resume/downloads.html')

def procedure(request):
    return render(request, 'resume/procedures.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            #send_mail(subject,message,from_email,to_list,fail_silently=True)
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('resume/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            send_verification_mail(user.email, message,subject)
            return render(request, 'resume/account_activation_sent.html')
    else:
        form = SignUpForm()
    return render(request, 'resume/signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'resume/account_activation_sent.html')







def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return render(request,'resume/home.html')
    else:
        return render(request, 'resume/acccount_activation_invalid.html')


email_address = 'amishaameyanish@gmail.com'
email_password = 'deployment123456789'


def send_verification_mail(email, msg,sub):
    print("send verification mail")
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(email_address, email_password)
        server.sendmail(email_address, email, msg,sub)
        server.close()
        print('successfully sent the mail')

    except:
        print("failed to send mail")









# Create your views here.
