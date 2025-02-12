import os
import json
import numpy as np
from PIL import Image


def sigmoid(x):
    x = np.where(x >= 10, 10, x)
    x = np.where(x <= -10, -10, x)
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    x = np.where(x >= 5, 5, x)
    x = np.where(x <= -5, -5, x)
    return (1 - sigmoid(x)) * sigmoid(x)


def read_img(path):
    img_array = np.array(Image.open(path), dtype=np.int16)
    img_array = img_array.flatten()
    return img_array


def read_dir(path, start, end):
    result = []
    for filename in os.listdir(path)[start - 1:end]:
        number = os.path.splitext(filename)[0]
        if os.path.splitext(filename)[1] == ".jpg":
            number = number.split('_')[2]
            file_path = os.path.join(path, filename)
            result.append([number, read_img(file_path)])
    return result


class Neuron:
    def __init__(self):
        self.weights = None
        self.bias = 0
        self.output = None

    def get_output(self, inputs):
        v = np.sum(inputs * self.weights) + self.bias
        self.output = sigmoid(v)
        return self.output


class Layer:
    def __init__(self, nums=0, weights_nums=0):
        self.neurons = []
        self.outputs = None

        for _ in range(nums):
            new_neuron = Neuron()
            new_neuron.weights = np.random.uniform(-1, 1, weights_nums)
            self.neurons.append(new_neuron)

    def get_outputs(self, inputs):
        self.outputs = np.array([neuron.get_output(inputs) for neuron in self.neurons])
        return self.outputs


class Network:
    def __init__(self, layer_nums=None):
        if layer_nums is None:
            layer_nums = []
        self.layers = []
        self.outputs = None

        for i in range(1, len(layer_nums)):
            new_layer = Layer(layer_nums[i], layer_nums[i - 1])
            self.layers.append(new_layer)

    def show(self):
        for i in range(len(self.layers)):
            print(f'【Layers{i + 1}】')
            for j in range(len(self.layers[i].neurons)):
                print(
                    f'[neuron{j + 1}] {self.layers[i].neurons[j].bias} {len(self.layers[i].neurons[j].weights)}:{self.layers[i].neurons[j].weights}')

    def forward(self, inputs):
        outputs = inputs
        for i in range(len(self.layers)):
            outputs = self.layers[i].get_outputs(outputs)
        self.outputs = self.layers[-1].outputs
        return self.outputs

    def memory(self):
        network_data = []
        for i in range(len(self.layers)):
            layer_list = []
            for j in range(len(self.layers[i].neurons)):
                layer_list.append([
                    self.layers[i].neurons[j].weights.tolist(),
                    self.layers[i].neurons[j].bias
                ])
            network_data.append(layer_list)

        network_data = json.dumps(network_data)
        with open("data/homework_two/data.json", "w") as f:
            f.write(network_data)
            f.close()

    def create_from_memory(self):
        with open("data/homework_two/data.json", "r") as f:
            network_data = f.read()
            f.close()
        network_data = json.loads(network_data)

        temp_layers = []
        for i in range(len(network_data)):
            new_layer = Layer()
            for j in range(len(network_data[i])):
                new_neuron = Neuron()
                new_neuron.weights = network_data[i][j][0]
                new_neuron.bias = network_data[i][j][1]
                new_layer.neurons.append(new_neuron)
            temp_layers.append(new_layer)
        self.layers = temp_layers

    def train(self, epoches, learning_rate, training_nums=10):
        self.create_from_memory()
        for i in range(epoches):
            self.create_from_memory()
            training_data = read_dir("mnist_handwriting_data/mnist_jpg", training_nums * i + 1,
                                     training_nums * i + training_nums)
            total_error = 0
            for j in range(len(training_data)):
                training_inputs = training_data[j][1]
                training_outputs = np.zeros(10)
                training_outputs[int(training_data[j][0])] = 1

                self.forward(training_inputs)
                error = training_outputs - self.outputs
                delta_vector = np.array([])
                weights_vector = []
                for k in range(len(self.layers[-1].neurons)):
                    v = sigmoid(
                        np.sum(self.layers[-1].neurons[k].weights * self.layers[-2].outputs) + self.layers[-1].neurons[
                            k].bias)
                    delta = error[k] * sigmoid_derivative(v)
                    delta_vector = np.append(delta_vector, delta)
                    self.layers[-1].neurons[k].weights += learning_rate * delta * self.layers[-2].outputs
                    weights_vector.append(self.layers[-1].neurons[k].weights)
                weights_vector = np.array(weights_vector)

                for k in range(len(self.layers) - 2, -1, -1):
                    delta_temp_vector = np.array([])
                    weights_temp_vector = []
                    for n in range(len(self.layers[k].neurons)):
                        pre_outputs = self.layers[k-1].outputs if k != 0 else training_inputs
                        delta_j = np.sum(delta_vector * weights_vector[:, n]) * sigmoid_derivative(np.sum(pre_outputs * self.layers[k].neurons[n].weights) + self.layers[k].neurons[n].bias)
                        delta_temp_vector = np.append(delta_temp_vector, delta_j)

                        self.layers[k].neurons[n].weights += learning_rate * delta_j * pre_outputs
                        weights_temp_vector.append(self.layers[k].neurons[n].weights)
                    delta_vector = delta_temp_vector
                    weights_vector = np.array(weights_temp_vector)

                total_error += np.sum(np.square(training_outputs - self.outputs)) / 2

            total_error /= len(training_data)

            self.memory()
            print(f'【training_times:{i+1}】  error{i+1}:{round(total_error, 4)}')


if __name__ == "__main__":
    nn = Network([784, 64, 32, 16, 16, 16, 10])
    nn.memory()
    my_img_array = read_img("mnist_handwriting_data/mnist_jpg/test_0_7.jpg")
    nn.train(200, 0.001, 10)
    print(nn.forward(my_img_array))
