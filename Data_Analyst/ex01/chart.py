import psycopg2
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter



def line_chart(cursor, event_time):
    
     # Extract the actual dates (day) from event_time
    event_time = np.array([date.date() for date in event_time])  # Using .date() to get just the date
    
    # Count occurrences for each day (the number of purchases per day)
    unique_days, counts = np.unique(event_time, return_counts=True)
    
    # Now unique_days are the days and counts are the number of purchases for each day
    print(unique_days, counts)  # Print to check if the counts align with your data
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_facecolor('lightgray')
    
    ax.plot(unique_days, counts, color='blue', marker='o', zorder=3)  # Plot the data with markers
    
    ax.set_ylabel('Number of customers')
    ax.set_yticklabels([0, 500, 1000, 1500, 2000])
    
    ax.set_xticks(np.unique[month for month in unique_days])
    ax.set_xticklabels(['Oct', 'Nov', 'Dec', 'Jan'])
    ax.grid(color='white')
    plt.show()
    
    
def bar_chart(cursor, event_time):
        event_months = [date.strftime('%b') for date in event_time]
        month_counts = Counter(event_months)
        months = ['Oct', 'Nov', 'Dec', 'Jan']  # Focus on these months
        counts = [month_counts.get(month, 0) for month in months]  # Ensure all months are represented

        fig, ax = plt.subplots()
        ax.set_facecolor('lightgray')
        
        ax.bar(months, counts, color='gray', zorder=3)
        
        
        ax.set_ylabel('total sales in millions')
        ax.set_yticklabels([0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2])
        ax.set_xlabel('months')
        ax.grid(axis='y', color='white')
        plt.show()



def histogram(cursor):
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

        line_chart(cursor, event_time)
        bar_chart(cursor, event_time)

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