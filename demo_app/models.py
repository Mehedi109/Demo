from django.db import models

class course_top(models.Model):
	title=models.CharField(max_length=50)
	subtitle=models.CharField(max_length=100)

class course_bottom(models.Model):
	image=models.FileField()
	title=models.CharField(max_length=50)
	description=models.TextField()

class teacher_top(models.Model):
	title=models.CharField(max_length=50)
	subtitle=models.CharField(max_length=100)

class teacher_bottom(models.Model):
	image=models.FileField()
	name=models.CharField(max_length=50)
	subject=models.CharField(max_length=50)
	contact=models.CharField(max_length=20)

	def __str__(self):
		return self.name

class contact_top(models.Model):
	title=models.CharField(max_length=50)
	subtitle=models.CharField(max_length=100)
	description=models.TextField()

class contact_bottom(models.Model):
	title=models.CharField(max_length=50)
	subtitle=models.CharField(max_length=100)

class contact_email(models.Model):
	title=models.CharField(max_length=50)
	subtitle=models.CharField(max_length=100)

class contact_call(models.Model):
	title=models.CharField(max_length=50)
	subtitle=models.CharField(max_length=100)

class Usermessage(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField(max_length=20)
	subject=models.CharField(max_length=50)
	message=models.TextField()

	def __str__(self):
		return self.name
class about_top(models.Model):
	title=models.CharField(max_length=50)
	subtitle=models.CharField(max_length=100)
	description=models.TextField()

class description(models.Model):
	image=models.FileField()
	title=models.CharField(max_length=100)
	body=models.TextField()
		

		
	
