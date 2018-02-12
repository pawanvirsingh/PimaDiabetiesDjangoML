# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.edit import CreateView
# Create your views here.
from .forms  import DiabetiesForm
from models import Diabeties
# class DibetiesView(FormView):
#     template_name= 'MlDiabetiesModel/DiabetiesReport.html'
#     form_class= DiabetiesForm
#     success_url= '/thanks/'

#     def form_valid(self, form):
#         print "form is valid so "
#         return super(DibetiesView).form_valid(form)

class DibetiesView(CreateView):
    template_name= 'MlDiabetiesModel/DiabetiesReport.html'
    success_url= '/thanks/'
    model = Diabeties
    form_class=DiabetiesForm
    # fields = "__all__"


# import pandas
# from sklearn import model_selection
# from sklearn.linear_model import LogisticRegression
# import pickle
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
# # 1. Number of times pregnant 
# # 2. Plasma glucose concentration a 2 hours in an oral glucose tolerance test 
# # 3. Diastolic blood pressure (mm Hg) 
# # 4. Triceps skin fold thickness (mm) 
# # 5. 2-Hour serum insulin (mu U/ml) 
# # 6. Body mass index (weight in kg/(height in m)^2) 
# # 7. Diabetes pedigree function 
# # 8. Age (years) 
# # 9. Class variable (0 or 1)
# names = ['preg', 'f', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
# dataframe = pandas.read_csv(url, names=names)
# array = dataframe.values
# X = array[:,0:8]
# Y = array[:,8]
# test_size = 0.33
# seed = 7
# X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)
# # Fit the model on 33%
# model = LogisticRegression()
# model.fit(X_train, Y_train)
# # save the model to disk
# filename = 'finalized_model.sav'
# pickle.dump(model, open(filename, 'wb'))
 
# # some time later...
 
# # load the model from disk
# loaded_model = pickle.load(open(filename, 'rb'))
# result = loaded_model.score(X_test, Y_test)
# print(result)


