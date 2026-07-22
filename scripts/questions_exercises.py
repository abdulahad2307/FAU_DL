"""Questions derived from the programming exercises (exercise 0-4).

These are grounded in the exercise descriptions, the exercise slide decks and the
provided skeleton code / unit tests, i.e. the layer-oriented framework the course
asks you to build (Sgd, FullyConnected, ReLU, SoftMax, CrossEntropyLoss,
Initializers, Adam, Conv, Pooling, Flatten, Dropout, BatchNormalization, RNN,
LSTM) plus the PyTorch/ResNet challenge.

Worth practising separately: the exam has a dedicated coding section that
explicitly says "You are given the framework of the exercise 1, 2 and 3".

Every entry carries source="exercises" and an "exercise" number so the trainer
can offer an exercise-only mode.
"""

X = []


def a(topic, diff, pts, qtype, q, opts, corr, expl, ex):
    X.append({"topic": topic, "difficulty": diff, "points": pts, "type": qtype,
              "question": q, "options": opts, "correct_answers": corr,
              "explanation": expl, "source": "exercises", "exercise": ex})


T_INTRO = "Introduction"
T_NN = "Neural Networks"
T_LO = "Loss and Optimization"
T_CNN = "Activation Functions and CNN"
T_REG = "Regularization"
T_RNN = "Recurrent Neural Networks"
T_UNS = "Unsupervised Learning"
T_CP = "Common Practices"
T_ARCH = "Architectures"
T_VIS = "Visualization and Attention Mechanism"
T_RL = "Deep Reinforcement Learning"
T_SEG = "Segmentation"

# =========================================================================
# Exercise 0 - NumPy tutorial, patterns, ImageGenerator
# =========================================================================

a(T_INTRO, "basics", 1, "single_choice",
  "In exercise 0 the pattern classes (Checker, Circle, Spectrum) must be built without Python loops. Why?",
  {"A": "Loops would produce mathematically wrong patterns",
   "B": "Python-level loops are slow, so vectorised NumPy operations are required",
   "C": "NumPy arrays cannot be indexed inside a loop",
   "D": "The unit tests inspect the source code for the word 'for'"},
  ["B"], "Python is interpreted, so element-wise loops are far slower than vectorised NumPy calls. The exercise forces you to learn proper indexing and slicing.", 0)

a(T_INTRO, "basics", 1, "single_choice",
  "Which three methods does every pattern class in exercise 0 provide?",
  {"A": "__init__(), draw() and show()",
   "B": "forward(), backward() and show()",
   "C": "__init__(), fit() and predict()",
   "D": "build(), run() and plot()"},
  ["A"], "Each pattern is a class with a constructor, a draw() that builds the array into the instance variable output, and a show() that displays it.", 0)

a(T_INTRO, "intermediate", 2, "single_choice",
  "The Checker class must reject some resolutions. Which condition does a valid checkerboard resolution satisfy?",
  {"A": "resolution must be a power of two",
   "B": "resolution must be evenly divisible by 2 * tile_size",
   "C": "resolution must be evenly divisible by tile_size only",
   "D": "resolution must be larger than tile_size squared"},
  ["B"], "A checker period is two tiles wide, so only multiples of 2*tile_size tile the image without a truncated block at the border.", 0)

a(T_INTRO, "basics", 1, "single_choice",
  "In the Checker pattern of exercise 0, which tile must be black?",
  {"A": "The tile in the top left corner",
   "B": "The tile in the bottom right corner",
   "C": "The centre tile",
   "D": "It does not matter, the tests accept both phases"},
  ["A"], "The description fixes the phase of the pattern by requiring the top-left tile to be black; otherwise the reference array comparison fails.", 0)

a(T_INTRO, "intermediate", 2, "single_choice",
  "draw() stores the pattern in the instance variable output. What should it return?",
  {"A": "None, the caller reads output directly",
   "B": "A copy of output",
   "C": "A reference to output, so callers can modify it in place",
   "D": "A flattened version of output"},
  ["B"], "Returning a copy prevents a caller from mutating the stored pattern through the returned reference.", 0)

a(T_INTRO, "intermediate", 2, "single_choice",
  "The Circle class receives resolution, radius and position. What does draw() produce?",
  {"A": "A grayscale circle with a smooth intensity falloff",
   "B": "A binary image of a circle at the given centre",
   "C": "A ring outline one pixel wide",
   "D": "A filled square inscribed in the circle"},
  ["B"], "The exercise asks for a binary circle drawn with NumPy operations; a single library call that draws circles is explicitly not accepted.", 0)

a(T_CP, "intermediate", 2, "single_choice",
  "The Spectrum class of exercise 0 produces an RGB image. What is the intensity range of each channel?",
  {"A": "0 to 255 as integers",
   "B": "minimum 0.0 and maximum 1.0",
   "C": "-1.0 to 1.0",
   "D": "0.0 to 0.5"},
  ["B"], "Each of the three channels rises across a different spatial direction, with 0.0 as the minimum and 1.0 as the maximum.", 0)

a(T_CP, "basics", 1, "single_choice",
  "What does ImageGenerator.next() return?",
  {"A": "A single image",
   "B": "A tuple (images, labels) forming one batch",
   "C": "Only the labels for the next batch",
   "D": "A generator object that must be iterated"},
  ["B"], "next() hands back one batch as a tuple of the image array and the matching label array.", 0)

a(T_CP, "intermediate", 2, "single_choice",
  "In exercise 0, what must the ImageGenerator do when the last batch of an epoch is smaller than batch_size?",
  {"A": "Return the short batch as is",
   "B": "Drop the remaining samples",
   "C": "Fill it up by reusing images from the beginning of the dataset",
   "D": "Pad it with zero images"},
  ["C"], "All batches must have the same size, so the tail batch is completed by wrapping around to the start of the data.", 0)

a(T_CP, "intermediate", 2, "single_choice",
  "With shuffle=True, what must the ImageGenerator guarantee within one epoch?",
  {"A": "The order inside each batch is random but the batch order is fixed",
   "B": "No duplicates appear within one epoch, and the indices are reshuffled after each epoch",
   "C": "Each image appears exactly twice",
   "D": "Shuffling only affects the labels"},
  ["B"], "Shuffling must randomise the whole dataset order, not just within a batch, and must not return duplicates before the epoch ends.", 0)

a(T_CP, "intermediate", 2, "single_choice",
  "How are the rotation and mirroring augmentations applied in ImageGenerator.next()?",
  {"A": "To the whole batch at once, so all images share the same transform",
   "B": "On an image-by-image basis, so a batch can mix transformed and untransformed images",
   "C": "Only to the first image of every batch",
   "D": "Only during the second and later epochs"},
  ["B"], "The description states that augmentation is per image, which is why a single batch may contain rotated and non-rotated images side by side.", 0)

a(T_CP, "basics", 1, "single_choice",
  "Which rotation angles does the ImageGenerator's rotation flag apply?",
  {"A": "Any angle drawn uniformly from 0 to 360 degrees",
   "B": "90, 180 or 270 degrees",
   "C": "Only 180 degrees",
   "D": "45 degree multiples"},
  ["B"], "Only multiples of 90 degrees are used, which keeps the image grid intact and needs no interpolation.", 0)

a(T_CP, "intermediate", 2, "single_choice",
  "In exercise 0, what is the difference between resizing and reshaping an image?",
  {"A": "They are two names for the same operation",
   "B": "Resizing interpolates the data, reshaping only reorders the existing values",
   "C": "Resizing works on colour images, reshaping only on grayscale",
   "D": "Reshaping changes the number of pixels, resizing does not"},
  ["B"], "The description explicitly warns against confusing the two: resize interpolates (e.g. skimage.transform.resize), reshape merely reinterprets the same buffer.", 0)

a(T_CP, "basics", 1, "single_choice",
  "How are the labels stored for the exercise 0 image generator?",
  {"A": "As a CSV table with one row per image",
   "B": "In a JSON file mapping the image filename to an integer class label",
   "C": "Encoded in the image filenames themselves",
   "D": "As one-hot vectors inside each .npy file"},
  ["B"], "The JSON is a dictionary whose key is the filename (e.g. '15' for 15.npy) and whose value is the integer class label.", 0)

a(T_CP, "basics", 1, "single_choice",
  "What does ImageGenerator.current_epoch() return, and when does it change?",
  {"A": "The number of batches served so far, incremented on every next() call",
   "B": "The current epoch number, updated in next() when iteration restarts from the beginning of the dataset",
   "C": "The remaining epochs until training finishes",
   "D": "A float between 0 and 1 giving progress through the epoch"},
  ["B"], "The counter tracks complete passes through the data and is advanced inside next() when the index wraps around.", 0)

a(T_INTRO, "basics", 1, "single_choice",
  "How do you run only one specific test case from the exercise 0 test suite?",
  {"A": "python NumpyTests.py --only <TestName>",
   "B": "python NumpyTests.py <TestName>",
   "C": "python NumpyTests.py -k <TestName>",
   "D": "You cannot; the suite always runs completely"},
  ["B"], "Passing the test name as a command line parameter runs that single test; passing nothing runs all of them.", 0)

a(T_INTRO, "basics", 1, "single_choice",
  "How are bonus points for an exercise computed automatically?",
  {"A": "By running the test suite with the Bonus command line flag",
   "B": "By counting the lines of code in the submission",
   "C": "By measuring the runtime of the unit tests",
   "D": "By manual review only"},
  ["A"], "Running the test file with 'Bonus' as the parameter reports the bonus points achieved for that exercise.", 0)

a(T_INTRO, "basics", 1, "single_choice",
  "What is the purpose of dispatch.py in the exercise material?",
  {"A": "It trains the network on a compute cluster",
   "B": "It checks the submission for completeness and zips the files needed for upload",
   "C": "It dispatches gradients to the optimizer",
   "D": "It downloads the dataset"},
  ["B"], "dispatch.py packages src_to_implement into a submission zip after checking that the required files are present.", 0)

# =========================================================================
# Exercise 1 - basic framework: Sgd, BaseLayer, FullyConnected, ReLU,
#              SoftMax, CrossEntropyLoss, NeuralNetwork
# =========================================================================

a(T_NN, "basics", 1, "single_choice",
  "Which two methods must every layer in the exercise framework implement?",
  {"A": "fit(x) and predict(x)",
   "B": "forward(input_tensor) and backward(error_tensor)",
   "C": "initialize() and update()",
   "D": "encode(x) and decode(z)"},
  ["B"], "The layer-oriented framework is built around exactly these two operations, executed during training and testing.", 1)

a(T_NN, "basics", 1, "single_choice",
  "What distinguishes a trainable from a non-trainable layer in the framework?",
  {"A": "Trainable layers implement backward(), non-trainable ones do not",
   "B": "Trainable layers have parameters optimised during training; the inherited member 'trainable' is set to True",
   "C": "Non-trainable layers are skipped in the forward pass",
   "D": "Trainable layers must be the last layers of the network"},
  ["B"], "BaseLayer initialises trainable=False; layers with parameters such as FullyConnected set it to True so the network knows to give them an optimizer.", 1)

a(T_NN, "basics", 1, "single_choice",
  "In BaseLayer, what is the default value of the member 'trainable'?",
  {"A": "True",
   "B": "False",
   "C": "None",
   "D": "It is not initialised in the constructor"},
  ["B"], "The base constructor sets trainable to False; only layers with parameters override it.", 1)

a(T_NN, "intermediate", 2, "single_choice",
  "Why does the course build a layer-oriented framework rather than a graph-oriented one?",
  {"A": "Layer-oriented frameworks are strictly more flexible",
   "B": "It offers a higher level of abstraction: less flexibility, but easy experimentation with conventional architectures",
   "C": "Graph-oriented frameworks cannot compute gradients",
   "D": "Layer-oriented frameworks avoid the need for a loss function"},
  ["B"], "The trade-off is deliberate: stacking elementary layers limits the expressible graphs but keeps the implementation simple.", 1)

a(T_NN, "basics", 1, "single_choice",
  "What does the Sgd constructor receive in exercise 1?",
  {"A": "The learning rate as a float",
   "B": "The learning rate and the momentum rate",
   "C": "The weight tensor",
   "D": "Nothing; the learning rate is passed to calculate_update"},
  ["A"], "Plain SGD only needs a learning rate; momentum and Adam arrive in exercise 2 with additional constructor arguments.", 1)

a(T_NN, "basics", 1, "single_choice",
  "What is the signature of the optimizer method used to update parameters?",
  {"A": "update(weights)",
   "B": "calculate_update(weight_tensor, gradient_tensor)",
   "C": "step(loss)",
   "D": "apply_gradients(gradient_tensor)"},
  ["B"], "Every optimizer in the framework exposes calculate_update(weight_tensor, gradient_tensor) and returns the updated weights.", 1)

a(T_NN, "intermediate", 2, "single_choice",
  "In the FullyConnected layer, what is the layout of input_tensor?",
  {"A": "input_size rows and batch_size columns",
   "B": "batch_size rows and input_size columns",
   "C": "A 4-D tensor in b, c, y, x order",
   "D": "A flat 1-D vector of length input_size * batch_size"},
  ["B"], "Rows index the batch, columns index the features, so the layer computes X W with X of shape (batch_size, input_size).", 1)

a(T_NN, "intermediate", 2, "single_choice",
  "How does the exercise framework handle the bias of a FullyConnected layer?",
  {"A": "It is stored in a separate member and added after the matrix multiplication",
   "B": "It is folded into the weights matrix, so a single matrix multiplication suffices",
   "C": "The bias is not learned at all",
   "D": "The bias is applied by the optimizer, not the layer"},
  ["B"], "Appending a constant 1 to the input and an extra row to the weights turns the affine map into one matrix product.", 1)

a(T_NN, "basics", 1, "single_choice",
  "How are the weights of the FullyConnected layer initialised in exercise 1, before Initializers exist?",
  {"A": "All zeros",
   "B": "Uniformly random in the range [0, 1)",
   "C": "Standard normal N(0, 1)",
   "D": "Xavier initialisation"},
  ["B"], "Exercise 1 uses a simple uniform random initialisation; Xavier and He are added in exercise 2.", 1)

a(T_NN, "intermediate", 2, "single_choice",
  "Which property must FullyConnected expose so the unit tests can check the parameter gradient?",
  {"A": "grad_w",
   "B": "gradient_weights",
   "C": "weight_gradient",
   "D": "dW"},
  ["B"], "The tests access the property gradient_weights after the backward pass; the parameters themselves live in a member called weights.", 1)

a(T_NN, "intermediate", 2, "single_choice",
  "When should the FullyConnected layer skip the weight update in its backward pass?",
  {"A": "When the error tensor is all zeros",
   "B": "When no optimizer has been set on the layer",
   "C": "During the first iteration only",
   "D": "It should never skip the update"},
  ["B"], "The layer calls calculate_update only if its optimizer property has been assigned; otherwise it just propagates the error.", 1)

a(T_NN, "advanced", 3, "single_choice",
  "The FullyConnected backward pass needs a quantity that is not passed to backward(). Which one, and how is it obtained?",
  {"A": "The learning rate; it is read from the optimizer",
   "B": "The input tensor of the forward pass; it must be stored during forward()",
   "C": "The label tensor; it is fetched from the data layer",
   "D": "The output of the next layer; it is recomputed"},
  ["B"], "The weight gradient is the product of the stored input and the incoming error, so the forward pass must cache its input.", 1)

a(T_CNN, "basics", 1, "single_choice",
  "Why is the ReLU described as having 'revolutionised' neural networks in the exercise slides?",
  {"A": "It guarantees convex optimisation",
   "B": "It reduces the effect of the vanishing gradient problem",
   "C": "It removes the need for a loss function",
   "D": "It makes the network invariant to translation"},
  ["B"], "Unlike saturating activations, ReLU has gradient 1 on the positive side, so gradients do not shrink layer after layer.", 1)

a(T_CNN, "basics", 1, "single_choice",
  "Does the ReLU layer in the exercise framework set trainable to True?",
  {"A": "Yes, it learns a slope parameter",
   "B": "No, it has no trainable parameters so the inherited default is kept",
   "C": "Yes, but only in the convolutional variant",
   "D": "Only when an optimizer is attached"},
  ["B"], "ReLU is a fixed non-linearity; the constructor takes no arguments and leaves trainable at False.", 1)

a(T_CNN, "intermediate", 2, "single_choice",
  "What does the SoftMax layer do in the exercise framework?",
  {"A": "It clips the logits to the range [0, 1]",
   "B": "It transforms the logits into a probability distribution, one per row of the batch",
   "C": "It computes the loss value directly",
   "D": "It normalises the weights of the previous layer"},
  ["B"], "Each row of the batch is turned into estimated class probabilities, which is why SoftMax is the usual final layer for classification.", 1)

a(T_LO, "advanced", 3, "single_choice",
  "Which class in exercise 1 does NOT inherit from BaseLayer?",
  {"A": "ReLU",
   "B": "SoftMax",
   "C": "CrossEntropyLoss",
   "D": "FullyConnected"},
  ["C"], "The loss is deliberately not treated as a layer in this framework, so CrossEntropyLoss stands outside the layer hierarchy.", 1)

a(T_LO, "intermediate", 2, "single_choice",
  "What arguments do the forward and backward methods of CrossEntropyLoss take?",
  {"A": "forward(prediction_tensor, label_tensor) and backward(label_tensor)",
   "B": "forward(input_tensor) and backward(error_tensor)",
   "C": "forward(label_tensor) and backward(prediction_tensor)",
   "D": "forward(prediction_tensor) and backward(error_tensor)"},
  ["A"], "Backpropagation starts at the loss, so no incoming error tensor exists; the labels are needed instead.", 1)

a(T_LO, "intermediate", 2, "single_choice",
  "What does CrossEntropyLoss.forward return?",
  {"A": "A vector with one loss value per sample",
   "B": "The loss accumulated over the batch",
   "C": "The gradient with respect to the predictions",
   "D": "The predicted class indices"},
  ["B"], "The forward pass sums the per-sample cross entropy over the batch into a single scalar loss.", 1)

a(T_NN, "intermediate", 2, "single_choice",
  "Which five members does the NeuralNetwork class of exercise 1 hold?",
  {"A": "optimizer, loss, layers, data_layer, loss_layer",
   "B": "weights, bias, gradient, learning_rate, epochs",
   "C": "model, criterion, optimizer, train_dl, val_dl",
   "D": "forward, backward, train, test, append_layer"},
  ["A"], "The optimizer arrives on construction, loss collects the per-iteration values, layers holds the architecture, and the two remaining members reference the data source and the loss layer.", 1)

a(T_NN, "basics", 1, "single_choice",
  "How does the NeuralNetwork obtain training data?",
  {"A": "It reads a CSV file directly",
   "B": "By calling next() on its data_layer, which returns an input tensor and a label tensor",
   "C": "The data is passed to the constructor",
   "D": "Each layer fetches its own data"},
  ["B"], "The data layer is a generator-style object; next() yields the pair used for one iteration.", 1)

a(T_NN, "advanced", 3, "single_choice",
  "In append_layer(layer), why is a deep copy of the network's optimizer made for each trainable layer?",
  {"A": "To allow different learning rates per layer by default",
   "B": "Because optimizers such as Adam keep internal state that must not be shared between layers",
   "C": "Because Python cannot pass objects by reference",
   "D": "To avoid a circular import"},
  ["B"], "Momentum and Adam accumulate per-parameter moments; sharing one object across layers would mix up their states.", 1)

a(T_NN, "intermediate", 2, "single_choice",
  "What does NeuralNetwork.test(input_tensor) return?",
  {"A": "The loss on the given input",
   "B": "The prediction of the last layer, typically the probabilistic SoftMax output",
   "C": "The accuracy as a percentage",
   "D": "The gradient with respect to the input"},
  ["B"], "test() only runs the forward pass through the layers and returns the network output; the loss layer is not involved.", 1)

a(T_NN, "intermediate", 2, "single_choice",
  "What does NeuralNetwork.train(iterations) store?",
  {"A": "A checkpoint file after every iteration",
   "B": "The loss value for each iteration in the member 'loss'",
   "C": "The weights of every layer at every step",
   "D": "Nothing; it only prints progress"},
  ["B"], "train() runs forward and backward for the given number of iterations and appends each loss to the list.", 1)

a(T_NN, "advanced", 3, "single_choice",
  "In which order does NeuralNetwork.backward() traverse the network?",
  {"A": "From the data layer forwards to the loss layer",
   "B": "From the loss layer backwards through the layers, passing the label tensor in first",
   "C": "In the order layers were appended",
   "D": "Trainable layers first, then non-trainable ones"},
  ["B"], "Backpropagation starts at the loss with the current label tensor and hands each layer's returned error tensor to its predecessor.", 1)

# =========================================================================
# Exercise 2 - Initializers, advanced optimizers, Flatten, Conv, Pooling
# =========================================================================

a(T_NN, "intermediate", 2, "single_choice",
  "Which four initializer classes are implemented in exercise 2?",
  {"A": "Zero, Normal, Uniform and Orthogonal",
   "B": "Constant, UniformRandom, Xavier and He",
   "C": "Xavier, He, LeCun and Glorot",
   "D": "Random, Pretrained, Frozen and Adaptive"},
  ["B"], "All four expose initialize(weights_shape, fan_in, fan_out) and return a tensor of the requested shape.", 2)

a(T_NN, "basics", 1, "single_choice",
  "What is the default constant value of the Constant initializer?",
  {"A": "0.0",
   "B": "0.1",
   "C": "1.0",
   "D": "0.01"},
  ["B"], "The class takes the value as a constructor argument with 0.1 as the default.", 2)

a(T_NN, "intermediate", 2, "single_choice",
  "What is the common signature of every initializer's initialize method?",
  {"A": "initialize(weights_shape, fan_in, fan_out)",
   "B": "initialize(weights)",
   "C": "initialize(layer)",
   "D": "initialize(shape, seed)"},
  ["A"], "A uniform signature lets NeuralNetwork.append_layer initialise any trainable layer without knowing its type.", 2)

a(T_NN, "intermediate", 2, "single_choice",
  "For a fully connected layer, how are fan_in and fan_out defined?",
  {"A": "fan_in is the batch size, fan_out the number of layers",
   "B": "fan_in is the input dimension of the weights, fan_out the output dimension",
   "C": "fan_in is the number of samples, fan_out the number of classes",
   "D": "Both equal the number of weights"},
  ["B"], "They are simply the two dimensions of the weight matrix.", 2)

a(T_CNN, "advanced", 3, "single_choice",
  "For a convolutional layer, how is fan_in defined in the exercise slides?",
  {"A": "number of input channels",
   "B": "number of input channels x kernel height x kernel width",
   "C": "number of output channels x kernel height x kernel width",
   "D": "kernel height x kernel width only"},
  ["B"], "fan_in counts every weight feeding one output unit; fan_out uses the number of output channels with the same kernel extent.", 2)

a(T_NN, "advanced", 3, "single_choice",
  "Xavier/Glorot initialisation draws weights from a zero-mean Gaussian. What is the standard deviation?",
  {"A": "sqrt(2 / fan_in)",
   "B": "sqrt(2 / (fan_out + fan_in))",
   "C": "sqrt(1 / (fan_in * fan_out))",
   "D": "sqrt(fan_in + fan_out)"},
  ["B"], "Xavier balances the variance of the forward and the backward signal, so both fan_in and fan_out appear.", 2)

a(T_NN, "advanced", 3, "single_choice",
  "He initialisation differs from Xavier in which way?",
  {"A": "It uses a uniform rather than a Gaussian distribution",
   "B": "Its standard deviation is sqrt(2 / fan_in), i.e. determined by the previous layer size only",
   "C": "It initialises the bias instead of the weights",
   "D": "It scales by the batch size"},
  ["B"], "He was derived from Xavier specifically for ReLU activations, which discard the negative half of the signal.", 2)

a(T_NN, "intermediate", 2, "single_choice",
  "In exercise 2, how is the bias of a FullyConnected layer initialised?",
  {"A": "With the same initializer as the weights",
   "B": "Separately, with the dedicated bias_initializer",
   "C": "Always with zeros, ignoring any initializer",
   "D": "It is not initialised at all"},
  ["B"], "initialize(weights_initializer, bias_initializer) treats the bias separately even though it is stored inside the weights matrix.", 2)

a(T_LO, "intermediate", 2, "single_choice",
  "What arguments does the SgdWithMomentum constructor receive, in order?",
  {"A": "momentum rate, learning rate",
   "B": "learning rate, momentum rate",
   "C": "learning rate, mu, rho",
   "D": "learning rate only"},
  ["B"], "The order matters because the unit tests construct the optimizer positionally.", 2)

a(T_LO, "intermediate", 2, "single_choice",
  "What arguments does the Adam constructor receive, in order?",
  {"A": "learning rate, mu, rho",
   "B": "mu, rho, learning rate",
   "C": "learning rate, rho, mu",
   "D": "learning rate, epsilon, mu"},
  ["A"], "In the literature mu is usually called beta1 and rho beta2.", 2)

a(T_LO, "basics", 1, "single_choice",
  "Which values are given as common defaults for Adam in the exercise slides?",
  {"A": "mu = 0.5, rho = 0.9, eta = 0.01",
   "B": "mu = 0.9, rho = 0.999, eta = 0.001",
   "C": "mu = 0.999, rho = 0.9, eta = 0.1",
   "D": "mu = 0.99, rho = 0.99, eta = 0.0001"},
  ["B"], "These are the standard Adam hyperparameters; mu weights the first moment and rho the second.", 2)

a(T_LO, "basics", 1, "single_choice",
  "Which momentum values are listed as common in the exercise slides?",
  {"A": "0.1, 0.2, 0.3",
   "B": "0.5, 0.6, 0.7",
   "C": "0.9, 0.95, 0.99",
   "D": "1.0, 1.5, 2.0"},
  ["C"], "Momentum close to but below 1 accumulates past gradients over roughly 1/(1-mu) steps.", 2)

a(T_LO, "advanced", 3, "single_choice",
  "Adam applies bias correction with terms 1 - mu^k and 1 - rho^k. What is k here?",
  {"A": "The layer index",
   "B": "An exponent, not an iteration index",
   "C": "The batch size",
   "D": "The number of parameters"},
  ["B"], "The exercise slides flag this explicitly: k is used as an exponent so the correction decays as training progresses.", 2)

a(T_LO, "advanced", 3, "single_choice",
  "Why does Adam need bias correction at all?",
  {"A": "Because the bias term of each layer is otherwise ignored",
   "B": "Because the moment estimates are initialised at zero and would otherwise be biased towards zero early in training",
   "C": "Because the learning rate is too large at the start",
   "D": "Because gradients can be negative"},
  ["B"], "With v and r starting at zero, the raw running averages underestimate the true moments in the first iterations.", 2)

a(T_LO, "intermediate", 2, "single_choice",
  "How does the exercise framework store optimizer state such as the momentum term?",
  {"A": "In a global cache indexed by layer id",
   "B": "By giving the weights and bias of every layer their own copy of the optimizer",
   "C": "Inside the NeuralNetwork object",
   "D": "State is recomputed from scratch each iteration"},
  ["B"], "This is why append_layer deep-copies the optimizer; it also means each parameter set could in principle use a different optimizer.", 2)

a(T_CNN, "basics", 1, "single_choice",
  "What does the Flatten layer do?",
  {"A": "It removes the batch dimension",
   "B": "It reshapes a multi-dimensional input into a one-dimensional feature vector per sample",
   "C": "It averages over the spatial dimensions",
   "D": "It sorts the activations by magnitude"},
  ["B"], "Flatten is the adapter that lets a convolutional or pooling layer feed a fully connected layer.", 2)

a(T_CNN, "intermediate", 2, "single_choice",
  "What does Flatten.backward(error_tensor) do?",
  {"A": "It returns the error tensor unchanged",
   "B": "It reshapes the error tensor back to the shape of the forward input",
   "C": "It averages the error over the flattened dimension",
   "D": "It returns zeros because Flatten has no parameters"},
  ["B"], "Flatten is a pure reshape, so the backward pass simply reverses it; the stored input shape is needed for that.", 2)

a(T_CNN, "intermediate", 2, "single_choice",
  "What three arguments does the Conv constructor receive?",
  {"A": "stride_shape, convolution_shape, num_kernels",
   "B": "in_channels, out_channels, kernel_size",
   "C": "convolution_shape, padding, num_kernels",
   "D": "num_kernels, pooling_shape, stride_shape"},
  ["A"], "convolution_shape encodes the channels and the spatial extent; num_kernels sets the number of output channels.", 2)

a(T_CNN, "intermediate", 2, "single_choice",
  "How does convolution_shape distinguish a 1-D from a 2-D convolutional layer?",
  {"A": "By a separate boolean flag",
   "B": "[c, m] means 1-D, [c, m, n] means 2-D",
   "C": "By the length of stride_shape only",
   "D": "1-D convolutions are not supported"},
  ["B"], "c is the number of input channels; m and n are the spatial extents of the kernel.", 2)

a(T_CNN, "intermediate", 2, "single_choice",
  "What is the expected input layout of the Conv layer for the 2-D case?",
  {"A": "b, y, x, c",
   "B": "b, c, y, x",
   "C": "c, b, y, x",
   "D": "y, x, c, b"},
  ["B"], "Batch first, then channels, then the spatial dimensions; the 1-D case drops x and uses b, c, y.", 2)

a(T_CNN, "intermediate", 2, "single_choice",
  "Which padding does the exercise require for the convolutional layer?",
  {"A": "Valid padding, so the output shrinks",
   "B": "Zero padding ('same'), so input and output share the spatial shape at stride 1",
   "C": "Reflection padding",
   "D": "No padding is applied in either direction"},
  ["B"], "Same padding keeps the spatial dimensions when the stride is 1, which simplifies stacking layers.", 2)

a(T_CNN, "advanced", 3, "single_choice",
  "The exercise slides state that a convolutional layer applies different padding along different axes. Which combination is correct?",
  {"A": "'valid' across the image plane and 'same' across the channel axis",
   "B": "'same' across the image plane and 'valid' across the channel axis",
   "C": "'same' along both",
   "D": "'valid' along both"},
  ["B"], "The kernel spans all input channels at once (fully connected across channels, i.e. valid), while the spatial axes are zero-padded.", 2)

a(T_CNN, "advanced", 3, "single_choice",
  "Which properties must the Conv layer expose for the gradient tests?",
  {"A": "gradient_weights and gradient_bias",
   "B": "grad_w and grad_b",
   "C": "weights_grad only",
   "D": "dW and db"},
  ["A"], "The parameters live in members called weights and bias, and the tests read the two gradient properties after backward().", 2)

a(T_CNN, "advanced", 3, "single_choice",
  "Why may the Conv layer need two copies of the optimizer object?",
  {"A": "To run forward and backward in parallel",
   "B": "Because the bias is handled separately from the other weights, and each parameter set needs its own optimizer state",
   "C": "Because 1-D and 2-D convolutions use different optimizers",
   "D": "To support both training and testing phases"},
  ["B"], "Stateful optimizers such as Adam would otherwise mix the moment estimates of the weights and the bias.", 2)

a(T_CNN, "advanced", 3, "single_choice",
  "The exercise hints at using correlation in the forward pass and convolution in the backward pass. Why?",
  {"A": "Correlation is faster than convolution on all hardware",
   "B": "It avoids explicitly flipping the kernels, since convolution and correlation differ exactly by that flip",
   "C": "Convolution cannot be applied to multi-channel data",
   "D": "The backward pass computes a different mathematical operation entirely"},
  ["B"], "Because the two operations differ only by a spatial flip of the kernel, choosing them appropriately keeps the implementation flip-free.", 2)

a(T_CNN, "advanced", 3, "single_choice",
  "The exercise permits implementing striding wastefully. What does that mean?",
  {"A": "Padding the input with extra zeros before convolving",
   "B": "Performing a stride-1 convolution and then subsampling the result",
   "C": "Convolving each channel separately in a Python loop",
   "D": "Computing the convolution twice and averaging"},
  ["B"], "It costs unnecessary computation but is much simpler; the backward pass must then re-insert zero rows and columns where samples were dropped.", 2)

a(T_CNN, "intermediate", 2, "single_choice",
  "Which two arguments does the Pooling constructor receive?",
  {"A": "stride_shape and pooling_shape",
   "B": "pooling_shape and num_kernels",
   "C": "stride_shape and padding",
   "D": "pooling_shape only"},
  ["A"], "The ordering matches the convolutional layer's convention.", 2)

a(T_CNN, "intermediate", 2, "single_choice",
  "Which padding does the Pooling layer use, and what follows from that?",
  {"A": "Same padding, so the spatial size is preserved",
   "B": "Valid padding, so border elements may be discarded",
   "C": "Reflection padding, so no information is lost",
   "D": "The same padding as the preceding Conv layer"},
  ["B"], "Unlike the convolutional layer, pooling applies no zero padding, which must be accounted for when sizing the output tensor.", 2)

a(T_CNN, "intermediate", 2, "single_choice",
  "For which case must the Pooling layer be implemented in exercise 2?",
  {"A": "Only the 1-D case",
   "B": "Only the 2-D case",
   "C": "Both 1-D and 2-D",
   "D": "Arbitrary dimensionality"},
  ["B"], "In contrast to Conv, which must handle 1-D and 2-D, the pooling layer is required only for 2-D inputs.", 2)

a(T_CNN, "advanced", 3, "single_choice",
  "What must the max-pooling forward pass store for its backward pass?",
  {"A": "The full input tensor",
   "B": "The locations of the maxima, so the error can be routed back to them",
   "C": "The mean of each pooling window",
   "D": "Nothing; the backward pass is a plain reshape"},
  ["B"], "Max pooling routes the incoming error only to the argmax positions; every other element receives zero.", 2)

a(T_CNN, "basics", 1, "single_choice",
  "Why do pooling layers reduce overfitting according to the exercise description?",
  {"A": "They add noise to the activations",
   "B": "They reduce dimensionality and introduce a degree of scale and translation invariance",
   "C": "They penalise large weights",
   "D": "They randomly drop activations"},
  ["B"], "Fewer dimensions mean fewer downstream parameters, and small shifts of the input leave the pooled maximum unchanged.", 2)

# =========================================================================
# Exercise 3 - regularizers, dropout, batch norm, LeNet, TanH/Sigmoid,
#              RNN and LSTM
# =========================================================================

a(T_REG, "intermediate", 2, "single_choice",
  "Exercise 3 adds a boolean member to BaseLayer. Which one, and why?",
  {"A": "trainable, to mark layers with parameters",
   "B": "testing_phase, because some layers behave differently during training and testing",
   "C": "memorize, to carry hidden state between sequences",
   "D": "initialized, to avoid re-initialising weights"},
  ["B"], "Dropout and batch normalization need to know the phase; NeuralNetwork sets it through its phase property in train() and test().", 3)

a(T_REG, "intermediate", 2, "single_choice",
  "What is the purpose of the new Optimizer base class introduced in exercise 3?",
  {"A": "To implement calculate_update once for all optimizers",
   "B": "To provide add_regularizer(regularizer) and store the regularizer for every optimizer",
   "C": "To replace the deep copy in append_layer",
   "D": "To hold the learning rate schedule"},
  ["B"], "All optimizers inherit from it so that any of them can apply an L1 or L2 constraint.", 3)

a(T_REG, "intermediate", 2, "single_choice",
  "Which two methods must L1_Regularizer and L2_Regularizer provide?",
  {"A": "forward(weights) and backward(weights)",
   "B": "calculate_gradient(weights) and norm(weights)",
   "C": "penalty(weights) and derivative(weights)",
   "D": "initialize(weights) and update(weights)"},
  ["B"], "calculate_gradient supplies the (sub-)gradient for the optimizer; norm supplies the value added to the data loss.", 3)

a(T_REG, "basics", 1, "single_choice",
  "What does the constructor argument alpha of the regularizer classes represent?",
  {"A": "The learning rate",
   "B": "The regularization weight",
   "C": "The moving average decay",
   "D": "The dropout keep probability"},
  ["B"], "alpha scales how strongly the norm penalty influences the total loss and the gradient.", 3)

a(T_REG, "intermediate", 2, "single_choice",
  "Which prior assumption does L1 regularization encode, according to the exercise description?",
  {"A": "Small weights",
   "B": "Sparsity of the weights",
   "C": "Zero-mean weights",
   "D": "Orthogonal weights"},
  ["B"], "L1 pushes many weights exactly to zero, while L2 shrinks all weights towards small values.", 3)

a(T_REG, "advanced", 3, "single_choice",
  "Why does the L1 regularizer supply a sub-gradient rather than a gradient?",
  {"A": "Because the L1 norm is not differentiable at zero",
   "B": "Because L1 is applied only every second iteration",
   "C": "Because the weights are integers",
   "D": "Because the gradient would be too large numerically"},
  ["A"], "The absolute value has a kink at the origin, so a sub-gradient (e.g. the sign function) is used there.", 3)

a(T_REG, "advanced", 3, "single_choice",
  "Which layers must contribute their norm(weights) to the regularization loss in NeuralNetwork?",
  {"A": "Only the FullyConnected layers",
   "B": "FullyConnected, Convolution and RNN layers",
   "C": "All layers, including ReLU and Flatten",
   "D": "Only the last layer before the loss"},
  ["B"], "Every layer that carries trainable weights sums its norm into the total; parameter-free layers contribute nothing.", 3)

a(T_REG, "basics", 1, "single_choice",
  "What does the constructor argument 'probability' of the Dropout layer mean in exercise 3?",
  {"A": "The fraction of units to drop",
   "B": "The fraction of units to keep",
   "C": "The probability that dropout is active at all",
   "D": "The variance of the dropout noise"},
  ["B"], "The description defines it as the fraction of units to keep, so a value of 0.25 keeps a quarter of the activations.", 3)

a(T_REG, "advanced", 3, "single_choice",
  "In inverted dropout, what happens during training?",
  {"A": "Activations are scaled by p at test time",
   "B": "Surviving activations are scaled by 1/p during training, so nothing has to change at test time",
   "C": "The weights are scaled by 1/p after each update",
   "D": "The loss is divided by p"},
  ["B"], "Rescaling during training keeps the expected activation constant, which is exactly what lets the test-time forward pass be the identity.", 3)

a(T_REG, "intermediate", 2, "single_choice",
  "How must Dropout.forward behave in the testing phase?",
  {"A": "It drops units with the same probability as during training",
   "B": "It passes the input through unchanged",
   "C": "It scales the input by p",
   "D": "It returns zeros"},
  ["B"], "With inverted dropout the scaling has already been applied during training, so test-time forward is a pass-through.", 3)

a(T_REG, "intermediate", 2, "single_choice",
  "Which regularization problem does dropout specifically address, according to the exercise?",
  {"A": "Vanishing gradients",
   "B": "Co-adaptation of units, by enforcing more independent weights",
   "C": "Internal covariate shift",
   "D": "Class imbalance"},
  ["B"], "Because a unit cannot rely on any particular partner being present, the layer learns more redundant, independent features.", 3)

a(T_REG, "basics", 1, "single_choice",
  "What argument does the BatchNormalization constructor receive?",
  {"A": "channels, the number of channels of the input tensor",
   "B": "The batch size",
   "C": "The moving average decay alpha",
   "D": "The epsilon used for numerical stability"},
  ["A"], "The same argument covers both the vector case and the image case, where a scalar mean and variance are kept per channel.", 3)

a(T_REG, "intermediate", 2, "single_choice",
  "How does BatchNormalization.initialize set the weights gamma and the bias beta?",
  {"A": "gamma with zeros and beta with ones",
   "B": "gamma with ones and beta with zeros, ignoring any assigned initializer",
   "C": "Both with the assigned weights_initializer",
   "D": "Both uniformly random in [0, 1)"},
  ["B"], "Starting at gamma=1, beta=0 makes the layer an identity transform of the normalised signal, so it has no impact at the beginning of training.", 3)

a(T_REG, "intermediate", 2, "single_choice",
  "Which epsilon does the exercise require inside batch normalization?",
  {"A": "Smaller than 1e-10",
   "B": "Exactly 1e-3",
   "C": "Larger than 1e-5",
   "D": "Zero; no epsilon is needed"},
  ["A"], "The tests compare against a reference implementation, so a very small epsilon is required to stay within tolerance.", 3)

a(T_REG, "advanced", 3, "single_choice",
  "How does BatchNormalization estimate the mean and variance used at test time?",
  {"A": "By recomputing them over the whole training set after training",
   "B": "By a moving average updated during training, initialised with the batch statistics of the first batch",
   "C": "By reusing the current test batch statistics",
   "D": "They are fixed to 0 and 1"},
  ["B"], "Computing the true training set statistics is expensive, so an online estimate of the form mu = alpha*mu + (1-alpha)*mu_batch is kept.", 3)

a(T_REG, "advanced", 3, "single_choice",
  "In the moving average formulas of batch normalization, what does the exponent (k) denote?",
  {"A": "An exponent, as in Adam's bias correction",
   "B": "An iteration index",
   "C": "The channel index",
   "D": "The layer depth"},
  ["B"], "The exercise slides flag this explicitly, because in Adam the same-looking superscript is an exponent rather than an index.", 3)

a(T_REG, "advanced", 3, "single_choice",
  "In convolutional batch normalization, over what are the statistics computed?",
  {"A": "One scalar mean and variance per channel, shared across the spatial positions and the batch",
   "B": "One mean and variance per pixel position",
   "C": "One mean and variance per sample in the batch",
   "D": "A single scalar for the entire tensor"},
  ["A"], "This mirrors how a convolution shares one kernel across all spatial positions.", 3)

a(T_REG, "advanced", 3, "single_choice",
  "What does the reformat(tensor) method of BatchNormalization do?",
  {"A": "It normalises the tensor to zero mean and unit variance",
   "B": "It converts between the 4-D image-like and the 2-D vector-like tensor shape, in both directions",
   "C": "It transposes the batch and channel axes only",
   "D": "It casts the tensor to float64"},
  ["B"], "One method handles both directions by branching on the shape, which lets the vector implementation be reused for images.", 3)

a(T_REG, "intermediate", 2, "single_choice",
  "Helpers.py provides compute_bn_gradients(...). What does it compute?",
  {"A": "The gradient with respect to gamma and beta",
   "B": "The gradient with respect to the inputs, but not with respect to the weights",
   "C": "The moving average of mean and variance",
   "D": "The full backward pass of the layer"},
  ["B"], "The description notes explicitly that the weight gradients still have to be derived and implemented yourself.", 3)

a(T_ARCH, "intermediate", 2, "single_choice",
  "Which optimizer settings does the optional LeNet task of exercise 3 prescribe?",
  {"A": "SGD with learning rate 0.01 and no regularizer",
   "B": "Adam with learning rate 5e-4 and an L2 regularizer of weight 4e-4",
   "C": "Adam with learning rate 1e-3 and an L1 regularizer of weight 1e-4",
   "D": "SGD with momentum 0.9 and dropout 0.5"},
  ["B"], "The task also asks you to store the optimizer and initializer settings together with the network.", 3)

a(T_ARCH, "advanced", 3, "single_choice",
  "Why must the data_layer be excluded when a network is saved with pickle in exercise 3?",
  {"A": "It contains the labels, which would leak the test set",
   "B": "It is a generator object, which pickle cannot process",
   "C": "It is too large to store",
   "D": "It changes between training runs"},
  ["B"], "__getstate__ drops it and __setstate__ restores the dropped members as None, so the data layer must be set again after loading.", 3)

a(T_ARCH, "basics", 1, "single_choice",
  "Which activation function and which output layer does the LeNet variant of exercise 3 use?",
  {"A": "Sigmoid activations and a SoftMax output",
   "B": "ReLU activations and a SoftMax output",
   "C": "TanH activations and a Sigmoid output",
   "D": "ReLU activations and a linear output"},
  ["B"], "The exercise deliberately modernises the classic architecture and also ignores its original lack of padding.", 3)

a(T_RNN, "advanced", 3, "single_choice",
  "For TanH and Sigmoid, the exercise asks you to store the activations rather than the input tensor. Why?",
  {"A": "Activations use less memory",
   "B": "Because the derivative of both functions can be expressed purely in terms of the activation",
   "C": "Because the input is not available in the backward pass",
   "D": "To keep the layers non-trainable"},
  ["B"], "For the sigmoid the derivative is a(1-a) and for tanh it is 1-a^2, so caching the output is sufficient for the dynamic programming step.", 3)

a(T_RNN, "intermediate", 2, "single_choice",
  "What three arguments does the RNN constructor of exercise 3 receive?",
  {"A": "input_size, hidden_size, output_size",
   "B": "input_size, sequence_length, output_size",
   "C": "hidden_size, batch_size, output_size",
   "D": "input_size, hidden_size, num_layers"},
  ["A"], "The hidden state is initialised with zeros and has dimension hidden_size.", 3)

a(T_RNN, "advanced", 3, "single_choice",
  "What does the memorize property of the RNN layer control?",
  {"A": "Whether the layer stores its inputs for the backward pass",
   "B": "Whether the hidden state is carried over to the next forward call or reset to zeros",
   "C": "Whether the weights are shared across time steps",
   "D": "Whether the layer caches its gradients"},
  ["B"], "Carrying the state over is what turns backpropagation through time into truncated backpropagation through time.", 3)

a(T_RNN, "intermediate", 2, "single_choice",
  "Which dimension of the input tensor does the RNN layer treat as the time axis?",
  {"A": "The channel dimension",
   "B": "The batch dimension",
   "C": "The feature dimension",
   "D": "A separate fourth dimension"},
  ["B"], "The exercise reuses the existing tensor layout and reinterprets the batch dimension as the sequence over which the recurrence runs.", 3)

a(T_RNN, "advanced", 4, "single_choice",
  "In the RNN layer, which weights does the property gradient_weights refer to?",
  {"A": "The weights of the output gate only",
   "B": "The weights involved in computing the hidden state, as a single stacked tensor",
   "C": "The sum of all weights in the layer",
   "D": "The weights of the embedded TanH layer"},
  ["B"], "If the hidden state is produced by one fully connected layer fed with the stacked hidden state and input, those are the weights of the whole class.", 3)

a(T_RNN, "advanced", 4, "single_choice",
  "Why is it wrong to update the hidden-gate weights at every time step while iterating backwards through TBPTT?",
  {"A": "Because the optimizer would run out of memory",
   "B": "Because the Elman cell shares one weight set across all time steps, so changing them mid-pass makes forward and backward inconsistent",
   "C": "Because the gradients would become exactly zero",
   "D": "Because the hidden state would be reset"},
  ["B"], "You would be changing the function while differentiating it; the remedy is to accumulate the gradients and update once the backward pass is finished.", 3)

a(T_RNN, "intermediate", 2, "single_choice",
  "Why does exercise 3 introduce the LSTM as an alternative to the Elman cell?",
  {"A": "Because Elman cells cannot process sequences",
   "B": "Because Elman networks suffer severely from the vanishing gradient problem",
   "C": "Because the LSTM needs fewer parameters",
   "D": "Because the LSTM avoids the need for backpropagation through time"},
  ["B"], "The gated cell state gives gradients a path through time that is not repeatedly squashed by a saturating non-linearity.", 3)

a(T_RNN, "intermediate", 2, "single_choice",
  "Under what condition do the LSTM unit tests run in exercise 3?",
  {"A": "Always, they are part of the default suite",
   "B": "Only when a file LSTM.py exists in the Layers folder",
   "C": "Only with the Bonus flag",
   "D": "Only after the RNN tests pass"},
  ["B"], "The optional task is detected by the presence of the file, so the suite does not fail for students who skip it.", 3)

a(T_RNN, "intermediate", 2, "single_choice",
  "Which extra capabilities must the RNN layer provide so regularizers can be reused?",
  {"A": "An optimizer property and a calculate_regularization_loss() method",
   "B": "A dropout property and a norm() method",
   "C": "A phase property only",
   "D": "A memorize property only"},
  ["A"], "Together with initialize(weights_initializer, bias_initializer), this makes the RNN behave like any other trainable layer.", 3)

# =========================================================================
# Exercise 4 - PyTorch challenge: ChallengeDataset, ResNet, Trainer, ONNX
# =========================================================================

a(T_ARCH, "basics", 1, "single_choice",
  "What is the classification task of the exercise 4 PyTorch challenge?",
  {"A": "Handwritten digit recognition on MNIST",
   "B": "Detecting cracks and inactive regions in electroluminescence images of solar cells",
   "C": "Segmenting street scenes",
   "D": "Predicting stock prices from time series"},
  ["B"], "A current is applied to the module so the silicon emits near-infrared light, which specialised cameras capture for visual defect inspection.", 4)

a(T_CP, "advanced", 3, "single_choice",
  "Why is a SoftMax output with cross entropy unsuitable for the exercise 4 task?",
  {"A": "Because there are only two classes",
   "B": "Because the labels 'crack' and 'inactive' are not mutually exclusive, so it is a multi-label problem",
   "C": "Because the images are grayscale",
   "D": "Because SoftMax cannot be used with convolutional networks"},
  ["B"], "SoftMax assumes exactly one class is active; here a cell can be both cracked and inactive, which calls for per-class sigmoids and BCE.", 4)

a(T_CP, "intermediate", 2, "single_choice",
  "Which loss is used in export_onnx.py of exercise 4, and what does that imply about the output layer?",
  {"A": "CrossEntropyLoss, so the model outputs raw logits",
   "B": "BCELoss, so the model already applies a sigmoid to its outputs",
   "C": "MSELoss, so the task is treated as regression",
   "D": "NLLLoss, so the model outputs log-probabilities"},
  ["B"], "t.nn.BCELoss expects probabilities, which matches the Sigmoid at the end of the prescribed ResNet.", 4)

a(T_CP, "intermediate", 2, "single_choice",
  "What must ChallengeDataset inherit from, and what does its constructor receive?",
  {"A": "torch.nn.Module; it receives the model and the optimizer",
   "B": "torch.utils.data.Dataset; it receives a pandas dataframe and a mode flag ('train' or 'val')",
   "C": "torchvision.datasets.ImageFolder; it receives a directory path",
   "D": "torch.utils.data.DataLoader; it receives a batch size"},
  ["B"], "Subclassing Dataset means implementing __len__ and __getitem__ so a DataLoader can batch and shuffle the samples.", 4)

a(T_CP, "intermediate", 2, "single_choice",
  "Which two methods must be overwritten in ChallengeDataset?",
  {"A": "forward and backward",
   "B": "__len__ and __getitem__",
   "C": "train_step and val_test_step",
   "D": "fit and predict"},
  ["B"], "__len__ reports the number of samples and __getitem__ returns one (image, label) tuple as torch tensors.", 4)

a(T_CP, "intermediate", 2, "single_choice",
  "Why does __getitem__ call skimage.color.gray2rgb on the solar cell images?",
  {"A": "To improve the contrast of the defects",
   "B": "Because the raw data is grayscale but the network expects three input channels",
   "C": "Because PyTorch cannot store single-channel tensors",
   "D": "To apply colour-based data augmentation"},
  ["B"], "The prescribed ResNet starts with Conv2D(3, 64, 7, 2), and the normalisation constants are also given per three channels.", 4)

a(T_CP, "intermediate", 2, "single_choice",
  "Which transforms must the Compose object of exercise 4 contain at minimum?",
  {"A": "Resize(), RandomCrop() and ToTensor()",
   "B": "ToPILImage(), ToTensor() and Normalize()",
   "C": "Normalize() and RandomHorizontalFlip()",
   "D": "ToTensor() only"},
  ["B"], "Normalize needs the mean and standard deviation of the training data, both of which the skeleton provides.", 4)

a(T_CP, "advanced", 3, "single_choice",
  "Why does the exercise suggest defining two different transform chains?",
  {"A": "Because validation images have a different resolution",
   "B": "Because augmentation belongs in the training chain but not in the validation chain",
   "C": "Because the labels differ between the two modes",
   "D": "Because the GPU requires a different data type at validation time"},
  ["B"], "Augmenting the validation set would make the reported score depend on random transforms rather than on model quality.", 4)

a(T_ARCH, "intermediate", 2, "single_choice",
  "What does one ResBlock in the exercise 4 ResNet consist of?",
  {"A": "A single Conv2D followed by ReLU",
   "B": "The sequence (Conv2D, BatchNorm, ReLU) repeated twice, with the skip connection added after the second BatchNorm and ReLU applied afterwards",
   "C": "Two fully connected layers with a skip connection",
   "D": "A Conv2D followed by MaxPool and Dropout"},
  ["B"], "The ordering matters: the shortcut is added before the final activation, not after it.", 4)

a(T_ARCH, "intermediate", 2, "single_choice",
  "What filter size do all Conv2D layers inside a ResBlock use?",
  {"A": "1",
   "B": "3",
   "C": "5",
   "D": "7"},
  ["B"], "Only the stem convolution of the network uses a 7x7 kernel; inside the blocks the kernels are 3x3.", 4)

a(T_ARCH, "advanced", 3, "single_choice",
  "Within a ResBlock, which convolution carries the stride?",
  {"A": "Both convolutions",
   "B": "The first convolution; the second uses no stride",
   "C": "The second convolution only",
   "D": "Neither; striding happens in the pooling layer"},
  ["B"], "The first convolution performs the spatial downsampling and the second keeps the resolution, so the block halves the size at most once.", 4)

a(T_ARCH, "advanced", 3, "single_choice",
  "Why must the input of a ResBlock sometimes be transformed before it is added to the output?",
  {"A": "Because the addition would otherwise be a concatenation",
   "B": "Because the stride and the number of channels can change inside the block, so the shapes would not match",
   "C": "Because the input has to be normalised first",
   "D": "Because ReLU cannot be applied to the raw input"},
  ["B"], "The recommended fix is a 1x1 convolution with the matching stride and channel count, followed by a batch norm.", 4)

a(T_ARCH, "advanced", 3, "single_choice",
  "In the prescribed ResNet, what are the channel counts of the four ResBlocks in order?",
  {"A": "64, 64, 128, 256",
   "B": "64->64, 64->128, 128->256, 256->512",
   "C": "32->64, 64->128, 128->256, 256->512",
   "D": "3->64, 64->128, 128->256, 256->512"},
  ["B"], "Only the first block keeps its channel count; the remaining three double the channels while halving the resolution with stride 2.", 4)

a(T_ARCH, "intermediate", 2, "single_choice",
  "Which layers follow the last ResBlock in the exercise 4 architecture?",
  {"A": "Flatten, FC(512, 2) and Sigmoid",
   "B": "GlobalAvgPool, Flatten, FC(512, 2) and Sigmoid",
   "C": "MaxPool, Flatten, FC(512, 2) and SoftMax",
   "D": "GlobalAvgPool and SoftMax"},
  ["B"], "Global average pooling reduces each of the 512 feature maps to one value, so the classifier sees a 512-dimensional vector regardless of input size.", 4)

a(T_ARCH, "intermediate", 2, "single_choice",
  "The final fully connected layer is FC(512, 2). What do the two outputs represent?",
  {"A": "The two mutually exclusive classes 'defect' and 'no defect'",
   "B": "The two independent labels 'crack' and 'inactive'",
   "C": "The bounding box coordinates of the defect",
   "D": "The mean and variance of the prediction"},
  ["B"], "Each output gets its own sigmoid, since a cell can exhibit both defects, only one, or neither.", 4)

a(T_CP, "basics", 1, "single_choice",
  "What is the early stopping criterion used in the exercise 4 Trainer?",
  {"A": "Stop when the training loss stops decreasing",
   "B": "Stop when the validation loss does not decrease for a specified number of epochs",
   "C": "Stop after a fixed number of epochs",
   "D": "Stop when the learning rate reaches zero"},
  ["B"], "The patience is passed to the Trainer as early_stopping_patience; a value of -1 disables it, in which case an epoch count must be given.", 4)

a(T_CP, "intermediate", 2, "single_choice",
  "Why must the gradients be reset at the start of each training step in PyTorch?",
  {"A": "Because the optimizer would otherwise use the wrong learning rate",
   "B": "Because PyTorch accumulates (sums up) gradients on every backward() call by default",
   "C": "Because the loss would otherwise be negative",
   "D": "Because the model would stay in evaluation mode"},
  ["B"], "Without zeroing, each step would apply the sum of all gradients seen so far rather than the current batch's gradient.", 4)

a(T_CP, "intermediate", 2, "single_choice",
  "Why does the validation step call model.eval() before iterating the validation set?",
  {"A": "To move the model to the CPU",
   "B": "Because layers such as Dropout and BatchNorm behave differently during training and testing",
   "C": "To reset the optimizer state",
   "D": "To enable gradient computation"},
  ["B"], "This is the PyTorch equivalent of the testing_phase flag added to BaseLayer in exercise 3.", 4)

a(T_CP, "intermediate", 2, "single_choice",
  "Why are gradients disabled during validation in the exercise 4 Trainer?",
  {"A": "Because the validation loss would otherwise be wrong",
   "B": "Because no weight update happens, so building the graph only wastes memory and time",
   "C": "Because the validation set has no labels",
   "D": "Because early stopping requires it"},
  ["B"], "Wrapping the loop in a no-grad context skips the autograd bookkeeping entirely.", 4)

a(T_CP, "intermediate", 2, "single_choice",
  "Which metric does the exercise 4 skeleton import from scikit-learn for evaluation?",
  {"A": "accuracy_score",
   "B": "f1_score",
   "C": "roc_auc_score",
   "D": "mean_squared_error"},
  ["B"], "The F1 score balances precision and recall, which matters because defective cells are the minority in this dataset.", 4)

a(T_CP, "basics", 1, "single_choice",
  "What is the purpose of save_onnx in the exercise 4 Trainer?",
  {"A": "To save the training checkpoints during the run",
   "B": "To export the trained model in a portable format for submission to the leader board",
   "C": "To store the dataset statistics",
   "D": "To serialise the optimizer state"},
  ["B"], "ONNX is a framework-independent exchange format; the export runs the model once on a dummy input to trace the graph.", 4)

a(T_CP, "advanced", 3, "single_choice",
  "The ONNX export declares dynamic_axes for input and output with batch_size at axis 0. Why?",
  {"A": "So the exported model accepts an arbitrary batch size at inference time",
   "B": "So the model can accept images of arbitrary spatial size",
   "C": "So the number of classes can change",
   "D": "So the model can run on multiple GPUs"},
  ["A"], "Everything else is traced with fixed shapes; marking axis 0 dynamic keeps the batch dimension free.", 4)

a(T_CP, "intermediate", 2, "single_choice",
  "How does the exercise 4 pipeline obtain a validation set?",
  {"A": "A separate CSV file with validation samples is provided",
   "B": "By splitting the data from data.csv with a train-test split",
   "C": "By using the leader board test set",
   "D": "By holding out the last batch of every epoch"},
  ["B"], "train.py imports train_test_split from sklearn.model_selection for exactly this purpose.", 4)

a(T_CP, "basics", 1, "single_choice",
  "What does each row of data.csv in exercise 4 contain?",
  {"A": "The image path and a single class index",
   "B": "The image path plus two numbers indicating 'crack' and 'inactive'",
   "C": "The raw pixel values of one image",
   "D": "The image path and a bounding box"},
  ["B"], "Two independent binary flags per row is what makes this a multi-label rather than a multi-class problem.", 4)

a(T_CP, "advanced", 3, "single_choice",
  "Why does the exercise recommend training on university machines rather than a laptop?",
  {"A": "Because the dataset may not be copied off campus",
   "B": "Because training neural networks needs substantial compute, and those machines provide GPUs",
   "C": "Because PyTorch is licensed per machine",
   "D": "Because the unit tests only run there"},
  ["B"], "The recommendation is to debug locally and run the actual training remotely, loading the python3 and torch modules first.", 4)

a(T_CP, "intermediate", 2, "single_choice",
  "Which two defect types does the exercise 4 dataset distinguish, and how do they relate?",
  {"A": "Cracks and inactive regions; inactive regions are often caused by cracks but are labelled independently",
   "B": "Cracks and dirt; they never co-occur",
   "C": "Inactive regions and shading; both are labelled as one class",
   "D": "Cracks and cell breakage; the second implies the first"},
  ["A"], "A cell is only labelled cracked when the crack is visible, and the two labels are treated as independent despite the physical link.", 4)

# =========================================================================
# Cross-exercise / framework-wide questions
# =========================================================================

a(T_NN, "intermediate", 2, "multiple_choice",
  "Which of the following layers in the exercise framework are trainable? (Select all that apply)",
  {"A": "FullyConnected",
   "B": "ReLU",
   "C": "Convolutional",
   "D": "BatchNormalization"},
  ["A", "C", "D"], "ReLU is a fixed non-linearity with no parameters; the other three all carry weights that an optimizer updates.", 3)

a(T_NN, "intermediate", 2, "multiple_choice",
  "Which layers of the exercise framework behave differently in the training and the testing phase? (Select all that apply)",
  {"A": "Dropout",
   "B": "BatchNormalization",
   "C": "Flatten",
   "D": "SoftMax"},
  ["A", "B"], "This is exactly why exercise 3 adds the testing_phase member to BaseLayer and the phase property to NeuralNetwork.", 3)

a(T_LO, "intermediate", 2, "multiple_choice",
  "Which optimizers are implemented across exercises 1 and 2? (Select all that apply)",
  {"A": "Sgd",
   "B": "SgdWithMomentum",
   "C": "Adam",
   "D": "RMSprop"},
  ["A", "B", "C"], "RMSprop is not part of the exercise sheet, although Adam's second moment term plays a similar role.", 2)

a(T_NN, "advanced", 3, "multiple_choice",
  "Which properties or methods must a fully trainable layer expose so it works with the finished framework? (Select all that apply)",
  {"A": "An optimizer property",
   "B": "A gradient_weights property",
   "C": "An initialize(weights_initializer, bias_initializer) method",
   "D": "A phase property that sets the phase of all other layers"},
  ["A", "B", "C"], "The phase property belongs to NeuralNetwork, which pushes the flag down into its layers; individual layers only carry testing_phase.", 3)

a(T_NN, "intermediate", 2, "multiple_choice",
  "Which statements about the exercise framework's NeuralNetwork class are true? (Select all that apply)",
  {"A": "It has no explicit knowledge of the graph structure beyond a list of layers",
   "B": "It supports exactly one data source and one loss function",
   "C": "It stores the loss for every training iteration",
   "D": "It computes the gradients itself rather than delegating to the layers"},
  ["A", "B", "C"], "Each layer implements its own backward pass; the network only orchestrates the order in which they are called.", 1)

a(T_CNN, "advanced", 3, "multiple_choice",
  "Which statements about the exercise Conv layer are true? (Select all that apply)",
  {"A": "num_kernels determines the number of output channels",
   "B": "1x1 convolutions and 1-D convolutions must be handled correctly",
   "C": "The layer must use valid padding across the image plane",
   "D": "It must expose gradient_weights and gradient_bias"},
  ["A", "B", "D"], "The image plane uses same (zero) padding; it is the channel axis that is treated as a valid convolution.", 2)

# =========================================================================
# Additional basics-level questions, so an exercises-only paper can still
# hold the 45/35/20 mixed ratio at a full 100-point target.
# =========================================================================

a(T_INTRO, "basics", 1, "single_choice",
  "Which two libraries does exercise 0 ask you to import for calculation and visualisation?",
  {"A": "pandas and seaborn",
   "B": "numpy and matplotlib.pyplot",
   "C": "torch and torchvision",
   "D": "scipy and PIL"},
  ["B"], "The conventional aliases np and plt are used throughout the exercise sheets.", 0)

a(T_INTRO, "basics", 1, "single_choice",
  "In which instance variable does every exercise 0 pattern class store its result?",
  {"A": "result",
   "B": "output",
   "C": "pattern",
   "D": "data"},
  ["B"], "The unit tests read this member directly, so the name is fixed by the exercise.", 0)

a(T_CP, "basics", 1, "single_choice",
  "What does ImageGenerator.class_name(int_label) return?",
  {"A": "The filename of the image",
   "B": "The class name corresponding to the integer label",
   "C": "The number of samples in that class",
   "D": "The one-hot encoding of the label"},
  ["B"], "It is used to title the subplots produced by show().", 0)

a(T_CP, "basics", 1, "single_choice",
  "Which flags of the ImageGenerator constructor default to False?",
  {"A": "rotation, mirroring and shuffle",
   "B": "batch_size and image_size",
   "C": "resize and normalize",
   "D": "train and validate"},
  ["A"], "Augmentation and shuffling are opt-in, so the generator returns the raw data in file order unless asked otherwise.", 0)

a(T_NN, "basics", 1, "single_choice",
  "In which folder does the exercise framework place FullyConnected.py, ReLU.py and SoftMax.py?",
  {"A": "Optimization",
   "B": "Layers",
   "C": "Models",
   "D": "src_to_implement root"},
  ["B"], "Optimizers.py, Loss.py and Constraints.py go into Optimization; the layers live in Layers.", 1)

a(T_LO, "basics", 1, "single_choice",
  "In which file and folder is the CrossEntropyLoss class implemented?",
  {"A": "Loss.py in Optimization",
   "B": "CrossEntropy.py in Layers",
   "C": "Loss.py in Layers",
   "D": "NeuralNetwork.py in the root folder"},
  ["A"], "The loss is grouped with the optimizers rather than the layers, mirroring the fact that it does not inherit BaseLayer.", 1)

a(T_NN, "basics", 1, "single_choice",
  "Which method adds a layer to the network and wires up its optimizer?",
  {"A": "add(layer)",
   "B": "append_layer(layer)",
   "C": "push(layer)",
   "D": "register(layer)"},
  ["B"], "It also initialises trainable layers with the network's stored weight and bias initializers.", 1)

a(T_NN, "basics", 1, "single_choice",
  "What does the 'loss' member of the NeuralNetwork class hold?",
  {"A": "The loss layer object",
   "B": "A list with the loss value of each training iteration",
   "C": "The current gradient of the loss",
   "D": "The regularization weight"},
  ["B"], "The loss layer itself is kept separately in loss_layer; this list is what you plot to inspect convergence.", 1)

a(T_CNN, "basics", 1, "single_choice",
  "What determines the number of output channels of the exercise Conv layer?",
  {"A": "The number of input channels",
   "B": "num_kernels",
   "C": "The stride shape",
   "D": "The batch size"},
  ["B"], "Each kernel spans every input channel and contributes exactly one output feature map.", 2)

a(T_CNN, "basics", 1, "single_choice",
  "Which form of pooling does exercise 2 ask you to implement?",
  {"A": "Average pooling",
   "B": "Max pooling",
   "C": "Global average pooling",
   "D": "Stochastic pooling"},
  ["B"], "It is described as the most common form; average pooling only reappears in the PyTorch ResNet of exercise 4.", 2)

a(T_NN, "basics", 1, "single_choice",
  "Which distribution does the UniformRandom initializer draw from?",
  {"A": "The interval [0, 1)",
   "B": "The interval [-1, 1]",
   "C": "A standard normal distribution",
   "D": "A Bernoulli distribution"},
  ["A"], "It matches the simple initialisation used in exercise 1 before Xavier and He are introduced.", 2)

a(T_LO, "basics", 1, "single_choice",
  "Which file holds the Sgd, SgdWithMomentum and Adam classes?",
  {"A": "Optimizers.py in the Optimization folder",
   "B": "Optimizers.py in the Layers folder",
   "C": "Adam.py in the Optimization folder",
   "D": "NeuralNetwork.py in the root folder"},
  ["A"], "All three share the calculate_update interface, so they sit in one module.", 2)

a(T_REG, "basics", 1, "single_choice",
  "In which file are L1_Regularizer and L2_Regularizer implemented?",
  {"A": "Constraints.py in the Optimization folder",
   "B": "Regularizers.py in the Layers folder",
   "C": "Constraints.py in the Layers folder",
   "D": "Loss.py in the Optimization folder"},
  ["A"], "The name reflects that they are norm constraints on the weights rather than layers.", 3)

a(T_REG, "basics", 1, "single_choice",
  "Which two trainable parameters does the BatchNormalization layer have?",
  {"A": "mean and variance",
   "B": "the weights gamma and the bias beta",
   "C": "alpha and epsilon",
   "D": "It has no trainable parameters"},
  ["B"], "The mean and variance are statistics estimated from the data, not parameters learned by the optimizer.", 3)

a(T_REG, "basics", 1, "single_choice",
  "Which layer of the exercise framework is described as most often used to regularize fully connected layers?",
  {"A": "BatchNormalization",
   "B": "Dropout",
   "C": "Pooling",
   "D": "Flatten"},
  ["B"], "Fully connected layers hold most of the parameters, which is where co-adaptation is most likely.", 3)

a(T_RNN, "basics", 1, "single_choice",
  "Which two activation layers are added in exercise 3 for use inside recurrent cells?",
  {"A": "ReLU and SoftMax",
   "B": "TanH and Sigmoid",
   "C": "LeakyReLU and ELU",
   "D": "Sigmoid and SoftMax"},
  ["B"], "Both are bounded, which is what keeps the recurrent state from growing without limit.", 3)

a(T_RNN, "basics", 1, "single_choice",
  "What is the name of the simple recurrent cell implemented in exercise 3?",
  {"A": "The Jordan network",
   "B": "The Elman network",
   "C": "The Hopfield network",
   "D": "The gated recurrent unit"},
  ["B"], "It is described as the simplest RNN cell and can be assembled modularly from layers you already built.", 3)

a(T_RNN, "basics", 1, "single_choice",
  "How is the hidden state of the RNN layer initialised?",
  {"A": "With all zeros",
   "B": "Uniformly random in [0, 1)",
   "C": "With the He initializer",
   "D": "With the first input tensor"},
  ["A"], "It is reset to zeros for each new sequence unless memorize is True.", 3)

a(T_ARCH, "basics", 1, "single_choice",
  "Which library does exercise 4 use instead of the hand-written framework?",
  {"A": "TensorFlow",
   "B": "PyTorch",
   "C": "JAX",
   "D": "scikit-learn"},
  ["B"], "It builds data flow graphs whose nodes are operations and whose edges are tensors.", 4)

a(T_ARCH, "basics", 1, "single_choice",
  "Which architecture do you implement in exercise 4?",
  {"A": "A variant of ResNet",
   "B": "A variant of VGG",
   "C": "A U-Net",
   "D": "An LSTM"},
  ["A"], "Its defining component is the ResBlock, a pair of convolution blocks augmented with a skip connection.", 4)

a(T_CP, "basics", 1, "single_choice",
  "What base class must the exercise 4 ResNet model inherit from?",
  {"A": "torch.utils.data.Dataset",
   "B": "torch.nn.Module",
   "C": "torch.optim.Optimizer",
   "D": "torchvision.models.ResNet"},
  ["B"], "Subclassing Module is what registers the parameters and enables the standard training workflow.", 4)

a(T_CP, "basics", 1, "single_choice",
  "In the exercise 4 Trainer, what does a negative early_stopping_patience mean?",
  {"A": "Training stops immediately",
   "B": "Early stopping is disabled, so an epoch count must be given instead",
   "C": "The patience is counted in batches rather than epochs",
   "D": "The validation loss is ignored"},
  ["B"], "The fit method asserts that either the patience or the epoch count is positive.", 4)
