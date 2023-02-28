from django.db import models

# Create your models here.


class Contact(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	subject=models.CharField(max_length=100)
	message=models.TextField()

	def __str__(self):
		return self.name

class Received_Resume(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	phone=models.CharField(max_length=100)
	cletter=models.TextField()
	resume=models.FileField()

	def __str__(self):
		return self.fname

class Post(models.Model):
	post_name=models.CharField(max_length=100)
	# slug = models.SlugField(max_length = 250, null = True, blank = True)
	

	def __str__(self):
		return self.post_name

class Responsibilites(models.Model):
	post_id=models.ForeignKey(Post,on_delete=models.CASCADE)
	Responsibilite=models.CharField(max_length=100)

	def __str__(self):
		return f'{self.post_id }'

class Qualifications(models.Model):
	post_id=models.ForeignKey(Post,on_delete=models.CASCADE)
	Qualification=models.CharField(max_length=100)

	def __str__(self):
		return f'{self.post_id }'

class Skill(models.Model):
	post_id=models.ForeignKey(Post,on_delete=models.CASCADE)
	Skills=models.CharField(max_length=100)	

	def __str__(self):
		return f'{self.post_id }'


class Job_Description(models.Model):
	post_id=models.OneToOneField(Post,on_delete=models.CASCADE, related_name='job_description')

	# responsibilites_id=models.ForeignKey(Responsibilites,on_delete=models.CASCADE,null=True,blank=True)
	# qualifications_id=models.ForeignKey(Qualifications,on_delete=models.CASCADE,null=True,blank=True)
	# Skill_id=models.ForeignKey(Skill,on_delete=models.CASCADE,null=True,blank=True)

	Title=models.CharField(max_length=100)
	Job_Category=models.CharField(max_length=100)
	Job_Type=models.CharField(max_length=100)
	Job_Location=models.CharField(max_length=100)
	Brief=models.CharField(max_length=255)

	

	def __str__(self):
		return f'{self.post_id }'

















		