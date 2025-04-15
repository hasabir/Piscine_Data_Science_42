import psycopg2
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import pandas as pd

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

def area_chart(data, event_time):
    spends = {}
    users = {}

    data['date'] = [date.date() for date in event_time]
    for _, row in data.iterrows():
        time_key = row['date']
        user_id = row['user_id']
        
        if time_key not in spends:
            spends[time_key] = row['price']
            users[time_key] = {user_id}
        else:
            spends[time_key] += row['price']
            users[time_key].add(user_id)

    average_spent_by_customers = [spends[time_key] / len(users[time_key]) for time_key in spends.keys()]


    x = list(spends.keys())
    y = list(average_spent_by_customers)
    
    _, ax = plt.subplots()
    
    ax.set_xlim([x[0], x[-1]])
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    
    ax.set_ylim(0, max(y) + 1)
    
    ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
    ax.set_ylabel('Average spend/customers in ₳')
    
    ax.set_facecolor('lightgray')
    plt.fill_between(x, y, zorder=3)
    ax.grid(color='white')
    plt.show()




def main():
    try:
        connection = psycopg2.connect(host='localhost', port='5432', database="piscineds",
                                      user='hasabir', password='mysecretpassword')
        cursor = connection.cursor()
        with open("chart.sql", 'r') as file:
            query = file.read()
        cursor.execute(query)
        data = cursor.fetchall()
        
        
        data = pd.DataFrame(data, columns=['event_time', 'user_id', 'price'])
        event_time = [pd.Timestamp(date).to_pydatetime() for date in data['event_time'].values]
        line_chart(event_time)
        


        bar_chart(event_time)
        
        
        area_chart(data, event_time)

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





