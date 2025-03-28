import streamlit as st
import base64
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,f1_score,precision_score,recall_score
import joblib

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


set_background("C:\\Users\\Nandhakishore\\Desktop\\Python\\EdTech\\Background.png")

st.markdown("<h1 style='text-align: center; color: black;'>DIFFICULTY LEVEL PREDICTOR</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='color: black;'>Enter the Student ID : </h3>", unsafe_allow_html=True)
student_id = st.number_input("Enter Student ID :")

st.markdown("<h3 style='color: black;'>Enter the Quiz ID : </h3>", unsafe_allow_html=True)
Quiz_id = st.number_input("Enter Quiz ID :")

st.markdown("<h3 style='color: black;'>Enter the Right Answers in Topic 1 : </h3>", unsafe_allow_html=True)
selected_number1 = st.selectbox("Select a number:", options=list(range(6)))
st.markdown("<h3 style='color: black;'>Enter Time Taken For Topic 1 : </h3>", unsafe_allow_html=True)
selected_time1 = st.number_input("Enter Time Taken For Topic 1 :")
#print(selected_number)

st.markdown("<h3 style='color: black;'>Enter the Right Answers in Topic 2 : </h3>", unsafe_allow_html=True)
selected_number2 = st.selectbox("Select a number for Topic 2:", options=list(range(6)))
st.markdown("<h3 style='color: black;'>Enter Time Taken For Topic 2 : </h3>", unsafe_allow_html=True)
selected_time2 = st.number_input("Enter Time Taken For Topic 2:")

st.markdown("<h3 style='color: black;'>Enter the Right Answers in Topic 3 : </h3>", unsafe_allow_html=True)
selected_number3 = st.selectbox("Select a number for Topic 3:", options=list(range(6)))
st.markdown("<h3 style='color: black;'>Enter Time Taken For Topic 3: </h3>", unsafe_allow_html=True)
selected_time3 = st.number_input("Enter Time Taken For Topic 3 :")

st.markdown("<h3 style='color: black;'>Enter the Right Answers in Topic 4 : </h3>", unsafe_allow_html=True)
selected_number4 = st.selectbox("Select a number for Topic 4:", options=list(range(6)))
st.markdown("<h3 style='color: black;'>Enter Time Taken For Topic 4 : </h3>", unsafe_allow_html=True)
selected_time4 = st.number_input("Enter Time Taken For Topic 4 :")

st.markdown("<h3 style='color: black;'>Enter the Right Answers in Topic 5 : </h3>", unsafe_allow_html=True)
selected_number5 = st.selectbox("Select a number for Topic 5:", options=list(range(6)))
st.markdown("<h3 style='color: black;'>Enter Time Taken For Topic 5 : </h3>", unsafe_allow_html=True)
selected_time5 = st.number_input("Enter Time Taken For Topic 5:")

st.markdown("<h3 style='color: black;'>Enter the Right Answers in Topic 6 : </h3>", unsafe_allow_html=True)
selected_number6 = st.selectbox("Select a number for Topic 6:", options=list(range(6)))
st.markdown("<h3 style='color: black;'>Enter Time Taken For Topic 6 : </h3>", unsafe_allow_html=True)
selected_time6 = st.number_input("Enter Time Taken For Topic 6 :")

st.markdown("<h3 style='color: black;'>Enter the Right Answers in Topic 7 : </h3>", unsafe_allow_html=True)
selected_number7 = st.selectbox("Select a number for Topic 7:", options=list(range(6)))
st.markdown("<h3 style='color: black;'>Enter Time Taken For Topic 7 : </h3>", unsafe_allow_html=True)
selected_time7 = st.number_input("Enter Time Taken For Topic 7 :")
st.markdown("<h3 style='color: black;'>Enter the Right Answers in Topic 8 : </h3>", unsafe_allow_html=True)
selected_number8 = st.selectbox("Select a number for Topic 8:", options=list(range(6)))
st.markdown("<h3 style='color: black;'>Enter Time Taken For Topic 8 : </h3>", unsafe_allow_html=True)
selected_time8 = st.number_input("Enter Time Taken For Topic 8 :")

st.markdown("<h3 style='color: black;'>Enter the Right Answers in Topic 9 : </h3>", unsafe_allow_html=True)
selected_number9 = st.selectbox("Select a number for Topic 9:", options=list(range(6)))
st.markdown("<h3 style='color: black;'>Enter Time Taken For Topic 9 : </h3>", unsafe_allow_html=True)
selected_time9 = st.number_input("Enter Time Taken For Topic 9 :")

st.markdown("<h3 style='color: black;'>Enter the Right Answers in Topic 10 : </h3>", unsafe_allow_html=True)
selected_number10 = st.selectbox("Select a number for Topic 10:", options=list(range(6)))

st.markdown("<h3 style='color: black;'>Enter Time Taken For Topic 10 : </h3>", unsafe_allow_html=True)
selected_time10 = st.number_input("Enter Time Taken For Topic 10:")

total_correct=selected_number1+selected_number2+selected_number3+selected_number4+selected_number5+selected_number6+selected_number7+selected_number8+selected_number9+selected_number10
total_time=selected_time1+selected_time2+selected_time3+selected_time4+selected_time5+selected_time6+selected_time7+selected_time8+selected_time9+selected_time10
total_incorrect=50-total_correct
avg_time=total_time/10

raw_data = pd.read_csv(r"C:\Users\Nandhakishore\Desktop\Python\EdTech\random_forest_dataset.csv")

X = raw_data.drop(columns='Difficulty Prediction', axis=1)
Y = raw_data['Difficulty Prediction']

std = StandardScaler()
X_scaled = std.fit_transform(X)

x_train, x_test, y_train, y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=45)

y_train = y_train.astype(int)
y_test = y_test.astype(int)

model = RandomForestClassifier()
model.fit(x_train, y_train)

train_predictions = model.predict(x_train)
test_predictions = model.predict(x_test)


train_accuracy = accuracy_score(y_train, train_predictions)
test_accuracy = accuracy_score(y_test, test_predictions)

#print("accuracy of training :", train_accuracy)
#print("accuracy of testing :", test_accuracy)

#input_data = input("enter the values : ")

#input_values = np.array([float(i) for i in input_data.split(',')]).reshape(1, -1)
#print(input_values)

#std_input_data = std.transform(input_values)

pre=model.predict([[student_id,Quiz_id,total_correct,total_incorrect,avg_time,selected_number1,5-selected_number1,selected_time1,selected_number2,5-selected_number2,selected_time2,selected_number3,5-selected_number3,selected_time3,selected_number4,5-selected_number4,selected_time4,selected_number5,5-selected_number5,selected_time5,selected_number6,5-selected_number6,selected_time6,selected_number7,5-selected_number7,selected_time7,selected_number8,5-selected_number8,selected_time8,selected_number9,5-selected_number9,selected_time9,selected_number10,5-selected_number10,selected_time10]])

if pre[0] == 0:
    print("The student will attend the same difficulty level")
    st.markdown("<h1 style='color: red;'>The student will attend the same difficulty level</h1>", unsafe_allow_html=True)
else:
    print("The student will move to the next difficulty level")
    st.markdown("<h1 style='color: green;'>The student will move to the next difficulty level</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: black;'>SUBJECT DIFFICULTY LEVEL PREDICTOR</h1>", unsafe_allow_html=True)

load_data = pd.read_csv(r"C:\Users\Nandhakishore\Desktop\Python\EdTech\quiz_performance_dataset.csv")

X1 = load_data[['Quiz_ID', 'Total_Marks', 'Avg_Response_Time', 'Total_Time_Spent',
                'Topic_1_Marks', 'Topic_2_Marks', 'Topic_3_Marks', 'Topic_4_Marks',
                'Topic_5_Marks', 'Topic_6_Marks', 'Topic_7_Marks', 'Topic_8_Marks',
                'Topic_9_Marks', 'Topic_10_Marks']]

Y1 = load_data[['Topic_1_Strength', 'Topic_2_Strength', 'Topic_3_Strength', 'Topic_4_Strength',
                'Topic_5_Strength', 'Topic_6_Strength', 'Topic_7_Strength', 'Topic_8_Strength',
                'Topic_9_Strength', 'Topic_10_Strength']]

std1 = StandardScaler()
X1_scaled = std1.fit_transform(X1)

x1_train, x1_test, y1_train, y1_test = train_test_split(X1_scaled, Y1, test_size=0.2, random_state=3)

y1_train = y1_train.astype(int)
y1_test = y1_test.astype(int)

model1 = DecisionTreeClassifier()
model1.fit(x1_train, y1_train)

train1_predictions = model1.predict(x1_train)
test1_predictions = model1.predict(x1_test)

train1_accuracy = accuracy_score(y1_train, train1_predictions)
test1_accuracy = accuracy_score(y1_test, test1_predictions)

st.markdown("<h3 style='color: black;'>Enter the Mark of Subject 1 : </h3>", unsafe_allow_html=True)
subject_mark1 = st.number_input("Enter the Mark of Subject 1 :")

st.markdown("<h3 style='color: black;'>Enter the Mark of Subject 2 : </h3>", unsafe_allow_html=True)
subject_mark2 = st.number_input("Enter the Mark of Subject 2 :")

st.markdown("<h3 style='color: black;'>Enter the Mark of Subject 3 : </h3>", unsafe_allow_html=True)
subject_mark3 = st.number_input("Enter the Mark of Subject 3 :")

st.markdown("<h3 style='color: black;'>Enter the Mark of Subject 4 : </h3>", unsafe_allow_html=True)
subject_mark4 = st.number_input("Enter the Mark of Subject 4 :")

st.markdown("<h3 style='color: black;'>Enter the Mark of Subject 5 : </h3>", unsafe_allow_html=True)
subject_mark5 = st.number_input("Enter the Mark of Subject 5 :")

st.markdown("<h3 style='color: black;'>Enter the Mark of Subject 6 : </h3>", unsafe_allow_html=True)
subject_mark6 = st.number_input("Enter the Mark of Subject 6 :")

st.markdown("<h3 style='color: black;'>Enter the Mark of Subject 7 : </h3>", unsafe_allow_html=True)
subject_mark7 = st.number_input("Enter the Mark of Subject 7 :")

st.markdown("<h3 style='color: black;'>Enter the Mark of Subject 8 : </h3>", unsafe_allow_html=True)
subject_mark8 = st.number_input("Enter the Mark of Subject 8 :")

st.markdown("<h3 style='color: black;'>Enter the Mark of Subject 9 : </h3>", unsafe_allow_html=True)
subject_mark9 = st.number_input("Enter the Mark of Subject 9 :")

st.markdown("<h3 style='color: black;'>Enter the Mark of Subject 10 : </h3>", unsafe_allow_html=True)
subject_mark10 = st.number_input("Enter the Mark of Subject 10 :")

total_mark=10*5

prediction1 = model1.predict([[Quiz_id,total_mark,avg_time,total_time,subject_mark1,subject_mark2,subject_mark3,subject_mark4,subject_mark5,subject_mark6,subject_mark7,subject_mark8,subject_mark9,subject_mark10]])

target_columns = ['Digestive System', 'Respiratory System', 'Circulatory System', 'Excretory System',
                          'Nervous System', 'Human Reproduction', 'Endocrine System', 'Genetics and Heredity',
                          'Immune System and Diseases', 'Biotechnolgy in Human Welfare']

print("predicted topic strengths for the student: ")
st.markdown("<h3 style='color: black;'>Predicted Topic Strengths for the Student : </h3>", unsafe_allow_html=True)

print("predicted topic strengths for the student: ")
for i, column in enumerate(target_columns):
    print(f"{column}: {prediction1[0][i]}")
    st.markdown(f"<h4 style='color: black;'>{column}: {prediction1[0][i]}</h4>", unsafe_allow_html=True)



