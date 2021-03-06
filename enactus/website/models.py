import django
from django.db import models
import datetime
# Create your models here.
class Season_board_1(models.Model):
    role_choices = [
        ('president','president'),
        ('vice president 1','vice president 1'),
        ('vice president 2', 'vice president 2'),
        ('vice president 3', 'vice president 3'),
        ('multimedia director','multimedia director'),
        ('er director','ER director'),
        ('hr director','HR director'),
        ('project director','project director'),
        ('presentation director','presentation director')
    ]
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    role = models.CharField(max_length=50,choices=role_choices)
    season = models.IntegerField()
    img = models.ImageField(upload_to='members-imgs')

    def __str__(self):
        return self.first_name+" "+self.last_name+" - "+self.role+" - Season "+str(self.season)

class Season_board_2(models.Model):
    role_choices = [
        ('president', 'president'),
        ('vice president 1', 'vice president 1'),
        ('vice president 2', 'vice president 2'),
        ('vice president 3', 'vice president 3'),
        ('multimedia director', 'multimedia director'),
        ('er director', 'ER director'),
        ('hr director', 'HR director'),
        ('project director', 'project director'),
        ('presentation director', 'presentation director')
    ]
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    role = models.CharField(max_length=50,choices=role_choices)
    season = models.IntegerField()
    img = models.ImageField(upload_to='members-imgs')

    def __str__(self):
        return self.first_name+" "+self.last_name+" - "+self.role+" - Season "+str(self.season)

class Event(models.Model):
    title = models.CharField(max_length = 100)
    status = models.BooleanField(default=False)
    banner = models.ImageField(upload_to='event-imgs')
    price = models.IntegerField()
    extra_price = models.CharField(max_length = 200,blank=True,null=True)
    text_1 = models.TextField()
    text_2 = models.TextField()
    text_3 = models.TextField()
    text_4 = models.TextField()

    def __str__(self):
        stt = 'Not Active'
        if self.status == True:
            stt = 'Active'
        return self.title+" - "+stt

class event_reservation(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    age = models.IntegerField()
    academic_year = models.IntegerField(blank=True,null=True)
    national_id_number = models.CharField(max_length=50,blank=True,null=True)
    first_time_for_him = models.CharField(max_length=50,blank=True,null=True)
    created_at = models.DateField(default=datetime.datetime.now(),blank=True)

    def __str__(self):
        stt = "Ended"
        if self.event.status == True:
            stt = "Active"
        return "({}) ".format(stt) + str(self.created_at) + " - " + str(self.event.title) + " -- Name: "+self.first_name+" "+self.last_name

class Gallery(models.Model):
    season = models.IntegerField()
    text = models.CharField(max_length=150)
    cover = models.ImageField(upload_to='album-cover')
class recruitment(models.Model):
    def current_year():
        return datetime.date.today().year
    colleges_list = [('Computer Science','Computer Science'),
                     ('Engineering','Engineering'),
                     ('Information Systems','Information Systems'),
                     ('Applied Arts','Applied Arts'),
                     ('Commerce and Business Administration','Commerce and Business Administration')
                     ]
    commities_list = [('multimedia','multimedia'),('hr','hr'),('er','er'),('presentation','presentation'),('project','project')]
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    college = models.CharField(max_length=50,choices=colleges_list)
    year_of_study = models.IntegerField()
    first_prefrence = models.CharField(max_length=50,choices=commities_list)
    second_prefrence = models.CharField(max_length=50,choices=commities_list)
    viewed = models.BooleanField(default=False)
    def __str__(self):
        v = "Not Viewed"
        if self.viewed:
            v = "Viewed"
        return "("+v+ ") "+self.first_name+" "+self.last_name

class open_recruitment(models.Model):
    status = models.BooleanField(default=False)
    def __str__(self):
        return "Open here to Enable or Disable Recruitment (Dont click on open_recruitment above just edit this)"

class summary(models.Model):
    season = models.IntegerField()
    title = models.CharField(max_length=100,null=True,blank=True)
    text = models.TextField()
    img = models.ImageField(upload_to='summary-imgs',null=True,blank=True)

    def __str__(self):
        return str(self.season)

class qr_code(models.Model):
    active = models.BooleanField(default=False)
    title = models.CharField(max_length=100,default="QR Code for Enactus NCA APP")
    qr_img = models.ImageField(upload_to='qr-imgs', null=True, blank=True)

    def __str__(self):
        return "Click here to Enable or Disable QR button or to add new QR Image"

class all_seasons_board(models.Model):
    season = models.IntegerField()
    summary_plan = models.ForeignKey('summary', on_delete=models.CASCADE)
    president = models.CharField(max_length=50)
    president_img = models.ImageField(upload_to='all-seasons-board-imgs')
    vice_1 = models.CharField(max_length=50)
    vice_1_img = models.ImageField(upload_to='all-seasons-board-imgs')
    vice_2 = models.CharField(max_length=50)
    vice_2_img = models.ImageField(upload_to='all-seasons-board-imgs')
    vice_3 = models.CharField(max_length=50,blank=True,null=True)
    vice_3_img = models.ImageField(upload_to='all-seasons-board-imgs',blank=True,null=True)
    multimedia = models.CharField(max_length=50)
    multimedia_img = models.ImageField(upload_to='all-seasons-board-imgs')
    hr = models.CharField(max_length=50)
    hr_img = models.ImageField(upload_to='all-seasons-board-imgs')
    er = models.CharField(max_length=50)
    er_img = models.ImageField(upload_to='all-seasons-board-imgs')
    project = models.CharField(max_length=50)
    project_img = models.ImageField(upload_to='all-seasons-board-imgs')
    presentation = models.CharField(max_length=50)
    presentation_img = models.ImageField(upload_to='all-seasons-board-imgs')

    def __str__(self):
        return str(self.season)


class sponsers(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='sponser-imgs')

    def __str__(self):
        return self.name
