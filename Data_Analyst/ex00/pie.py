import psycopg2
import matplotlib.pyplot as plt
import numpy as np

def main():
    try:
        connection = psycopg2.connect(host='localhost', port='5432', database="piscineds",
                                      user='hasabir', password='mysecretpassword')
        cursor = connection.cursor()
  
        cursor.execute("SELECT event_type FROM customers")
        rows = cursor.fetchall()
        connection.commit()
        
        
        
        rows = np.array([row[0] for row in rows])
        lables, counts = np.unique(rows, return_counts=True)
        print(lables, counts)
        
        
        colors = ['blue', 'orange', 'green', 'red']
        plt.pie(counts, labels=lables, colors=colors, autopct='%1.1f%%',
                wedgeprops={'linewidth': 1.0, 'edgecolor': 'white'})
        plt.show() 
    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:  
            connection.close()
        print("Connection closed")
        
        
        
        
if __name__ == "__main__":
    main()
