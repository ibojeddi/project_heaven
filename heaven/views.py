from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Cemetery, Burial
from .forms import CemeteryForm, BurialForm, UserProfileForm, UserForm
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.views import login, logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    return render(request,'heaven/home.html')

def cemetery(request):
    return render(request, 'heaven/base_cemetery.html', {})

# -------- Cemetery ----------
@login_required
def add_cemetery(request):
    if request.method=='POST':
        form=CemeteryForm(request.POST)

        if form.is_valid():
            cemetery=form.save(commit=False)
            cemetery.name=request.POST.get('name')
            cemetery.city=request.POST.get('city')
            cemetery.zipcode=request.POST.get('zipcode')
            cemetery.latitude=request.POST.get('latitude')
            cemetery.longitude=request.POST.get('longitude')
            cemetery.date_created=timezone.now()
            if request.user.is_authenticated:
                cemetery.created_by=request.user
            else:
                return login(request)
            #cemetery_obj=Cemetery(name=name, city=city,zipcode=zipcode,created_by=created_by)
            cemetery.save()
            return redirect('view_cemetery')
    else:
        form=CemeteryForm
    return render(request,'heaven/add_cemetery.html',{'form':form})

def view_cemetery(request):
    cemeteries=Cemetery.objects.filter(date_created__lte=timezone.now()).order_by('date_created')
    return render(request, 'heaven/view_cemetery.html', {'cemeteries':cemeteries})

def view_cemetery_details(request,pk):
    cemetery=get_object_or_404(Cemetery,pk=pk)
    return render(request, 'heaven/view_cemetery_details.html', {'cemetery':cemetery})

def edit_cemetery(request):
    return render(request, 'heaven/edit_cemetery.html', {})

def delete_cemetery(request):
    return render(request, 'heaven/delete_cemetery.html', {})

# -------- Burial ----------

def burial(request):
    return render(request, 'heaven/base_burial.html', {})

def add_burial(request):
    if request.method=="POST":
        form=BurialForm(request.POST)
        if form.is_valid():
            #create an instance of Cemetery

            burial=form.save(commit=False)
            burial.cemetery_id=Cemetery.objects.get(id=request.POST.get('cemetery_id'))
            burial.first_name=request.POST.get('first_name')
            burial.DoB=form.cleaned_data.get('DoB')
            burial.DoD=form.cleaned_data.get    ('DoD')
            burial.sex=request.POST.get('sex')
            burial.latitude=request.POST.get('latitude')
            burial.longitude=request.POST.get('longitude')
            burial.date_created=request.POST.get('date_created')
            if request.user.is_authenticated:
                burial.created_by=request.user
            else:
                return login(request)
            burial.save()
            return redirect('view_burial')
    else:
        form=BurialForm
    return render(request,'heaven/add_burial.html',{'form':form})


def view_burial(request):
    burials=Burial.objects.filter(date_created__lte=timezone.now()).order_by('date_created')
    return render(request, 'heaven/view_burial.html', {'burials':burials})

def view_burial_details(request,pk):
    burial=get_object_or_404(Burial,pk=pk)
    return render(request, 'heaven/view_burial_details.html', {'burial':burial})

def edit_burial(request):
    return render(request, 'heaven/edit_burial.html', {})

def delete_burial(request):
    return render(request, 'heaven/delete_burial.html', {})

#---------- Photo ------------

def photo(request):
    return render(request, 'heaven/base_photo.html', {})

def add_photo(request):
    return render(request,'heaven/add_photo.html')

def view_photo(request):
    return render(request, 'heaven/view_photo.html')

def edit_photo(request):
    return render(request, 'heaven/edit_photo.html', {})

def delete_photo(request):
    return render(request, 'heaven/delete_photo.html', {})

#------ add ----------
def add(request):
    return render(request, 'heaven/base_add.html', {})

def view(request):
    return render(request, 'heaven/base_view.html', {})

def edit(request):
    return render(request, 'heaven/base_edit.html', {})

def delete(request):
    return render(request, 'heaven/base_delete.html', {})


#-------------- Register ------------------
def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print (user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,'heaven/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context)

    ''' render_to_response was removed from django's newer versions, this function was used in tango with django
    return render_to_response(
            'heaven/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)'''

#--------------- Login ---------------------
def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            #print ("Invalid login details.") # "Invalid login details: {0}, {1}".format(username, password)
            return render(request,'heaven/login.html', {'credentials':'invalid'})
            #return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request,'heaven/login.html',)

#------------------ Logout ----------------------
# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')