from django.db import models

# Create your models here.
class Board(models.Model):
	title = models.CharField(max_length=100)
	sorder = models.IntegerField()
	def __str__(self):
		return self.title    

# class Club(models.Model):
# 	title = models.CharField(max_length=100)
# 	board = models.ForeignKey(Board )

# 	def __str__(self):
# 		return self.title

# 	def gensec(self):
# 		x = self.representative_set.filter(position="General Secretary")
# 		if x:
# 			return x[0].__str__()	
# 	def status(self):
# 		x = self.representative_set.all().promise_set.filter(status="C")
# 		return len(x)		
class Representative(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	image = models.ImageField(null=True,blank=True,upload_to='images/')
	join_data = models.DateField()
	end_data = models.DateField()
	position = models.CharField(max_length=200)
	description = models.CharField(max_length=300)
	phone = models.IntegerField()
	webmail = models.EmailField()
	board = models.ForeignKey(Board)
	sub_board = models.CharField(max_length=50,null=True,blank=True)
	dept = models.CharField(max_length=100,null=True,blank=True)
	year = models.CharField(max_length=100,null=True,blank=True)
	degree = models.CharField(max_length=100,null=True,blank=True)

	# club = models.ForeignKey(Club)
	def __str__(self):
		return self.first_name+" "+self.last_name
	def contact_info(self):
		return "Phone Number: "+self.phone+"<br> Webmail: "+self.webmail    
	def successful(self):
		return self.promise_set.filter(status="C").count()
	def pg(self):
		return self.promisegroup_set.all()		
class PromiseGroup(models.Model):
	description = models.CharField(max_length=150)
	representative = models.ForeignKey(Representative)

	def __str__(self):
		return self.description+", "+self.representative.__str__()
	def promisesC(self):
		return self.promise_set.filter(status="C")	
	def promisesWIP(self):
		return self.promise_set.filter(status="WIP")	
	def promisesNS(self):
		return self.promise_set.filter(status="NS")	
	def promisesB(self):
		return self.promise_set.filter(status="B")	
		
class Promise(models.Model):
	description = models.TextField()
	representative = models.ForeignKey(Representative)
	promisegroup = models.ForeignKey(PromiseGroup)
	STATUS = (
		('C','Completed'),
		('WIP','In Progress'),
		('NS','Not Started'),
		('B','Broken'),
		)
	status = models.CharField(max_length=3, choices=STATUS, default='NS' )
	def __str__(self):
		return "Promise "+str(self.id)+", "+self.representative.__str__()
