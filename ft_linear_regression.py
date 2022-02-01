import pandas as pd
import matplotlib.pyplot as plt
import sys

class LinearRegression:
    __theta0 = 0
    __theta1 = 0

    def __init__(self, filename):
        self.__data = pd.read_csv(filename)
        self.__data0 = pd.read_csv(filename)
        self.__m = len(self.__data['km'])
        
    def estimatePrice(self, x):
        return (self.__theta0 + (self.__theta1 * x))

    def print_data(self):
        print('km' , 'price')
        for i in range(self.__m):
            print(self.__data['km'][i], self.__data['price'][i])

    def linear_regression_training(self, learningRate = 1, learningRateStep = 0.1, iterations = 100, epsilon = 0.00001):
        m = self.__m

        while True:
            convergence_count = 0

            for i in range(iterations):
                theta0_sum, theta1_sum = 0.0, 0.0
                for i in range(m):
                    theta0_sum += (self.estimatePrice(self.__data['km'][i]) - self.__data['price'][i])
                    theta1_sum += ((self.estimatePrice(self.__data['km'][i]) - self.__data['price'][i]) * self.__data['km'][i])
                # if (self.__theta0 - ((learningRate/m) * theta0_sum) <= epsilon and self.__theta1 - ((learningRate/m) * theta1_sum) <= epsilon):
                #     convergence_count += 1
                # else:
                #     convergence_count = 0
                self.__theta0 -=  (theta0_sum / m * learningRate)
                self.__theta1 -=  (theta1_sum / m * learningRate)
                # plt.scatter(self.__theta0, self.__theta1)
                # print(self.__theta0, self.__theta1, theta0_sum, theta1_sum)

            # if (convergence_count >= 100):
            # plt.show()
            self.denormalize_tetha()
            break
            learningRate -= learningRateStep
    
    def plot_data(self):
        plt.scatter(self.__data['km'], self.__data['price'])

    def plot_result(self):
        x = self.__data['km']
        y = self.__theta0 + self.__theta1 * x
        plt.plot(x, y , '-g')

    def normalisation(self):
        i = 0
        min_km = min_price =  (2**64)
        max_km = max_price = -1 * (2**64)

        for i in range(self.__m):
            min_km = min(self.__data['km'][i], min_km)
            min_price = min(self.__data['price'][i], min_price)
            max_km = max(self.__data['km'][i], max_km)
            max_price = max(self.__data['price'][i], max_price)
        for i in range(self.__m):
            self.__data['km'][i] = (float(self.__data['km'][i]) - min_km) /  (max_km - min_km)
            self.__data['price'][i] = (float(self.__data['price'][i]) - min_price) /  (max_price - min_price)
    
    def denormalize_tetha(self):
        i = 0
        min_km = min_price =  (2**64)
        max_km = max_price = -1 * (2**64)
        data = self.__data0

        for i in range(self.__m):
            min_km = min(data['km'][i], min_km)
            min_price = min(data['price'][i], min_price)
            max_km = max(data['km'][i], max_km)
            max_price = max(data['price'][i], max_price)
        x = (0 - min_km) / (max_km - min_km)
        theta0 = (self.estimatePrice(x) * (max_price - min_price) + min_price)
        theta1 = (self.estimatePrice(self.__data['km'][0]) * (max_price - min_price) + min_price - theta0) / self.__data0['km'][0]
        print('minmax', (max_price - min_price) , min_price)
        print ('thetas', self.__theta0, self.__theta1)
        print ('theta0', theta0, theta1)
        

lr = LinearRegression('data.csv')

lr.normalisation()
lr.linear_regression_training(0.1, 0.001, 1200)

# data = pd.read_csv('data.csv')
# print(data['km'][0], data['price'][0], lr.estimatePrice(data['km'][0]))
# print(data['km'][1], data['price'][1], lr.estimatePrice(data['km'][1]))
# print(data['km'][2], data['price'][2], lr.estimatePrice(data['km'][2]))

lr.plot_data()
lr.plot_result()
plt.show()