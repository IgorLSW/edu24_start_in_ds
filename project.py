# Итоговый проект (Анализ зарплат в России)

# импортируем библиотеку streamlit
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# заголовок приложения
st.title('Итоговый проект')
st.title('Анализ зарплат в России')

# Загрузка изображения
st.image('ds.png', caption='Старт в Data Science!')

st.header('Старт в Data Science!')
st.subheader(':blue[_Описание курса_] :rocket:', divider='rainbow')

st.write(
    """
Главной целью этого курса является обучение слушателей основам Python и аналитики - для последующей успешной карьеры в области анализа данных. Также слушатели познакомятся с инструментом Streamlit для создания красивых интерактивных сервисов и дашбордов.

Курс проводится командой магистратуры "Машинное обучение и высоконагруженные системы" факультета компьютерных наук ВШЭ.
    """
)

st.write(
    """
    ### About Dataset
В проекте используются открытые данные из официальных источников:

[Сайт Росстата](https://rosstat.gov.ru/)

[Таблицы уровня инфляции в России](https://уровень-инфляции.рф/)


Данные по заработной плате получены из таблицы 
"Среднемесячная номинальная начисленная заработная плата работников в целом по экономике по субъектам Российской Федерации за 2000-2023 гг." 
https://rosstat.gov.ru/storage/mediabank/tab3-zpl_2023.xlsx


Данные об уровне инфляции в стране получены с сайта 
[https://уровень-инфляции.рф/](https://уровень-инфляции.рф/%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D1%8B-%D0%B8%D0%BD%D1%84%D0%BB%D1%8F%D1%86%D0%B8%D0%B8)

Валовой внутренний продукт, ВВП годы (с 1995 г.) 
https://rosstat.gov.ru/storage/mediabank/VVP_god_s_1995.xlsx

ВВП на душу населения 
https://rosstat.gov.ru/storage/mediabank/VVP_na_dushu_s_1995.xlsx

Индекс производительности труда 
https://rosstat.gov.ru/storage/mediabank/Index_proizv_truda(06102023).xlsx

    """
)



# загрузка данных

# Инфляция и заработная плата
#df = pd.read_csv('data.csv', sep=';')
df = st.cache_data(pd.read_csv)("data.csv", sep=';')

# Индексы физического объема валового внутреннего продукта
# (в процентах к предыдущему году)
#df_vvp = pd.read_csv('vvp_index.csv', sep=';')
df_vvp = st.cache_data(pd.read_csv)("vvp_index.csv", sep=';')

# Индексы физического объема валового внутреннего продукта на душу населения
# (в процентах к предыдущему году)
#df_vvp_nd = pd.read_csv('vvp_index_dn.csv', sep=';')
df_vvp2 = st.cache_data(pd.read_csv)("vvp_index_dn.csv", sep=';')

# Индекс производительности труда в экономике Российской Федерации в 2003-2022 гг.
# (в % к предыдущему году)
#df_ipt = pd.read_csv('ipt.csv', sep=';')
df_ipt = st.cache_data(pd.read_csv)("ipt.csv", sep=';')



st.subheader(':blue[_1. Среднемесячная номинальная начисленная заработная плата работников по отраслям_] :chart_with_upwards_trend:', divider='rainbow')
cl = df.columns  # выбираем последние 5 колонок
chart_zp = pd.DataFrame(df, columns=cl)
st.line_chart(chart_zp, x=cl[0], y=cl[2:])

st.markdown('Данные представлены в таблице 1')
show_data = st.sidebar.checkbox('Таблица 1')
if show_data == True:
    st.markdown('##### Среднемесячная номинальная начисленная заработная плата работников по отраслям')
    st.markdown('##### Таблица 1')
    st.write(df)



st.subheader(':blue[_2. Инфляция_] :chart_with_downwards_trend:', divider='rainbow')

st.markdown('##### Годовая инфляция')
cl = df.columns  # выбираем последние 5 колонок
chart_zp = pd.DataFrame(df, columns=cl)
st.line_chart(chart_zp, x=cl[0], y=cl[1])

st.markdown('##### Суммарная инфляцию относительно 2000 года')
df1 = pd.DataFrame()
df1[['Год', 'Инфляция']] = df[['Год', 'Инфляция']]
df1['Суммарная инфляция'] = df['Инфляция'].cumsum()

cl = df1.columns  # выбираем последние 2 колонок
chart_inf = pd.DataFrame(df1, columns=cl)
st.line_chart(chart_inf,x=cl[0], y=cl[1:], color=["#00aaff",'#ff0000'])

st.markdown('Данные представлены в таблице 2')
show_data = st.sidebar.checkbox('Таблица 2')
if show_data == True:
    st.markdown('##### Инфляция')
    st.markdown(
        "##### Таблица 2 ")
    st.write(df1)



st.subheader(':blue[_3. Реальная среднемесячная заработная плата с учетом инфляции_] :chart_with_upwards_trend:', divider='rainbow')

df_real = df.copy()
for column in df.columns[-5:]:
    df_real[column] = (df_real[column] / (1 + df['Инфляция'] / 100)).astype(int)

cl = df_real.columns  # выбираем последние 5 колонок
chart_zp = pd.DataFrame(df_real, columns=cl)
st.line_chart(chart_zp, x=cl[0], y=cl[2:])

st.markdown('Данные представлены в таблице 3')
show_data = st.sidebar.checkbox('Таблица 3')
if show_data == True:
    st.markdown('##### Реальная среднемесячная заработная плата с учетом инфляции')
    st.markdown('##### Таблица 3')
    st.write(df_real)



st.subheader(':blue[_4. Сравнение номинальной и реальной заработной платы_] :chart_with_upwards_trend:', divider='rainbow')

df_r = df_real.add_prefix('Реальные_')
df_comp = pd.merge(df, df_r, left_on='Год', right_on='Реальные_Год')

cl = df_comp.columns  # выбираем последние 5 колонок
chart_comp = pd.DataFrame(df_comp, columns=cl)

st.markdown('##### Среднемесячная заработная плата - Всего по экономике')
st.line_chart(chart_comp, x=cl[0], y=cl[[2, 9]])

st.markdown('##### Среднемесячная заработная плата')
st.markdown('##### Добыча топливно-энергетических полезных ископаемых')
st.line_chart(chart_comp, x=cl[0], y=cl[[4, 11]])



st.subheader(':blue[_5. Динамика изменения заработной платы_] :chart_with_downwards_trend:', divider='rainbow')

st.write('Посчитаем процент изменения зарплаты относительно предыдущего года')
df2 = pd.DataFrame()
df2[['Год', 'Инфляция']] = df[['Год', 'Инфляция']]
for col in df.columns[2:]:
    df2[col+' % изменения'] = (df[col].pct_change() * 100).round(2)
df2.fillna(value=0, inplace=True)

cl = df2.columns  # выбираем последние 5 колонок
chart_d = pd.DataFrame(df2, columns=cl)
st.line_chart(chart_d, x=cl[0], y=cl[2:])

st.write(' ')
st.write('Рассмотрим подробнее некоторые отрасли')

st.markdown('##### Динамика изменения заработной платы в сельском хозяйстве, в % к предыдущему году')
st.line_chart(chart_d, x=cl[0], y=cl[[1,2,3]])

st.markdown('##### Динамика изменения заработной платы')
st.markdown('##### Добыча топливно-энергетических полезных ископаемых')
st.line_chart(chart_d, x=cl[0], y=cl[[1,2,4]])

st.markdown('Данные представлены в таблице 4')
show_data = st.sidebar.checkbox('Таблица 4')
if show_data == True:
    st.markdown('##### Динамика изменения заработной платы')
    st.write('(в процентах к предыдущему году)')
    st.markdown('##### Таблица 4')
    st.write(df2)



st.subheader(':blue[_6. Индексы валового внутреннего продукта ВВП_] :bar_chart:', divider='rainbow')

st.markdown('##### Индексы физического объема валового внутреннего продукта')
cl = df_vvp.columns  # выбираем последние 5 колонок
chart_vvp = pd.DataFrame(df_vvp, columns=cl)
st.line_chart(chart_vvp, x=cl[0], y=cl[1])

st.markdown('Данные представлены в таблице 5')
show_data = st.sidebar.checkbox('Таблица 5')
if show_data == True:
    st.markdown('##### Индексы физического объема валового внутреннего продукта')
    st.write('(в процентах к предыдущему году)')
    st.markdown('##### Таблица 5')
    st.write(df_vvp)


st.markdown('##### Индексы физического объема валового внутреннего продукта на душу населения')
cl = df_vvp2.columns  # выбираем последние 5 колонок
chart_vvp = pd.DataFrame(df_vvp2, columns=cl)
st.bar_chart(chart_vvp, x=cl[0], y=cl[1])

st.markdown('Данные представлены в таблице 6')
show_data = st.sidebar.checkbox('Таблица 6')
if show_data == True:
    st.markdown('##### Индексы физического объема валового внутреннего продукта на душу населения')
    st.write('(в процентах к предыдущему году)')
    st.markdown('##### Таблица 6')
    st.write(df_vvp2)



st.subheader(':blue[_7. Индекс производительности труда_] :chart_with_downwards_trend:', divider='rainbow')

cl = df_ipt.columns  # выбираем последние 4 колонок
chart_d = pd.DataFrame(df_ipt, columns=cl)
st.line_chart(chart_d, x=cl[0], y=cl[1:])


st.markdown('Данные представлены в таблице 7')
show_data = st.sidebar.checkbox('Таблица 7')
if show_data == True:
    st.markdown('##### Индекс производительности труда')
    st.write('(в процентах к предыдущему году)')
    st.markdown('##### Таблица 7')
    st.write(df_ipt)



st.subheader(':blue[_8. Выводы_] :rocket:', divider='rainbow')

st.markdown('''
- Наблюдается значительное расслоение уровня зарплат по отраслям.
- Рост уровня зарплат опережает официальную инфляцию, но постепенно снижается.
- Рост уровня зарплат по всей видимости, не связан с ростом производительности труда.
- Наблюдаются тренды к снижению:
    - уровня инфляции, 
    - прироста ВВП на душу населения, 
    - темпов роста производительность труда
- Сравнение данных Росстата со своей персональной зарплатой вызывает недоверие к статистике как науке. )
''')

st.markdown('Более подробно визуализация представлена в файле project.ipynb')



if st.button('Finish'):
    st.balloons()

