import psycopg2
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import matplotlib.dates as mdates

def line_chart(event_time):

    dates = np.array([date.date() for date in event_time])
    unique_dates, counts = np.unique(dates, return_counts=True)
    
    _ , ax = plt.subplots()
    ax.set_facecolor('lightgray')
    ax.plot(unique_dates, counts) 

    ax.set_ylabel('Number of customers')
    ax.set_yticklabels([0, 500, 1000, 1500, 2000])
    
    ax.set_xlim([unique_dates[0], unique_dates[-1]])
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

 
    ax.grid(color='white')


    plt.show()


def bar_chart(event_time):
    event_months = [date.strftime('%b') for date in event_time]
    month_counts = Counter(event_months)
    months = ['Oct', 'Nov', 'Dec', 'Jan']
    counts = [month_counts[month] for month in months]

    _, ax = plt.subplots()
    ax.set_facecolor('lightgray')
    
    ax.bar(months, counts, zorder=3)
    
    
    ax.set_ylabel('total sales in millions')
    ax.set_yticklabels([0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2])
    ax.set_xlabel('months')
    ax.grid(axis='y', color='white')
    plt.show()

def area_chart(event_time):
    ...


def main():
    try:
        connection = psycopg2.connect(host='localhost', port='5432', database="piscineds",
                                      user='hasabir', password='mysecretpassword')
        cursor = connection.cursor()
        with open("chart.sql", 'r') as file:
            function_queries = file.read()
        cursor.execute(function_queries)
        connection.commit()
        
        
        # set the x axis
        cursor.execute("SELECT * FROM get_event_time()")
        event_time = cursor.fetchall()
        connection.commit()
        event_time = np.array([(number[0]) for number in event_time])

        line_chart(event_time)


        bar_chart(event_time)
        area_chart(event_time)

    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
        return
    finally:
        if cursor:
            cursor.close()
        if connection:  
            connection.close()
        print("Connection closed")
        
        
        
if __name__ == "__main__":
    main()










        # cursor.execute("SELECT * FROM get_price()")
        # prices = cursor.fetchall()
        # connection.commit()
        # # print(prices[0][0])
        # prices = np.array([(number[0]) for number in prices])
















