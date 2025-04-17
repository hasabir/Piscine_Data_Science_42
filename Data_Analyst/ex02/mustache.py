import psycopg2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def get_summary_statistics(prices):
    stats = {
        'count': len(prices),
        'mean': np.mean(prices),
        'std': np.std(prices),
        'min': np.min(prices),
        '25%': np.quantile(prices, 0.25),
        '50%': np.quantile(prices, 0.5),
        '75%': np.quantile(prices, 0.75),
        'max': np.max(prices),
    }
    for key, value in stats.items():
        print(f'{key:<12}{value:>12.5f}')
    return stats


# def get_average_price_per_customer(prices, users):
#     customer_totals = {}
#     customer_counts = {}
    
#     for user_id, price in zip(users, prices):
#         if user_id not in customer_totals:
#             customer_totals[user_id] = price
#             customer_counts[user_id] = 1
#         else:
#             customer_totals[user_id] += price
#             customer_counts[user_id] += 1
    
#     return [customer_totals[user_id] / customer_counts[user_id] for user_id in customer_totals]



def fetch_price_data():
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(
            host='localhost',
            port='5432',
            database='piscineds',
            user='hasabir',
            password='mysecretpassword'
        )
        cursor = connection.cursor()
        with open("mustache.sql", 'r') as file:
            query = file.read()
        cursor.execute(query)
        results = cursor.fetchall()
        prices = np.array([float(price) for _, price in results])
        users = np.array([users for users, _ in results])
        return prices, users
    except psycopg2.Error as e:
        print(f"Database error: {e}")
        return np.array([])
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print("Connection closed")


def plot_boxplot(price=None, zoom=False, average_price_per_customer=None):
    fig, ax = plt.subplots()
    ax.set_facecolor('lightgray')
    ax.set_xlabel("price")
    ax.grid(color='white', axis='x')

    box = ax.boxplot(
        price if price is not None else average_price_per_customer,
        vert=False,
        patch_artist=True,
        showfliers=not zoom,
        flierprops=dict(marker='D',
                        markerfacecolor='#556B2F',
                        markeredgecolor='#556B2F',
                        markersize=4)
    )

    for patch in box['boxes']:
        patch.set_facecolor('green') if price is not None else patch.set_facecolor('blue')
        patch.set_edgecolor('black')
    
    
    for median in box['medians']:
        median.set_color('black')
    
    ax.set_ylim(0.9, 1.1)
    if zoom:
        ax.set_xlim(-0.75, 12)
    elif average_price_per_customer is not None:
        ax.set_xlim(26, 43)

    plt.show()





def main():
    prices, users = fetch_price_data()
    if prices.size == 0 or users.size == 0:
        print("No data available.")
        return

    get_summary_statistics(prices)
    # average_price_per_customer = get_average_price_per_customer(prices, users)
    plot_boxplot(prices)
    plot_boxplot(prices, zoom=True)
    # plot_boxplot(average_price_per_customer=average_price_per_customer)


if __name__ == "__main__":
    main()
