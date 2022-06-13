import streamlit as st
import pickle
import numpy as np


#import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))


st.title("Laptop Price Predictor")

# brand
company = st.selectbox('Brand',df['Company'].unique())

# type of laptop
typename = st.selectbox('Type',df['TypeName'].unique())

# Type of ram
ram = st.selectbox('Ram(in GB',df['Ram'].unique())

# Weight
weight = st.number_input('Weight of laptop')

# Touchscreen
touchscreen = st.selectbox('Touchscreen',['No','Yes'])

# Ips
ips = st.selectbox('ips',['No','Yes'])

# screen size
screen_size = st.number_input('Screen size')

# resolution
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

#Cpu
cpu = st.selectbox('Cpu',df['Cpu_brand'].unique())

#hdd
hdd = st.selectbox('HDD(in Gb',[0,128,256,512,1024,2048])

#ssd
ssd = st.selectbox('SSD(in Gb',[0,128,256,512,1024])

#Gpu
gpu = st.selectbox('Gpu',df['Gpu_brand'].unique())

#OS
os = st.selectbox('Cpu',df['Os'].unique())

if st.button('Predict Price'):
    x_res = int(resolution.split('x')[0])
    y_res = int(resolution.split('x')[1])
    ppi =((x_res**2)+(y_res**2))**0.5/screen_size


    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    query = np.array([company,typename,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])
    query = query.reshape((1,12))
    st.title('The Price of this Laptop is ' + str(int(np.exp(pipe.predict(query)[0]))))