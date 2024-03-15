from django.db import models
from django.contrib.auth.models import User



departments=[
('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons'),
('Endocrinologists','Endocrinologists'),
('Gastroenterologists','Gastroenterologists'),
('Nephrologists','Nephrologists'),
('Urologists','Urologists'),
('Pulmonologists','Pulmonologists'),
('Neurologists','Neurologists'),
('Radiologists','Radiologists'),
('Rheumatologists','Rheumatologists'),
('Orthopedic Surgeons','Orthopedic Surgeons'),
('Ophthalmologists','Ophthalmologists'),
('Oncologists','Oncologists'),
('Psychiatrists','Psychiatrists'),
('Pathologists','Pathologists'),
('Pediatricians','Pediatricians'),
('Gynecologists','Gynecologists'),
('Obstetricians','Obstetricians'),
('General Surgeons','General Surgeons'),
('Family Physicians','Family Physicians'),
('Dentists','Dentists'),
('Physiotherapists','Physiotherapists'),
('Neonatologists','Neonatologists'),
('Geriatricians','Geriatricians'),
('Hematologists','Hematologists'),
('Infectious Disease Specialists','Infectious Disease Specialists'),
('Pain Management Specialists','Pain Management Specialists'),
('Plastic Surgeons','Plastic Surgeons'),
('Radiation Oncologists','Radiation Oncologists'),
('Sleep Medicine Specialists','Sleep Medicine Specialists'),
('Sports Medicine Physicians','Sports Medicine Physicians'),
('Vascular Surgeons','Vascular Surgeons'),
('Diagnostic Radiologists','Diagnostic Radiologists'),
('Interventional Radiologists','Interventional Radiologists'),
('Medical Geneticists','Medical Geneticists'),
('Nuclear Medicine Specialists','Nuclear Medicine Specialists'),
('Occupational Medicine Specialists','Occupational Medicine Specialists'),
('Osteopathic Physicians','Osteopathic Physicians'),
('Podiatrists','Podiatrists'),
('Preventive Medicine Specialists','Preventive Medicine Specialists'),
('Pulmonary Disease Specialists','Pulmonary Disease Specialists'),
('Reproductive Endocrinologists','Reproductive Endocrinologists'),
('Medical Oncologists','Medical Oncologists'),
('Thoracic Surgeons','Thoracic Surgeons'),
('Transplant Surgeons','Transplant Surgeons'),
('Urogynecologists','Urogynecologists'),
('Vascular Medicine Specialists','Vascular Medicine Specialists')
]

class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)



class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    symptoms = models.CharField(max_length=100,null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name+" ("+self.symptoms+")"


class Appointment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)



class PatientDischargeDetails(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40)
    assignedDoctorName=models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    symptoms = models.CharField(max_length=100,null=True)

    admitDate=models.DateField(null=False)
    releaseDate=models.DateField(null=False)
    daySpent=models.PositiveIntegerField(null=False)

    roomCharge=models.PositiveIntegerField(null=False)
    medicineCost=models.PositiveIntegerField(null=False)
    doctorFee=models.PositiveIntegerField(null=False)
    OtherCharge=models.PositiveIntegerField(null=False)
    total=models.PositiveIntegerField(null=False)


class Diagnosis(models.Model):
    text = models.TextField()
    disease = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    app_label = 'diagnosis'  # Set the app_label explicitly
    ans = models.TextField() 
