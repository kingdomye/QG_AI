import numpy as np
import moon
import matplotlib.pyplot as plt


def sigmoid(x):
    return (1 - np.exp(-2 * x)) / (1 + np.exp(-2 * x))


def sigmoid_derivative(x):
    return (1 - sigmoid(x)) * (1 + sigmoid(x))


class Neuron:
    def __init__(self, weights):
        self.weights = weights

    def get_output(self, inputs):
        weights_vector = self.weights.T
        v = np.sum(np.dot(weights_vector, inputs))
        return sigmoid(v)


class Layer:
    def __init__(self, inputs=None):
        self.inputs = inputs
        self.neurons = None

    def add_neurons(self, neurons):
        self.neurons = neurons

    def get_outputs(self):
        return np.array([neuron.get_output(self.inputs) for neuron in self.neurons])

    def get_weights(self):
        return np.array([neuron.weights for neuron in self.neurons])


class Network:
    def __init__(self):
        self.layers = None
        self.inputs = None

    def add_layer(self, layer):
        if self.layers is None:
            self.layers = [layer]
        else:
            self.layers.append(layer)

    def get_outputs(self):
        return self.layers[-1].get_outputs()

    def activate(self):
        for i in range(len(self.layers)):
            if i == 0:
                self.layers[i].inputs = self.inputs
            else:
                self.layers[i].inputs = self.layers[i-1].get_outputs()

    def show(self):
        for i in range(len(self.layers)):
            print("-----------------------------------------------")
            print(f'layer {i} weights:')
            print(self.layers[i].get_weights())
        print("=================================================================")


if __name__ == "__main__":
    input_layer = Layer()
    input_neurons = []
    for _ in range(2):
        weights_array = np.array([np.random.uniform(-1, 1) for _ in range(2)])
        input_neurons.append(Neuron(weights_array))
    input_layer.add_neurons(input_neurons)

    hidden_layer = Layer()
    hidden_neurons = []
    for _ in range(20):
        weights_array = np.array([np.random.uniform(-1, 1) for _ in range(2)])
        hidden_neurons.append(Neuron(weights_array))
    hidden_layer.add_neurons(hidden_neurons)

    output_layer = Layer()
    output_neurons = []
    for _ in range(1):
        weights_array = np.array([np.random.uniform(-1, 1) for _ in range(20)])
        output_neurons.append(Neuron(weights_array))
    output_layer.add_neurons(output_neurons)

    nn = Network()
    nn.add_layer(input_layer)
    nn.add_layer(hidden_layer)
    nn.add_layer(output_layer)
    nn.show()

    epochs = 50
    learning_rate = 0.0005

    x1 = x2 = y1 = y2 = np.array([])
    y = []
    for _ in range(epochs):
        my_moon = moon.Moon(4, 2, -1)
        point_nums = 128
        res1, res2 = my_moon.moon(point_nums)
        x1 = np.append(x1, res1[:, 0])
        x2 = np.append(x2, res2[:, 0])
        inputs = np.concatenate((res1, res2))
        np.random.shuffle(inputs)
        outputs = [1 if inputs[i][1] > 0 else -1 for i in range(len(inputs))]
        for i in range(point_nums):
            nn.inputs = inputs[i]
            nn.activate()
            error = outputs[i] - nn.get_outputs()
            delta = error * sigmoid_derivative(nn.get_outputs())
            for k in range(len(nn.layers[-1].neurons)):
                delta_weight = learning_rate * delta * nn.layers[-1].inputs
                nn.layers[-1].neurons[k].weights += delta_weight

            for j in range(len(nn.layers) - 2, -1, -1):
                delta = sigmoid_derivative(nn.layers[j].get_outputs()) * np.dot(delta, nn.layers[j+1].get_weights())
                for k in range(len(nn.layers[j].neurons)):
                    delta_weight = learning_rate * delta[k] * nn.layers[j].inputs
                    nn.layers[j].neurons[k].weights += delta_weight

        total_error = 0
        for i in range(point_nums):
            nn.inputs = inputs[i]
            nn.activate()
            total_error += np.square(outputs[i] - nn.get_outputs())
        y.append(total_error / point_nums)

    r, r1, r2 = 4, 3, 5
    d = -1
    y1 = np.array([])
    for x in x1:
        low = 0 if abs(x) > r1 else np.sqrt(np.square(r1) - np.square(x))
        high = np.sqrt(np.square(r2) - np.square(x))
        y1 = np.append(y1, np.random.uniform(low, high))

    x2 -= r
    y2 = np.array([])
    for x in x2:
        low = 0 if abs(x) > r1 else np.sqrt(np.square(r1) - np.square(x))
        high = np.sqrt(np.square(r2) - np.square(x))
        low = -low - d
        high = -high - d
        y2 = np.append(y2, np.random.uniform(low, high))
    x2 += r

    plt.title(f"epochs {epochs}, learning_rate {learning_rate}")
    plt.xlabel("epochs")
    plt.ylabel("MSE")
    plt.ylim(0, 3)
    plt.plot(y)
    plt.savefig(f"output/epochs{epochs}_learning_rate{learning_rate}.png")
    plt.show()

    nn.show()
    # plt.plot(x1, y1, 'ro')
    # plt.plot(x2, y2, 'bo')

    # decision_x = np.linspace(-5, 9, 100)
    # decision_y = np.array([])
    # for i in range(len(decision_x)):
    #     min_y = 5
    #     min_output = 1
    #     for temp_y in np.linspace(-5, 5, 100):
    #         nn.inputs = np.array([decision_x[i], temp_y])
    #         nn.activate()
    #         if abs(nn.get_outputs()[0]) < abs(min_output):
    #             min_y = temp_y
    #             min_output = nn.get_outputs()[0]
    #     decision_y = np.append(decision_y, min_y)
    #
    # plt.plot(x1, y1, 'ro')
    # plt.plot(x2, y2, 'bo')
    #
    # plt.plot(decision_x, decision_y, 'g-')
    # plt.show()
