from random import randint
from django.forms import EmailField
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import *
from django.conf import settings
from django.core.mail import send_mail

default_data = {
    'app_name': 'Expenses Manager',
}

def index(request):
    return render(request, 'index.html', default_data)

def signup_page(request):
    return render(request, "signup_page.html", default_data)

def signin_page(request):
    return render(request, "signin_page.html", default_data)

def otp_page(request):
    return render(request, "otp_page.html", default_data)

def expenses_page(request):
    load_expenses(request) # calling a method to load expenses data
    return render(request, "expenses_page.html", default_data)

def profile_page(request):
    if 'email' in request.session:
        profile_data(request) # calling a method to load profile data
        return render(request, "profile_page.html", default_data)
    return redirect(signin_page)

# serialize data
def serialize_data(obj):
    object = {}
    source_dict = obj.__dict__
    for o in source_dict:
        if o.startswith('_') or o.endswith('_') or (o.startswith('_') and o.endswith('_')):
            # object.pop(o)
            continue
        object.setdefault(o, source_dict[o])
    # print(object)
    return object

# load profile data
def profile_data(request):
    master = Master.objects.get(Email = request.session['email'])
    profile = Profile.objects.get(Master = master)

    sd = serialize_data(profile)

    print('serialized data:', sd)

    print(gender_choices)
    genders = []
    for gc in gender_choices:
        genders.append(
            {'short_text': gc[0], 'text': gc[1]}
        )

    print(genders)

    default_data['gender_choices'] = genders
    default_data['profile_data'] = sd

# profile update functionality
def profile_update(request):
    master = Master.objects.get(Email = request.session['email'])
    profile = Profile.objects.get(Master = master)

    profile.FullName = request.POST['full_name']
    profile.Mobile = request.POST['mobile']
    profile.Gender = request.POST['gender']
    profile.State = request.POST['state']
    profile.City = request.POST['city']
    profile.Address = request.POST['address']

    profile.save()

    
    # return redirect(profile_page)
    profile_data(request)
    return JsonResponse(default_data)

# load all expenses
def load_expenses(request):
    master = Master.objects.get(Email = request.session['email'])
    profile = Profile.objects.get(Master = master)

    all_expenses = Expense.objects.filter(Profile = profile)
    default_data['all_expenses'] = all_expenses

# create otp
def create_otp(request):
    email_to_list = [request.session['reg_data']['email'],]

    from_email = settings.EMAIL_HOST_USER

    otp = randint(1000, 9999)
    request.session['otp'] = otp

    subject = "OTP verification"
    message = f"OTP Verification for ExpenseManager: {otp}"

    send_mail(subject, message, from_email, email_to_list)

# otp verification
def otp_verify(request):
    if request.POST:
        otp = int(request.POST['otp'])

        if otp == request.session['otp']:
            master = Master.objects.create(
                Email = request.session['reg_data']['email'],
                Password = request.session['reg_data']['password'],
                IsActive = True
            )

            Profile.objects.create(Master=master)

            print('account verified successfully.')

            del request.session['reg_data']
            del request.session['otp']
        else:
            print('invalid otp')
            return redirect(otp_page)

        return redirect(signin_page)

    else:
        print('invalid method')

    return redirect(otp_page)

# signup functionality
def signup(request):
    print('sigup data', request.POST)

    request.session['reg_data'] = {
        'email': request.POST['email'],
        'password': request.POST['password']
    }

    create_otp(request) # calling method
    

    
    
    return redirect(otp_page)

# signin functionality
def signin(request):
    print('sigin data', request.POST)

    if request.POST:
        master = Master.objects.get(Email = request.POST['email'])

        if master.Password == request.POST['password']:
            request.session['email'] = master.Email
            return redirect(profile_page)
        else:
            print('incorrect password')
    else:
        print('invalid method')
    
    return redirect(signin_page)

def signout(request):
    if 'email' in request.session:
        del request.session['email']
    return redirect(signin_page)