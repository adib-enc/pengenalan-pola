# Membaca data dari file dengan format CSV
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def readCsvs():
    data = pd.read_csv("./data/data.csv", sep=";")
    print(data)

    # Membaca data dari file dengan format text (delimeter)
    print("\n read text data with tab delimiter")
    with open('./data/data.txt') as data:
        print(data.read())

    # Membaca data dari URL
    f = pd.read_csv('http://www.exploredata.net/ftp/Spellman.csv')
    print(f)

def plots():
    # fname = "https://raw.githubusercontent.com/rwepa/DataDemo/master/web_traffic.csv"
    fname = "./data/web_traffic.csv"
    traffic = np.genfromtxt(fname, delimiter='\t')
    print(traffic[:10])
    print(traffic.shape)

    x = traffic[:,0]
    y = traffic[:,1]

    x = x[~np.isnan(y)]
    y = y[~np.isnan(y)]
 
    plt.scatter(x,y)
    plt.title("Web traffic last month")
    plt.xlabel("Time")
    plt.ylabel("Hits/hour")

    plt.xticks([w*7*24 for w in range(10)],['week %i' %w for w in range(10)])
    plt.autoscale(tight=True)
    plt.grid()
    plt.show()

data = pd.read_csv("./sakit.csv")
print(data)

readCsvs()
plots()
