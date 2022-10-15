from main.models import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
import smtplib
from django.views.decorators.csrf import csrf_exempt


def index2(request):
	data = {'disciplines': Discipline.objects.all(), 
			'services': Service.objects.all(), 
			'educations': Education.objects.all(),
			'additions': Addition.objects.all(), 
			'partners': Partner.objects.all()}

	return render(request, 'index.html', data)


@csrf_exempt
def index(request):
	data = {'disciplines': Discipline.objects.all(), 
			# 'services': Service.objects.all(), 
			# 'educations': Education.objects.all(),
			# 'additions': Addition.objects.all(), 
			'partners': Partner.objects.all(),
			'form': ContactForm(),
			'questions': Question.objects.filter(is_visible=True)}
	if request.method == "GET":
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			# e_name = form.cleaned_data["e_name"]
			# email = form.cleaned_data["email"]
			# send_email_(f"{e_name}\n{email}")

	return render(request, "index.html", data)


# def send_email_(namemail):
# 	sender = "expertmail050@gmail.com"
# 	password = "pydvu4-kitpuX-butzes"

# 	server = smtplib.SMTP("smtp.gmail.com", 587)
# 	server.starttls()

# 	try:
# 		server.login(sender, password)
# 		msg = MIMEText(namemail)
# 		msg["Subject"] = "message from Expert"
# 		server.sendmail(sender, sender, msg.as_string())

# 		# server.sendmail(sender, sender, f"Subject: CLICK ME PLEASE!\n{message}")

# 		return "The message was sent successfully!"
# 	except Exception as _ex:
# 		return f"{_ex}\nCheck your login or password please!"
