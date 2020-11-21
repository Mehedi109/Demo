from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from . models import teacher_top,course_top,course_bottom,teacher_bottom,contact_top,contact_bottom,Usermessage
from . models import contact_email,contact_call,about_top,description
from django.contrib import messages
from . forms import teacher_bottomForm
def index(request):
	if request.user.is_authenticated:
		#return redirect('/')
		post=get_object_or_404(teacher_top)
		post2=get_object_or_404(course_top)
		post3=course_bottom.objects.all
		post4=teacher_bottom.objects.all()
		post5=get_object_or_404(contact_top)
		post6=get_object_or_404(contact_bottom)
		post7=get_object_or_404(contact_email)
		post8=get_object_or_404(contact_call)
		post9=get_object_or_404(about_top)
		post10=get_object_or_404(description)
		
		if request.method == 'POST':
			post_message=Usermessage()
			name=request.POST['name']
			email=request.POST['email']
			subject=request.POST['subject']
			message=request.POST['message']
			post_message.name=name
			post_message.email=email
			post_message.subject=subject
			post_message.message=message
			post_message.save()
			return HttpResponse('<h1>Thanks for messaging us</h1>')
			#return redirect('/')
		context={
			"post":post,
			"post2":post2,
			"post3":post3,
			#"post4":total_post,
			"post4":post4,
			"post5":post5,
			"post6":post6,
			"post7":post7,
			"post8":post8,
			"post9":post9,
			"post10":post10,
		}
		return render(request,"index.html",context)
	else:
		return redirect('login')

def author(request):
	return render(request,"author.html")

def teacher(request):
	post=teacher_bottom.objects.all()
	return render(request,'teacher.html',{'post':post})

def teacher_edit(request,id):
	post=teacher_bottom.objects.get(id=id)
	return render(request,"teacher_edit.html",{"post":post})

def teacher_update(request,id):
	post=teacher_bottom.objects.get(id=id)
	form=teacher_bottomForm(request.POST,instance=post)
	if form.is_valid():
	   form.save()  
	   return redirect("/teacher")
	   return render(request,"teacher_edit.html",{"post":post})
	return HttpResponse()

