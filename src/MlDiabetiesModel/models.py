# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Diabeties(models.Model):
	#this is the models 
	# 1. Number of times pregnant 
	# 2. Plasma glucose concentration a 2 hours in an oral glucose tolerance test 
	# 3. Diastolic blood pressure (mm Hg) 
	# 4. Triceps skin fold thickness (mm) 
	# 5. 2-Hour serum insulin (mu U/ml) 
	# 6. Body mass index (weight in kg/(height in m)^2) 
	# 7. Diabetes pedigree function 
	# 8. Age (years) 
	# 9. Class variable (0 or 1)
	preg= models.CharField(max_length=25,verbose_name='Number of times pregnant')
	plas=  models.CharField(max_length=25, verbose_name= 'Plasma glucose concentration a 2 hours in an oral glucose tolerance test')
	pres= models.CharField(max_length=25,verbose_name="Diastolic blood pressure (mm Hg)")
	skin= models.CharField(max_length=25,verbose_name="Triceps skin fold thickness (mm)")
	test= models.CharField(max_length=25,verbose_name="2-Hour serum insulin (mu U/ml)")
	mass= models.CharField(max_length=25, verbose_name="Body mass index (weight in kg/(height in m)^2) ")
	pedi= models.CharField(max_length=25,verbose_name="Diabetes pedigree function ")
	age= models.CharField(max_length=25, verbose_name='Age (years) ')
	class_data= models.CharField(max_length=25,verbose_name="Diabetes result")
	result= models.CharField(max_length=10,verbose_name="Diabetes result1")


