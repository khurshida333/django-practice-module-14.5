from django.shortcuts import render,redirect
from .forms import DoctorForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
# Create your views here.

#Rendering Django forms in HTML templates


def contact(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            # Define the subject of the email
            subject = "Contact"  # This is the subject of the email

            # Define the message body of the email
            body = {
                'name': form.cleaned_data['name'],  # Get the first name from the form
                'email': form.cleaned_data['email'],  # Get the email address from the form
                'message': form.cleaned_data['message'],  # Get the message from the form
            }
            # Create the message by joining the values of the body dictionary with newline characters
            message = "\n".join(body.values())

            try:
                # Try to send the email with the subject and message to the specified email addresses
                send_mail(subject, message, 'admin@gmail.com', ['admin@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            # Redirect to the homepage upon successful submission
            return redirect("contact")

    # If the request method is not POST, display an empty form
    form = DoctorForm()
    return render(request, "contact.html", {'form': form})


# def FirstApp(request):
#     if request.method == 'POST':
#         form = forms.DoctorForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('first_app')
#         else:
#             print(form.errors)  # Add this line to print form errors
#     else:
#         form = forms.DoctorForm()
#         return render(request, 'home.html',{'form': form})