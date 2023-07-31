import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor
from category_encoders import BinaryEncoder
import subprocess

subprocess.call("pip install -r requirements.txt", shell=True)

st.sidebar.header('User Input Features')

def user_input_features():
    gender = st.sidebar.radio('Gender', ('Male', 'Female'))
    age = st.sidebar.slider('Age', 21, 56, 32)
    years_of_exp = st.sidebar.slider('Years of Experience', 0, 25, 5)
    education_level = [
        "Bachelor's", 
        "Master's", 
        'PhD', 
        'High School']
    selected_education_level = st.sidebar.selectbox('Education Level', education_level)
    industry = [
        'Information Technology',
        'Management',
        'Sales',
        'Marketing',
        'Science',
        'Human Resources',
        'Finance',
        'Customer Service',
        'Engineering',
        'Business',
        'Design',
        'Administrative',
        'Event Planning',
        'Research',
        'Logistics',
        'Training',
        'Media',
        'Product Development']
    selected_industry = st.sidebar.selectbox('Industry', industry)
    data = {
        'Age' : age,
        'Gender' : gender,
        'Education Level' : selected_education_level,
        'Years of Experience' : years_of_exp,
        'Job Title' : selected_industry}
    features = pd.DataFrame(data, index=[0])
    return features 

input_df = user_input_features()

df = pd.read_csv('Salary_Data_Based_country_and_race.csv')
df = df.drop(columns=['Salary'])
df = pd.concat([input_df, df], axis=0)

df = pd.get_dummies(df, columns=['Gender'])
df = pd.get_dummies(df, columns=['Education Level'])

industry_mapping = {
    'Software Engineer': 'Information Technology',
    'Data Analyst': 'Information Technology',
    'Senior Manager': 'Management',
    'Sales Associate': 'Sales',
    'Director': 'Management',
    'Marketing Analyst': 'Marketing',
    'Product Manager': 'Management',
    'Sales Manager': 'Sales',
    'Marketing Coordinator': 'Marketing',
    'Senior Scientist': 'Science',
    'Software Developer': 'Information Technology',
    'HR Manager': 'Human Resources',
    'Financial Analyst': 'Finance',
    'Project Manager': 'Management',
    'Customer Service Rep': 'Customer Service',
    'Operations Manager': 'Management',
    'Marketing Manager': 'Marketing',
    'Senior Engineer': 'Engineering',
    'Data Entry Clerk': 'Information Technology',
    'Sales Director': 'Sales',
    'Business Analyst': 'Business',
    'VP of Operations': 'Management',
    'IT Support': 'Information Technology',
    'Recruiter': 'Human Resources',
    'Financial Manager': 'Finance',
    'Social Media Specialist': 'Marketing',
    'Software Manager': 'Information Technology',
    'Junior Developer': 'Information Technology',
    'Senior Consultant': 'Management',
    'Product Designer': 'Design',
    'CEO': 'Management',
    'Accountant': 'Finance',
    'Data Scientist': 'Information Technology',
    'Marketing Specialist': 'Marketing',
    'Technical Writer': 'Information Technology',
    'HR Generalist': 'Human Resources',
    'Project Engineer': 'Engineering',
    'Customer Success Rep': 'Customer Service',
    'Sales Executive': 'Sales',
    'UX Designer': 'Design',
    'Operations Director': 'Management',
    'Network Engineer': 'Information Technology',
    'Administrative Assistant': 'Administrative',
    'Strategy Consultant': 'Management',
    'Copywriter': 'Marketing',
    'Account Manager': 'Sales',
    'Director of Marketing': 'Marketing',
    'Help Desk Analyst': 'Information Technology',
    'Customer Service Manager': 'Customer Service',
    'Business Intelligence Analyst': 'Business',
    'Event Coordinator': 'Event Planning',
    'VP of Finance': 'Finance',
    'Graphic Designer': 'Design',
    'UX Researcher': 'Design',
    'Social Media Manager': 'Marketing',
    'Director of Operations': 'Management',
    'Senior Data Scientist': 'Information Technology',
    'Junior Accountant': 'Finance',
    'Digital Marketing Manager': 'Marketing',
    'IT Manager': 'Information Technology',
    'Customer Service Representative': 'Customer Service',
    'Business Development Manager': 'Business',
    'Senior Financial Analyst': 'Finance',
    'Web Developer': 'Information Technology',
    'Research Director': 'Research',
    'Technical Support Specialist': 'Information Technology',
    'Creative Director': 'Design',
    'Senior Software Engineer': 'Information Technology',
    'Human Resources Director': 'Human Resources',
    'Content Marketing Manager': 'Marketing',
    'Technical Recruiter': 'Human Resources',
    'Sales Representative': 'Sales',
    'Chief Technology Officer': 'Management',
    'Junior Designer': 'Design',
    'Financial Advisor': 'Finance',
    'Junior Account Manager': 'Sales',
    'Senior Project Manager': 'Management',
    'Principal Scientist': 'Science',
    'Supply Chain Manager': 'Logistics',
    'Senior Marketing Manager': 'Marketing',
    'Training Specialist': 'Training',
    'Research Scientist': 'Research',
    'Junior Software Developer': 'Information Technology',
    'Public Relations Manager': 'Marketing',
    'Operations Analyst': 'Management',
    'Product Marketing Manager': 'Marketing',
    'Senior HR Manager': 'Human Resources',
    'Junior Web Developer': 'Information Technology',
    'Senior Project Coordinator': 'Management',
    'Chief Data Officer': 'Management',
    'Digital Content Producer': 'Media',
    'IT Support Specialist': 'Information Technology',
    'Senior Marketing Analyst': 'Marketing',
    'Customer Success Manager': 'Customer Service',
    'Senior Graphic Designer': 'Design',
    'Software Project Manager': 'Information Technology',
    'Supply Chain Analyst': 'Logistics',
    'Senior Business Analyst': 'Business',
    'Junior Marketing Analyst': 'Marketing',
    'Office Manager': 'Administrative',
    'Principal Engineer': 'Engineering',
    'Junior HR Generalist': 'Human Resources',
    'Senior Product Manager': 'Management',
    'Junior Operations Analyst': 'Management',
    'Senior HR Generalist': 'Human Resources',
    'Sales Operations Manager': 'Sales',
    'Senior Software Developer': 'Information Technology',
    'Junior Web Designer': 'Design',
    'Senior Training Specialist': 'Training',
    'Senior Research Scientist': 'Research',
    'Junior Sales Representative': 'Sales',
    'Junior Marketing Manager': 'Marketing',
    'Junior Data Analyst': 'Information Technology',
    'Senior Product Marketing Manager': 'Marketing',
    'Junior Business Analyst': 'Business',
    'Senior Sales Manager': 'Sales',
    'Junior Marketing Specialist': 'Marketing',
    'Junior Project Manager': 'Management',
    'Senior Accountant': 'Finance',
    'Director of Sales': 'Sales',
    'Junior Recruiter': 'Human Resources',
    'Senior Business Development Manager': 'Business',
    'Senior Product Designer': 'Design',
    'Junior Customer Support Specialist': 'Customer Service',
    'Senior IT Support Specialist': 'Information Technology',
    'Junior Financial Analyst': 'Finance',
    'Senior Operations Manager': 'Management',
    'Director of Human Resources': 'Human Resources',
    'Junior Software Engineer': 'Information Technology',
    'Senior Sales Representative': 'Sales',
    'Director of Product Management': 'Management',
    'Junior Copywriter': 'Marketing',
    'Senior Marketing Coordinator': 'Marketing',
    'Senior Human Resources Manager': 'Human Resources',
    'Junior Business Development Associate': 'Business',
    'Senior Account Manager': 'Sales',
    'Senior Researcher': 'Research',
    'Junior HR Coordinator': 'Human Resources',
    'Director of Finance': 'Finance',
    'Junior Marketing Coordinator': 'Marketing',
    'Junior Data Scientist': 'Information Technology',
    'Senior Operations Analyst': 'Management',
    'Senior Human Resources Coordinator': 'Human Resources',
    'Senior UX Designer': 'Design',
    'Junior Product Manager': 'Management',
    'Senior Marketing Specialist': 'Marketing',
    'Senior IT Project Manager': 'Information Technology',
    'Senior Quality Assurance Analyst': 'Information Technology',
    'Director of Sales and Marketing': 'Sales',
    'Senior Account Executive': 'Sales',
    'Director of Business Development': 'Business',
    'Junior Social Media Manager': 'Marketing',
    'Senior Human Resources Specialist': 'Human Resources',
    'Senior Data Analyst': 'Information Technology',
    'Director of Human Capital': 'Human Resources',
    'Junior Advertising Coordinator': 'Marketing',
    'Junior UX Designer': 'Design',
    'Senior Marketing Director': 'Marketing',
    'Senior IT Consultant': 'Information Technology',
    'Senior Financial Advisor': 'Finance',
    'Junior Business Operations Analyst': 'Business',
    'Junior Social Media Specialist': 'Marketing',
    'Senior Product Development Manager': 'Product Development',
    'Junior Operations Manager': 'Management',
    'Senior Software Architect': 'Information Technology',
    'Junior Research Scientist': 'Science',
    'Senior Financial Manager': 'Finance',
    'Senior HR Specialist': 'Human Resources',
    'Senior Data Engineer': 'Information Technology',
    'Junior Operations Coordinator': 'Management',
    'Director of HR': 'Human Resources',
    'Senior Operations Coordinator': 'Management',
    'Junior Financial Advisor': 'Finance',
    'Director of Engineering': 'Engineering',
    'Software Engineer Manager': 'Information Technology',
    'Back end Developer': 'Information Technology',
    'Senior Project Engineer': 'Engineering',
    'Full Stack Engineer': 'Information Technology',
    'Front end Developer': 'Information Technology',
    'Front End Developer': 'Information Technology',
    'Director of Data Science': 'Information Technology',
    'Human Resources Coordinator': 'Human Resources',
    'Junior Sales Associate': 'Sales',
    'Human Resources Manager': 'Human Resources',
    'Juniour HR Generalist': 'Human Resources',
    'Juniour HR Coordinator': 'Human Resources',
    'Digital Marketing Specialist': 'Marketing',
    'Receptionist': 'Administrative',
    'Marketing Director': 'Marketing',
    'Social Media Man': 'Marketing',
    'Delivery Driver': 'Logistics',
    'Information Technology': 'Information Technology',
    'Management': 'Management',
    'Sales': 'Sales',
    'Marketing': 'Marketing',
    'Science': 'Science',
    'Human Resources': 'Human Resources',
    'Finance': 'Finance',
    'Customer Service': 'Customer Service',
    'Engineering': 'Engineering',
    'Business': 'Business',
    'Design': 'Design',
    'Administrative': 'Administrative',
    'Event Planning': 'Event Planning',
    'Research': 'Research',
    'Logistics': 'Logistics',
    'Training': 'Training',
    'Media': 'Media',
    'Product Development': 'Product Development'
}

df['Industry'] = df['Job Title'].map(industry_mapping)
df.drop(columns='Job Title', inplace=True)

encoder = BinaryEncoder(cols=['Industry'])
df = encoder.fit_transform(df)

df = df.iloc[:1]

load_model = pickle.load(open('random_forest_model.pkl', 'rb'))

prediction = load_model.predict(df)
#prediction_str = prediction.ToString()

st.markdown("""
<style>
    .box {   
        padding: 20px;
        border: 2px solid #ccc;
        border-radius: 10px;
        text-align: center;
    }
        
    .box h3 {
        padding: 0;
    }
    
    .box p {
        margin: 0;
    }
        
    .box hr {
        margin-top: 10px;
        margin-bottom: 10px;
        margin-right: 100px;
        margin-left: 100px;
        border: 1px solid #ccc;
    }
    
    .box table {
        opacity: 0.7;
        margin: 50px auto;
    }
    
    .box th, .box td {
        border: 1px solid #ccc;
        padding: 8px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="box">
    <h3>Salary Prediction App</h3>
    <hr>
    <p>Use the elements in the sidebar to predict a salary based on certain details.</p>
    <table>
        <tr>
            <th>Predicted Salary</th>
        </tr>
        <tr>
            <td>${:.2f}</td>
        </tr>
    </table>
</div>

""".format(prediction[0]), unsafe_allow_html=True)

