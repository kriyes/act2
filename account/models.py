from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from phone_field import PhoneField


class Common_info(models.Model):  # DJANGO/PYTHON POWER
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    # state = models.ForeignKey(State,on_delete=models.CASCADE,default="")
    # city = models.ForeignKey(City ,on_delete=models.CASCADE,default="")
    # area = models.ForeignKey(Area,on_delete=models.CASCADE,default="")
    # address = models.CharField(max_length=30,default="")
    email = models.EmailField(default="")
    mobile = PhoneField(blank=True, help_text='Contact phone number', default="")
    joining_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Company(Common_info):
    CTYPE = (("ONE", "ONE"), ("TWO", "TWO"))
    # use Business Listing Services
    name = models.CharField(max_length=50, default="")
    company_type = models.CharField(max_length=30, choices=CTYPE, default='1')
    website = models.CharField(max_length=50, default="")
    GST = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.name


class Job(Common_info):
    job_company_name = models.ForeignKey(Company, on_delete=models.CASCADE, default="")
    job_name = models.CharField(max_length=50)
    job_profile = models.TextField()

    # job_type = models.ForeignKey(Job_type ,on_delete=models.CASCADE,default="")
    # job_category = models.ForeignKey(Job_category ,on_delete=models.CASCADE,default="")
    # job_salary = models.DecimalField(max_digits=10,decimal_places=2,default=10000.00)
    # Job_summary = models.TextField(default="abc")
    # job_responsibilities = models.TextField(default="abc")
    # job_keyskills = models.ManyToManyField(Key_skills,default="COMPUTER")

    def __str__(self):
        return self.job_name


class Langu(models.Model):
    choice = models.CharField(max_length=154, unique=True)

    def __str__(self):
        return self.choice


class Talent(Common_info):
    SEX = (("Male", "Male"), ("Female", "Female"))
    LANGU = (("english", "english"), ("hindi", "hindi"), ("gujarati", "gujarati"))
    HAIRL = (("long", "long"), ("short", "short"))
    COLO = (("light", "light"), ("dark", "dark"))
    HAIRC = (("BLACK", "BLACK"), ("WHITE", "WHITE"))
    EYES = (("black", "black"), ("dark brown", "dark brown"))
    COM = (("fair", "fair"), ("dark", "dark"))
    BODY = (("SLIM", "SLIM"), ("AVG", "AVG"))
    TATOO = (("YES", "YES"), ("NO", "NO"))
    PASS = (("YES", "YES"), ("NO", "NO"))
    CITY = (("SURAT", "SURAT"), ("ANAND", "ANAND"))
    ASIGN = (("YES", "YES"), ("NO", "NO"))
    EXPD = (("YES", "YES"), ("NO", "NO"))

    name_candidate = models.CharField(max_length=30)
    about_myself = models.TextField(max_length=300)
    # education = models.ManyToManyField(Education,blank=True)
    # job_expriance = models.ManyToManyField(Job,blank=True)
    # extra
    age = models.IntegerField(blank=True, null=True)
    expriance_in_year = models.IntegerField(blank=True, null=True)
    your_best_image1 = models.ImageField(upload_to='account/', blank=True)
    your_best_image2 = models.ImageField(upload_to='account/', blank=True)
    portfolio_img1 = models.ImageField(upload_to='account/', blank=True)
    portfolio_img2 = models.ImageField(upload_to='account/', blank=True)
    portfolio_img3 = models.ImageField(upload_to='account/', blank=True)
    portfolio_img4 = models.ImageField(upload_to='account/', blank=True)
    portfolio_img5 = models.ImageField(upload_to='account/', blank=True)
    portfolio_img6 = models.ImageField(upload_to='account/', blank=True)
    portfolio_img7 = models.ImageField(upload_to='account/', blank=True)
    portfolio_img8 = models.ImageField(upload_to='account/', blank=True)
    agency_signed = models.CharField(max_length=30, choices=ASIGN, default='1')
    exprienced = models.CharField(max_length=30, choices=EXPD, default='1')
    actor_model = models.CharField(max_length=30)  # DONE
    home_town = models.CharField(max_length=30, choices=CITY, default='1')  # DONE
    current_city = models.CharField(max_length=30, choices=CITY, default='1')  # DONE
    sex = models.CharField(max_length=30, choices=SEX, default='1')
    language = models.CharField(max_length=30, choices=LANGU, default='1')  # models.ManyToManyField(Langu)
    hair_color = models.CharField(max_length=30, choices=HAIRC, default='1')
    color = models.CharField(max_length=30, choices=COLO, default='1')
    hair_length = models.CharField(max_length=30, choices=HAIRL, default='1')
    eyes = models.CharField(max_length=30, choices=EYES, default='1')
    complexion = models.CharField(max_length=30, choices=COM, default='1')
    bust = models.CharField(max_length=30, default='29')
    waist = models.CharField(max_length=30, default='27')
    hips = models.CharField(max_length=30, default='30')
    body = models.CharField(max_length=30, choices=BODY, default='1')
    shoe_size = models.CharField(max_length=30, default='6')
    passport = models.CharField(max_length=30, choices=PASS, default='1')

    # WhatsApp number
    # Interest areas  mumbai & gujarat
    # Language - hindi bhojpuri english gujarati marathi
    # - Ramps - yes
    # - Traditional wear - yes
    # - Western wear - yes
    # -Bold . No
    # -Body Paint  no
    # - Nude shoot- no
    # -semi Nude  no
    # - Nightwear -   
    # - Bikini/  yes
    # -Swimwear -  yes
    # - TV serials -  yes
    # - Movies -  yes
    # - Any danceing skills -yes
    # Travel in any city yes
    # Work experience -- yes

    def __str__(self):
        return self.name_candidate


# /%Y/%m/%d

class Blog(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='blog/', blank=True)
    details = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='blog/%Y/%m/%d', blank=True)
    details = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# follwers,like,profile views ,contact ,+follow ,+like


# EXPERIENCE LEVEL
#     Experienced
# CURRENT STATE
#     Tamil Nadu
# CURRENT CITY
#     Coimbatore
# MARITAL STATUS
#     Single
# LANGUAGES KNOWN
#     English
# AVAILABLE FOR
#     Print Shoots
# PREFERRED LOCATION
#     Anywhere in India


# Physical Appearance
# HEIGHT (FEET, INCH.)
#     5 FEET 9 INCHES
# WEIGHT (KG)
#     67
# BICEPS (INCH)
#     14
# CHEST/BUST (INCH)
#     40
# WAIST (INCH)
#     31
# HIPS (INCH)
#     32
# HAIR COLOR
#     Black
# HAIR LENGTH
#     Medium
# HAIR TYPE
#     Wavy
# SKIN TONE
#     Dusky
# EYE COLOR
#     Brown
# DRESS (XS, S, M, L)
#     M
# SHOES (NO.)
#     8
# Rates & Travel
#     FULL DAY RATE
# Available On Request
#     HALF DAY RATE
# Available on request
#     HOURLY RATE
# Available on request
# PAYMENT OPTIONS
#     Bank Transfer, Cheque, Paytm, Cash
# AVAILABILITY
#     Weekends
# PASSPORT READY
#     Yes
# MAX DRIVING DISTANCE
#     300
# WILL TRAVEL? (FLY)
#     Yes
# TEST/TFP?
#     Yes
# About
#     I am experienced model

# Tags


# Create your models here.

# class State(models.Model):
#     name = models.CharField(max_length=20)

#     def __str__(self):
#         return self.name


# class City(models.Model):
#     state = models.OneToOneField(State,on_delete=models.CASCADE,default="")
#     name = models.CharField(max_length=20)

#     def __str__(self):
#         return self.name

# class Area(models.Model):
#     city = models.OneToOneField(City,on_delete=models.CASCADE,default="")
#     name = models.CharField(max_length=20)

#     def __str__(self):
#         return self.name

# class Education(models.Model):
#     highest_education = models.CharField(max_length=30)
#     board = models.CharField(max_length=30)

#     def __str__(self):
#         return '%s ' % (self.highest_education)

# class Job_category(models.Model):
#     name = models.CharField(max_length=20)

#     def __str__(self):
#         return self.name


# class Job_type(models.Model):
#     name = models.CharField(max_length=20)

#     def __str__(self):
#         return self.name


# class Company_type(models.Model):
#     name = models.CharField(max_length=20)

# #     def __str__(self):
# #         return self.name

# class Key_skills(models.Model):
#     name = models.CharField(max_length=30)

#     def __str__(self):
#         return self.name
