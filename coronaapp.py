import streamlit as st
import pandas as pd
import pickle 

dbfile=open('coronamodel.pickle','rb')
model=pickle.load(dbfile)

st.title("Corona Prediction")

cs=st.radio("Do you have cough symptoms:",["Yes","No"])
f=st.radio("Do you have Fever:",["Yes","No"])
stt=st.radio("Do you have Sore_throat:",["Yes","No"])
sb=st.radio("Do you have Shortness_of_breath:",["Yes","No"])
h=st.radio("Do you have Headache:",["Yes","No"])
age=st.radio("Do you have Age_60_above:",["Yes","No"])
sex=st.radio("Enter your gender:",["Male","Female"])
cwc=st.radio("attached with:",["abroad","other","contact_with_conform"])

if st.button("Prediction"):
	if cs=="Yes":
		Cough_symptoms=1
	else:
		Cough_symptoms=0

	if f=="Yes":
		Fever=1
	else:
		Fever=0
	if stt=="Yes":
		Sore_throat=1
	else:
		Sore_throat=0

	if sb=="Yes":
		Shortness_of_breath=1
	else:
		Shortness_of_breath=0

	if h=="Yes":
		Headache=1
	else:
		Headache=0

	if age=="Yes":
		Age_60_above=1
	else:
		Age_60_above=0

	if sex=="Male":
		Sex=1
	else:
		Sex=0
	known_contact = {"abroad": 0, "other": 1, "contact_with_conform": 2}[cwc]

#['Cough_symptoms', 'Fever', 'Sore_throat', 'Shortness_of_breath',
 #      'Headache', 'Corona', 'Age_60_above', 'Sex', 'Known_contact']
	df=pd.DataFrame({"Cough_symptoms":[Cough_symptoms],
	"Fever":[Fever],
	"Sore_throat":[Sore_throat],
	"Shortness_of_breath":[Shortness_of_breath],
	"Headache":[Headache],
	"Age_60_above":[Age_60_above],
	"Sex":[Sex],
	"Known_contact":[known_contact]})
	st.dataframe(df)
	result=model.predict(df)
	if (result)>1:
		st.title("Corona positive")

	else:
		st.title(" Congratulatio! Corona Negative")
		st.balloons()

	st.write(result)


	
