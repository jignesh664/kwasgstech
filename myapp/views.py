# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http  import Http404
from .models import Contact,Received_Resume,Post,Job_Description,Responsibilites,Qualifications,Skill

# for flash massages
from django.contrib import messages


# Create your views here.
def index(request):
	return render(request,'index.html')

def header(request):
	return render(request,'header.html')

def about(request):
	return render(request,'about.html')		

def services(request):
	return render(request,'services.html')

def Quality_Assurance_Services(request):
	return render(request,'Quality_Assurance_Services.html')

def Cloud_Computing(request):
	return render(request,'Cloud_Computing.html')

def Android_Application_Development(request):
	return render(request,'Android_Application_Development.html')

def React_Native_Development(request):
	return render(request,'React_Native_Development.html')

def Web_Development(request):
	return render(request,'Web_Development.html')

def Game_development(request):
	return render(request,'Game_development.html')


def career(request):
	l=Post.objects.all()
	return render(request,'career.html',{'l':l})
	

def contact(request):
	return render(request,'contact.html')

def sitemap(request):
	return render(request,'sitemap.html')	

def privacy_policy(request):
	return render(request,'privacy_policy.html')		

	




def contact1(request):
	if request.method=="POST":
		user=Contact.objects.create(
			name=request.POST['name'],
			email=request.POST['email'],
			subject=request.POST['subject'],
			message=request.POST['message'],
			
			)			
		 
		messages.success(request,f'Hey, {user.name}! \n Thanks for approaching us,We will get back to You Soon!!!')
		return render(request,'contact.html')
	# else:
	# 	return render(request,'index.html')	

# def Job_Post(request,pk):
# 	p=get_object_or_404(Post, pk=pk)
# 	if not hasattr(p, 'job_description'):
# 		# raise Http404("Job description not found")
# 		return render(request,'error.html')
# 	jd = p.job_description
	
# 	a=Responsibilites.objects.all()
# 	b=Qualifications.objects.all()
# 	c=Skill.objects.all()
# 	return render(request,'Job/Job_Post.html',{'p':jd, 'a':a,'b':b,'c':c})


def Job_Post(request,pk):
	p=get_object_or_404(Post, pk=pk)
	if not hasattr(p, 'job_description'):
		# raise Http404("Job description not found")
		return render(request,'error.html')
	jd = p.job_description
	
	# a=Responsibilites.objects.filter(post_id=p)
	a=Responsibilites.objects.filter(post_id=p)
	b=Qualifications.objects.filter(post_id=p)
	c=Skill.objects.filter(post_id=p)
	return render(request,'Career/Job.html',{'p':jd, 'a':a,'b':b,'c':c})

def job_apply(request):
	if request.method=="POST":
		user=Received_Resume.objects.create(
			fname=request.POST['fname'],
			lname=request.POST['lname'],
			email=request.POST['email'],
			phone=request.POST['phone'],
			cletter=request.POST['cletter'],
			resume=request.FILES['resume']	
		)
		messages.success(request,f'Hey, {user.fname}! \n Thanks for Applying this Job,  We will get back to You Soon!!')
		return render(request,'contact.html')		
	else:
		return render(request,'career.html')		



























	


	
	