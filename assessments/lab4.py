# AND gate input and expected output
inputs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

outputs = [0, 0, 0, 1]

# Initialize weights and bias
w1 = 0
w2 = 0
bias = 0

learning_rate = 0.1
epochs = 10

# Training process
for epoch in range(epochs):
    print("\nIteration:", epoch + 1)

    for i in range(len(inputs)):
        x1, x2 = inputs[i]

        net = (x1 * w1) + (x2 * w2) + bias

        # Step activation function
        predicted = 1 if net > 0 else 0

        error = outputs[i] - predicted

        # Update weights and bias
        w1 = w1 + learning_rate * error * x1
        w2 = w2 + learning_rate * error * x2
        bias = bias + learning_rate * error

    print("Weight 1:", round(w1, 2))
    print("Weight 2:", round(w2, 2))
    print("Bias:", round(bias, 2))

# Testing the trained model
print("\nTesting AND Gate:")

for x1, x2 in inputs:
    net = (x1 * w1) + (x2 * w2) + bias
    predicted = 1 if net > 0 else 0
    print(x1, "AND", x2, "=", predicted)
