from main.models import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import *
import smtplib
from django.views.decorators.csrf import csrf_exempt


def index2(request):
	data = {'services': Service.objects.all(), 
			'educations': Education.objects.all(),
			'additions': Addition.objects.all()}

	return render(request, 'index1.2.html', data)


@csrf_exempt
def index(request):
	data = {'disciplines': Discipline.objects.all(), 
			# 'services': Service.objects.all(), 
			# 'educations': Education.objects.all(),
			# 'additions': Addition.objects.all(), 
			'partners': Partner.objects.all(),
			'c_form': ContactForm(),
			"q_form": QuestionForm()}
	
	if request.method == "POST":
		if "e_name" in request.POST:
			form = ContactForm(request.POST)
			if form.is_valid():
				form.save()
		elif "q_name" in request.POST:
			form = QuestionForm(request.POST)
			if form.is_valid():
				form.save()

	return render(request, "index1.html", data)


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
