from django.shortcuts import render
from .forms import ApprovalForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Approvals
from .serializers import approvalsSerializers
import pickle
from sklearn.externals import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd
from django.views.generic import  FormView


class ApprovalsView(viewsets.ModelViewSet):
	queryset = Approvals.objects.all()
	serializer_class = approvalsSerializers

def ohevalue(df):
	ohe_col = joblib.load("/home/samir/Downloads/allcol.pkl")
	cat_columns = ['Gender','Married','Education','Self_Employed','Property_Area']
	df_processed = pd.get_dummies(df, columns=cat_columns)
	newdict= {}
	for i in ohe_col:
		if i in df_processed.columns:
			newdict[i] = df_processed[i].values
		else:
			newdict[i] = 0
	newdf = pd.DataFrame(newdict)
	return newdf

def myform(request):
	form = ApprovalForm(request.POST or None)
	context = {
	"form": form
	}
	if form.is_valid():
		Firstname = form.cleaned_data['firstname']
		Lastname = form.cleaned_data['lastname']
		Dependents = form.cleaned_data['Dependents']
		ApplicantIncome = form.cleaned_data['ApplicantIncome']
		CoapplicantIncome = form.cleaned_data['CoapplicantIncome']
		LoanAmount = form.cleaned_data['Loan_Amount']
		Loan_Amount_Term = form.cleaned_data['Loan_Amount_Term']
		Credit_History = form.cleaned_data['Credit_History']
		Gender = form.cleaned_data['Gender']
		Married = form.cleaned_data['Married']
		Education = form.cleaned_data['Education']
		Self_Employed = form.cleaned_data['Self_Employed']
		Property_Area = form.cleaned_data['Property_Area']
		myDict = (request.POST).dict()
		df = pd.DataFrame(myDict, index=[0])
		answer = approvereject(ohevalue(df))
		messages.success(request, 'Application Status: {}'.format(answer))
	return render(request, 'myform/form.html',context)
		
# @api_view(["POST"])
def approvereject(unit):
	try:
		mdl=joblib.load("/home/samir/MLAPLI-master/MyAPI/loan_model.pkl")
		#mydata=pd.read_excel('/Users/sahityasehgal/Documents/Coding/bankloan/test.xlsx')
		scalers=joblib.load("/home/samir/MLAPLI-master/MyAPI/scalers.pkl")
		X=scalers.transform(unit)
		y_pred=mdl.predict(X)
		y_pred=(y_pred>0.58)
		newdf=pd.DataFrame(y_pred, columns=['Status'])
		newdf=newdf.replace({True:'Approved', False:'Rejected'})
		return ('Your Status is {}'.format(newdf))
	except ValueError as e:
		return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
