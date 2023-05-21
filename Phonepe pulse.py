import mysql.connector
import pandas as pd
import streamlist as st
import PIL
from PIL import Image
from steamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd

import requests

#connect to the database
import mysql.connector
conn = mysql.connector.connect(user='root', password='Ajith_suba99', host='3306', database='phonepe_pulse"')
cursor = conn.cursor()

#sidebar

SELECT = option_menu(
    menu_title = None,
    options = ["About","Home","Basic insights","Contact"],
    icons = ["bar-chart","hpuse","toggles","at"],
    default_index=2,
    orientation='horizontal',
    styles={"container":{'padding':"0!important","background-color": "whilte","size":"cover","width":"100%"},
            "icon":{"color":"black", "font-size": "20px"},
            "nav-link": {"font-size": "20px", "text-align":"center", "margin": "-2px","--hover-color":"#6F36AD"},
            "nac-link-selected": {"backgrund-color":"#6F36AD"}})


#Basic Insights


if SELECT == "Basic insights":
    st.title("BASIC INSIGHTS")
    st.write("---")
    st.subheader("Let's know some basic insights about the data")
    options = ["--select--",
               "Top 10 states based on year and amount of transaction",
               "List 10 states based on type and amount of transaction",
               "Top 5 Transaction_Type based on Transaction_Amount"
               "Top 10 Registered-users based on States and District",
               "Top 10 Districts based on states and Count of transaction",
               "list 10 Disctricts based on states and amount of transaction",
               "List 10 Transaction_Count based on Districts and states",
               "Top 10 RegisteredUsers based on states and District"]

    #1

    select = st.selectbox("Select the option",options)
    if select=="Top 10 states based on year and amount of transaction":
        cursor.execute("SELECT DISTINCT states, Transaction_Year, SUM(Transaction_Amount AS Total_Transaction_Amount FROM top_trans GROUP BY States,Transaction_Year)
                       df = pd.DataFrame(cursor,fetchall(), columns['States','Transaction_Year','Transaction_Amount'])
                       col1,col2 = st.columns(2)
                       with col1:
                           st.write(df)
                    with col2:
                        st.title("Top 10 states and amount of transaction")
                        st.bar_chart(data=df,x='Transaction_Amount',y="States")
    #2

    elif select=="List 10 states based on type and amount of transaction":
        cursor.execute("SELECT DISTINCT states, SUM(Transaction_Count) as Total FROM top_tran GROUP BY States ORDER BY Total ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['States','Total_Transaction'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("List 10 states based on type and amount of transaction")
            st.bar_chart(data=df,x="Total_Transaction",y="States")

    #3

    elif select=="Top 5 Transaction_Type based on Transaction_Amoun":
        cursor.execute("SELECT DISTINCT Transaction_Type, SUM(Transaction_Amount) AS Amount FROM agg_user GROUP BY Transaction_Type ORDER BY Amount");
        df = pd.DataFrame(cursor.fetchall(),columns=['Transaction_Type','Transaction_Amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 5 Transaction_Type based on Transaction_Amount")
            st.bar_chart(data=df,x="Transaction_Type",y="Amount")

    #4

    elif select=="Top 10 Registered-users based on States and District":
        cursor.execute("SELECT DISTINCT State, District, SUM(RegisteredUsers) AS Users FROM top_user GROUP BY State, District ORDER BY Users DESC LIST")
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District','RegisteredUsers'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 Registered-users based on States and District")
            st.bar_chart(data=df,x="State",y="RegisteredUsers")

    #5

    elif select=="Top 10 Districts based on states and Count of transaction":
        cursor.execute("SELECT DISTINCT States,District,SUM(Transaction_Count) AS Counts FROM map_tran GROUP BY States,District ORDER BY Counts DESC")
        df = pd.DataFrame(cursor.fetchall(),columns=['States','District','Transaction_Count'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 Districts based on states and Count of transaction")
            st.bar_chart(data=df,x="States",y="Transaction_Count")

    #6

    elif select=="List 10 Districts based on states and amount of transaction":
        cursor.execute("SELECT DISTINCT States,Transaction_year,SUM(Transaction_Amount) AS Amount FROM agg_trans GROUP BY States, Transaction_year ORDER BY States")
        df = pd.DataFrame(cursor.fetchall(),columns=['States','Transaction_year','Transaction_Amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Least 10 Districts based on states and amount of transaction")
            st.bar_chart(data=df,x="States",y="Transaction_Amount")

    #7

    elif select=="List 10 Transaction_Count