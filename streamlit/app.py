# Домашнее задание (Streamlit)

# импортируем библиотеку streamlit
import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt


# заголовок приложения
st.title('Домашнее задание (Streamlit)')

# Загрузка изображения
st.image('start.png', caption='Старт')

st.header('Space Mission Launches')
st.subheader(':blue[_Запуски космических миссий_] :rocket:', divider='rainbow')

st.write(
    """
    ### About Dataset
    You'll find an incredibly rich dataset from nextspaceflight.com that includes all the space missions since the beginning of Space Race between the USA and the Soviet Union in 1957! It has data on the mission status (success/failure), the cost of the mission, the number of launches per country, and much much more. There's so much we can learn from this dataset about the dominant organisations and the trends over time. For example:
    
    Who launched the most missions in any given year?
    
    How has the cost of a space mission varied over time?
    
    Which months are the most popular for launches?
    
    Have space missions gotten safer or has the chance of failure remained unchanged?


    ##### Адрес dataset на Kaggle: 
    https://www.kaggle.com/datasets/sefercanapaydn/mission-launches?select=mission_launches.csv
    
    """
)


# загрузка данных
# https://www.kaggle.com/datasets/sefercanapaydn/mission-launches?select=mission_launches.csv

df = st.cache_data(pd.read_csv)("mission_launches.csv", parse_dates=['Date'])
df = df.drop(columns=['Unnamed: 0.1', 'Unnamed: 0','Rocket_Status', 'Price'])
col = df.columns
# колонки
#st.write(col)


st.subheader('Status Space Mission Launches')

mission_counts = df['Mission_Status'].value_counts()

st.write(mission_counts)

#chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
chart_data = sorted(mission_counts,reverse=True)
st.bar_chart(chart_data)


# status_names = mission_counts
# status_counts = mission_counts.tolist()
# # st.write(status_names)
#
#
# index_list = mission_counts.index.tolist()[0:3]
# status_counts = mission_counts.tolist()[0:3]

# # создаем круговую диаграмму
# fig, ax = plt.subplots()
# # задаем размер круговой диаграммы
# plt.figure(figsize=(8, 6))
# ax.pie(status_counts, labels=index_list, autopct='%1.1f%%', startangle=90)
# ax.axis('equal')
#
# # отображаем круговую диаграмму в Streamlit
# st.pyplot(fig)



show_data = st.sidebar.checkbox('Космодромы')
if show_data == True:
    st.subheader('Космодромы')
    st.markdown(
        "#### Location Space Mission Launches.")
    location_counts = df['Location'].value_counts()
    st.write(location_counts)


show_data = st.sidebar.checkbox('Организации')
if show_data == True:
    st.subheader('Организации')
    st.markdown(
        "#### Organisation Space Mission Launches.")
    org_counts = df['Organisation'].value_counts()
    st.write(org_counts)


show_data = st.sidebar.checkbox('Таблица')
if show_data == True:
    st.subheader('Таблица')
    st.markdown(
        "#### Data Space Mission Launches.")
    st.write(df)



if st.button('Finish'):
    st.balloons()

