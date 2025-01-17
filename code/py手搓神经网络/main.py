import img
import json
import random
import numpy as np


class Neuron:
    def __init__(self):
        self.inputs = None
        self.weight = None
        self.threshold = 0
        self.function = None
        self.output = 0

    def get_output(self):
        self.inputs = np.array(self.inputs, dtype=np.float64)
        self.inputs /= np.sum(self.inputs)
        multiply_array = np.dot(self.inputs, self.weight)
        self.output = self.function(multiply_array.sum() - self.threshold)
        return self.output


class Layer:
    def __init__(self, num):
        self.inputs = None
        self.neurons = []
        for i in range(num):
            neuron = Neuron()
            neuron.weight = random.uniform(0, 1)
            neuron.threshold = random.uniform(0, 1)
            neuron.function = sigmoid
            self.neurons.append(neuron)

    def get_output(self):
        output = np.array([])
        for neuron in self.neurons:
            neuron.inputs = self.inputs
            output = np.append(output, neuron.get_output())

        return output

    def show(self):
        print("number | weights | threshold")
        i = 0
        for neuron in self.neurons:
            i += 1
            print(f'neuron{i} | {neuron.weight} | {neuron.threshold}')


class Network:
    def __init__(self):
        self.inputs = None
        self.layers = []
        self.output = None

    def add_layer(self, layer):
        self.layers.append(layer)

    def set_inputs(self, inputs):
        self.inputs = inputs
        self.layers[0].inputs = inputs

    def get_output(self):
        self.output = self.layers[-1].get_output()
        return self.output

    def activate(self):
        for i in range(1, len(self.layers)):
            self.layers[i].inputs = self.layers[i-1].get_output()

    def show(self):
        for layer in self.layers:
            print("=======================================================================")
            layer.show()


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))


def record_network(network):
    result, index = {}, 1
    for layer in network.layers:
        layer_list = []
        for neuron in layer.neurons:
            layer_list.append((neuron.weight, neuron.threshold))
        result[index] = layer_list
        index += 1

    with open("data/json/memory.json", "w") as f:
        f.write(json.dumps(result))
    return result


def create_network_from_json():
    with open("data/json/memory.json", "r") as f:
        data = json.load(f)
    res_network = Network()
    for layer in data:
        new_layer = Layer(len(data[layer]))
        for i in range(len(data[layer])):
            new_layer.neurons[i].weight = data[layer][i][0]
            new_layer.neurons[i].threshold = data[layer][i][1]
        res_network.add_layer(new_layer)
    return res_network


def train(network, inputs, outputs):
    network.set_inputs(inputs)
    network.activate()

    for i in range(len(network.layers) - 1, 0, -1):
        delta_y = outputs - network.layers[i].get_output()
        for j in range(len(network.layers[i].neurons)):
            delta_weight = delta_y[j] * derivative(network.layers[i].neurons[j].get_output())
            network.layers[i].neurons[j].weight += delta_weight

    for i in range(len(network.layers[0].neurons)):
        delta_y = outputs - network.layers[0].get_output()
        delta_weight = delta_y[i] * derivative(network.layers[0].neurons[i].get_output())
        network.layers[0].neurons[i].weight += delta_weight

    record_network(network)
    return network


if __name__ == "__main__":
    nn = create_network_from_json()
    inputs_array = img.read_img("input.jpg")
    nn.set_inputs(inputs_array)
    nn.activate()

    # 输出numpy最大值索引
    print(nn.get_output())
    print(np.argmax(nn.get_output()))
