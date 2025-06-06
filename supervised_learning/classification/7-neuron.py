#!/usr/bin/env python3
"""
    Class Neuron
"""

import numpy as np


class Neuron:
    """
        Class Neuron : define single neuron performing binary classification
    """

    def __init__(self, nx):
        """
        class constructor
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """
            The weights vector for the neuron

            :return: value for private attribute __W
        """
        return self.__W

    @property
    def b(self):
        """
            The bias for the neuron

            :return: value for private attribute __b
        """
        return self.__b

    @property
    def A(self):
        """
            The activated output of the neuron (prediction)

            :return: value for private attribute __A
        """
        return self.__A

    def forward_prop(self, X):
        """
            method to calculate the forward propagation of the neuron

            :param X: ndarray (shape (nx, m)) contains input data

            :return: forward propagation
        """
        # multiplication of weight and add bias
        Z = np.matmul(self.__W, X) + self.__b

        # activation function
        self.__A = 1 / (1 + np.exp(-Z))

        return self.__A

    def cost(self, Y, A):
        """
            Method to calculate cost (using logistic regression)

            :param Y: ndarray shape(1,m) correct labels
            :param A: ndarray shape(1,m) activated output

            :return: the cost
        """
        # store m value
        m = Y.shape[1]

        # calculate log loss function
        log_loss = -(1 / m) * np.sum((Y * np.log(A) + (1-Y) *
                                      np.log(1.0000001 - A)))

        return log_loss

    def evaluate(self, X, Y):
        """
        Method to evaluate the neuron's prediction

        :param X: ndarray shape(nx,m) contains input data
        :param Y: ndarray shape (1,m) correct labels

        :return: neuron's prediction and cost of the network
        """

        # run forward propagation
        A = self.forward_prop(X)

        # calculate cost
        cost = self.cost(Y, A)

        # label values
        result = np.where(A >= 0.5, 1, 0)

        return result, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """
            Method calculate one pass of gradient descent on the neuron

            :param X: ndarray, shape(nx,m) contains input data
            :param Y: ndarray, shape(1, m) correct labels
            :param A: ndarray, shape(1,m) activated output
            :param alpha: learning rate

            :return: one pass of gradient descent on the neuron
        """

        # store m
        m = X.shape[1]

        # calculate weight gradient with X transpose
        grad_w = 1 / m * np.matmul((A-Y), X.T)

        # calculate bias gradient
        grad_b = 1/m * np.sum((A-Y))

        # update parameters W and b
        self.__W = self.__W - alpha * grad_w
        self.__b = self.__b - alpha * grad_b

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """
            Method to train neuron

            :param X: ndarray, shape(nx,m) contains input data
            :param Y: ndarray, shape(1, m) correct labels
            :param iterations: number of iterations
            :param alpha: learning rate

            :return: evaluation of the training data after iterations
        """

        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations < 0:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha < 0:
            raise ValueError("alpha must be positive")

        for i in range(iterations):
            # run forward propagation
            A = self.forward_prop(X)
            # run gradient descent
            self.gradient_descent(X, Y, A, alpha)
            # run evaluate
            result, cost = self.evaluate(X, Y)

        return result, cost

    def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True, graph=True, step=100):
        """
        trains the neuron and updates __W, __b, and __A
        """
        if type(iterations) is not int:
            raise TypeError("iterations must be an integer")
        if iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        if type(alpha) is not float:
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")

        if graph:
            import matplotlib.pyplot as plt
            x_points = np.arange(0, iterations + 1, step)
            points = []

        for itr in range(iterations):
            A = self.forward_prop(X)
            if verbose and itr % step == 0:
                cost = self.cost(Y, A)
                print(f"Cost after {itr} iterations: {cost}")
            if graph and itr % step == 0:
                points.append(self.cost(Y, A))
            self.gradient_descent(X, Y, A, alpha)

        if verbose:
            cost = self.cost(Y, A)
            print(f"Cost after {iterations} iterations: {cost}")

        if graph:
            points.append(self.cost(Y, A))
            plt.plot(x_points, points, 'b')
            plt.xlabel("Iteration")
            plt.ylabel("Cost")
            plt.title("Training Cost")
            plt.show()

        return self.evaluate(X, Y)
