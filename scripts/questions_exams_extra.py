"""A second batch of questions adapted from the past DL exams.

The first batch (questions_exams.py) covered the single- and multiple-choice
sections. This module works through the parts that were left: the short-answer
sections, the numeric/derivation tasks and the coding section, all rewritten as
multiple choice. Answers are checked against the official solution PDFs of
SS21, WS20/21, WS21/22, SS22 and the WiSe20/21 mock.
"""

E2 = []


def a(topic, diff, pts, qtype, q, opts, corr, expl):
    E2.append({"topic": topic, "difficulty": diff, "points": pts, "type": qtype,
               "question": q, "options": opts, "correct_answers": corr,
               "explanation": expl, "source": "past exams"})


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

# ---------------- Neural networks, bias, capacity ---------------------------

a(T_NN, "intermediate", 2, "single_choice",
  "Why is it useful to learn a bias term in addition to the weights?",
  {"A": "It guarantees the activations stay positive",
   "B": "It shifts the activation function, so the decision boundary need not pass through the origin",
   "C": "It normalises the input distribution",
   "D": "It prevents the weights from growing too large"},
  ["B"], "Without a bias, every layer computes a purely linear map through the origin, which severely restricts the functions the network can represent.")

a(T_NN, "intermediate", 2, "single_choice",
  "What does the model capacity of a network describe?",
  {"A": "The number of training samples it was optimised with",
   "B": "The variety of functions it can approximate",
   "C": "The amount of GPU memory it occupies",
   "D": "The maximum batch size it can process"},
  ["B"], "Capacity is a property of the model class, not of the dataset; it grows with depth and width and sits at the centre of the bias-variance trade-off.")

a(T_NN, "advanced", 3, "multiple_choice",
  "Which statements about model capacity are TRUE? (Select all that apply)",
  {"A": "It is linked to the variety of functions that can be approximated",
   "B": "It is influenced by the depth of the network",
   "C": "It is closely related to the bias-variance trade-off",
   "D": "Increasing capacity necessarily increases the bias of the prediction"},
  ["A", "B", "C"], "Higher capacity typically lowers bias and raises variance, so the last statement has the relationship backwards.")

a(T_NN, "advanced", 3, "single_choice",
  "You feed a network trained on ImageNet a blank image where every pixel has the same white value. Will it output the same score for every class?",
  {"A": "Yes, because a constant input carries no class information",
   "B": "No, because the weights and biases differ per class, so a constant input still produces different scores",
   "C": "Yes, but only if the last layer is a SoftMax",
   "D": "It cannot be determined without knowing the architecture"},
  ["B"], "A constant input is still multiplied by different weight vectors, so the logits differ; uniform output would require identical weights per class.")

a(T_NN, "advanced", 3, "single_choice",
  "In a network with two fully connected layers and no non-linearity between them, why is the model no more expressive than a single layer?",
  {"A": "Because the second layer's weights are always zero",
   "B": "Because the composition of two linear maps is again a linear map, W = W2 W1 with bias W2 b1 + b2",
   "C": "Because the gradients cancel out",
   "D": "Because the batch dimension collapses"},
  ["B"], "Only a non-linearity between the layers lets the network represent functions a single affine map cannot.")

a(T_NN, "intermediate", 2, "single_choice",
  "Data normalisation example: a feature has mean 82 and standard deviation 40, and the observed value is 22. What is the normalised value?",
  {"A": "-1.5",
   "B": "1.5",
   "C": "-0.6",
   "D": "-60"},
  ["A"], "Standardisation subtracts the mean and divides by the standard deviation: (22 - 82) / 40 = -1.5.")

a(T_NN, "advanced", 3, "single_choice",
  "A two-feature dataset is normalised to (-1, -1), (-1, 1), (1, -1), (1, 1) with alternating labels along the diagonals. Was a single-layer perceptron a good choice?",
  {"A": "Yes, the data is linearly separable after normalisation",
   "B": "No, the distribution is an XOR problem, which a single-layer perceptron cannot solve",
   "C": "Yes, because normalisation always makes data separable",
   "D": "No, because the data must first be augmented"},
  ["B"], "XOR requires at least one hidden layer; no single hyperplane separates the two diagonal pairs.")

# ---------------- Activations and CNN --------------------------------------

a(T_CNN, "intermediate", 2, "single_choice",
  "How do you connect the output of a convolutional layer to the input of a fully connected layer?",
  {"A": "By inserting a flatten layer that reshapes the feature maps into a vector",
   "B": "By averaging all channels into a single scalar",
   "C": "By transposing the feature maps",
   "D": "By adding a second convolutional layer with kernel size equal to the image size"},
  ["A"], "Flattening (or global pooling) turns the multi-dimensional feature maps into the one-dimensional vector the fully connected layer expects.")

a(T_CNN, "advanced", 3, "single_choice",
  "A network flattens a feature map and applies a fully connected layer. A colleague replaces this with a convolution whose kernel covers the whole feature map. How do the two compare?",
  {"A": "The convolution has far fewer parameters",
   "B": "They are equivalent; the convolutional version avoids the explicit flatten and may be implemented more efficiently",
   "C": "The convolution cannot produce the same output",
   "D": "The fully connected version is translation invariant, the convolutional one is not"},
  ["B"], "A convolution whose kernel spans the entire input is exactly a fully connected layer written in convolutional form.")

a(T_CNN, "intermediate", 2, "single_choice",
  "An image is (X, X) and a fully connected layer produces Z outputs. Ignoring the bias, how many weights does it need?",
  {"A": "X * Z",
   "B": "X^2 * Z",
   "C": "X^2 + Z",
   "D": "X * Z^2"},
  ["B"], "Every one of the X^2 input pixels connects to every one of the Z output neurons.")

a(T_CNN, "intermediate", 2, "single_choice",
  "The same image is processed by a convolutional layer with N kernels of size (K, K) on a single input channel. Ignoring bias, how many weights does it need?",
  {"A": "N * K^2",
   "B": "X^2 * N",
   "C": "K^2 * X^2",
   "D": "N * K"},
  ["A"], "Weight sharing makes the parameter count independent of the image size, which is the key advantage over the fully connected layer.")

a(T_CNN, "advanced", 3, "single_choice",
  "For a 2-D convolution with an EVEN filter width k and stride 1, what padding gives an output of the same size as the input?",
  {"A": "k/2 on both sides",
   "B": "Asymmetric padding: k/2 - 1 on one side and k/2 on the other",
   "C": "(k-1)/2 on both sides",
   "D": "Same size output is impossible for even k"},
  ["B"], "Odd kernels allow the symmetric (k-1)/2; an even kernel has no centre pixel, so the two sides must differ by one.")


a(T_CNN, "intermediate", 2, "single_choice",
  "Which statement about a 'valid' convolution is FALSE?",
  {"A": "It outputs an image of the same size as its input",
   "B": "It applies no padding",
   "C": "It discards border positions where the kernel does not fully overlap the input",
   "D": "It produces a smaller output than a 'same' convolution with the same kernel"},
  ["A"], "That describes 'same' convolution. A valid convolution shrinks the output by k-1 in each spatial dimension.")

a(T_CNN, "intermediate", 2, "single_choice",
  "A CONV layer has 16 kernels applied to an input with 3 channels. How many channels does the output have?",
  {"A": "3",
   "B": "16",
   "C": "48",
   "D": "19"},
  ["B"], "Each kernel spans all input channels and produces exactly one output feature map, so the number of kernels sets the output depth.")

a(T_CNN, "advanced", 3, "single_choice",
  "A pytorch model applies nn.Conv2d(3, 16, 3, padding=1) to an input of shape 256 x 256 x 3, and later maps back to 3 channels with the same padding. What is the output shape?",
  {"A": "254 x 254 x 3",
   "B": "256 x 256 x 3",
   "C": "128 x 128 x 16",
   "D": "256 x 256 x 16"},
  ["B"], "A 3x3 kernel with padding 1 and stride 1 preserves the spatial size, so only the channel count changes through the network.")

a(T_CNN, "advanced", 3, "single_choice",
  "Why is a stride greater than 1 sometimes described as subsampling?",
  {"A": "Because it averages neighbouring pixels",
   "B": "Because it evaluates the convolution only at every s-th position, discarding the intermediate outputs",
   "C": "Because it reduces the number of channels",
   "D": "Because it applies the kernel to a random subset of positions"},
  ["B"], "That equivalence is exactly why a strided convolution can be implemented as a stride-1 convolution followed by dropping rows and columns.")

a(T_CNN, "advanced", 4, "single_choice",
  "A strided convolution is implemented as stride-1 convolution plus subsampling. What must happen to the error tensor in the backward pass?",
  {"A": "It must be scaled by the stride",
   "B": "It must be padded with zeros at the rows and columns that were discarded in the forward pass",
   "C": "It must be transposed",
   "D": "It must be averaged over the stride window"},
  ["B"], "Positions that produced no output receive no gradient, so inserting zeros restores the shape the stride-1 backward pass expects.")

# ---------------- Regularization and batch norm -----------------------------

a(T_REG, "intermediate", 2, "single_choice",
  "Name a plausible cause of internal covariate shift.",
  {"A": "The distribution of a layer's inputs changes as the parameters of the preceding layers are updated",
   "B": "The test set is drawn from a different population than the training set",
   "C": "The learning rate is too small",
   "D": "The loss function is non-convex"},
  ["A"], "Because every layer's input is the previous layer's output, updating early layers shifts the distribution that later layers have to cope with.")

a(T_REG, "advanced", 3, "multiple_choice",
  "Which situations contribute to internal covariate shift? (Select all that apply)",
  {"A": "Weight updates in earlier layers changing the distribution seen by later layers",
   "B": "Unnormalised input data with widely differing feature scales",
   "C": "Using a fixed random seed",
   "D": "Large learning rates causing large parameter changes per step"},
  ["A", "B", "D"], "The seed only fixes the initialisation and shuffling order; it does not affect how distributions drift during training.")

a(T_REG, "intermediate", 2, "single_choice",
  "You train one network with L2 regularization and one with L1. How do the weights differ from an unregularised run?",
  {"A": "L2 gives sparser weights, L1 gives uniformly smaller weights",
   "B": "L2 gives smaller weights overall, L1 gives sparser weights with many close to zero",
   "C": "Both give identical weight distributions",
   "D": "L1 increases the weights, L2 decreases them"},
  ["B"], "The quadratic penalty shrinks large weights hardest, whereas the absolute-value penalty has constant gradient magnitude and drives small weights to exactly zero.")

a(T_REG, "advanced", 3, "single_choice",
  "Which observation about a trained weight histogram most strongly suggests L1 rather than L2 regularization?",
  {"A": "A narrow Gaussian centred at zero",
   "B": "A sharp spike exactly at zero with a spread of non-zero weights around it",
   "C": "A bimodal distribution with peaks at -1 and 1",
   "D": "A uniform distribution over [-1, 1]"},
  ["B"], "L2 shrinks everything smoothly towards zero, so it yields a narrow bell shape rather than an atom of mass exactly at zero.")

# ---------------- Loss and optimization ------------------------------------

a(T_LO, "intermediate", 2, "single_choice",
  "Three loss-over-iteration curves are observed for the same task, with noise levels high, medium and almost none. Which ordering matches SGD, mini-batch GD and batch GD?",
  {"A": "SGD is the noisiest, mini-batch is intermediate, batch GD is the smoothest",
   "B": "Batch GD is the noisiest, SGD the smoothest",
   "C": "All three are equally noisy",
   "D": "Mini-batch GD is the noisiest"},
  ["A"], "The gradient estimate averages over more samples as the batch grows, so its variance and therefore the curve noise shrink.")


a(T_LO, "advanced", 3, "single_choice",
  "A GAN is trained with mini-batches in which all dog images come first, then all cat images. Why is this a problem?",
  {"A": "The batches are too large",
   "B": "Each mini-batch gradient is biased towards one class, so the updates oscillate instead of approximating the full-data gradient",
   "C": "The discriminator cannot process two classes",
   "D": "It is not a problem as long as every image is seen once per epoch"},
  ["B"], "Mini-batch gradient descent assumes each batch is a representative sample; sorted batches break that assumption badly.")



a(T_LO, "advanced", 3, "single_choice",
  "Why does a classifier that ends with ReLU followed by sigmoid, thresholded at 0.5, classify every sample as positive?",
  {"A": "Because the sigmoid saturates",
   "B": "Because the ReLU output is always >= 0, so the sigmoid output is always >= 0.5",
   "C": "Because the loss function is wrong",
   "D": "Because the weights were initialised with zeros"},
  ["B"], "sigmoid(0) = 0.5 and the function is monotonic, so a non-negative pre-activation can never fall below the threshold.")

a(T_LO, "advanced", 3, "single_choice",
  "Would a step-like activation that is 0 for x < -0.5, x on [-0.5, 0.5] and 1 for x > 0.5 train well with SGD?",
  {"A": "Yes, it behaves like a bounded ReLU",
   "B": "No, because the gradient is zero almost everywhere outside the narrow linear region",
   "C": "Yes, because it is bounded",
   "D": "No, because it is not continuous"},
  ["B"], "Backpropagation multiplies by the derivative, so units driven into the flat regions stop receiving any learning signal.")

# ---------------- Recurrent networks ---------------------------------------

a(T_RNN, "advanced", 3, "single_choice",
  "A simplified Elman cell has h_t = ReLU(w_hh * h_{t-1} + w_xh * x_t) with w_hh = 1, w_xh = 2, h_0 = 0 and x_1 = 2. What is h_1?",
  {"A": "2",
   "B": "4",
   "C": "0",
   "D": "6"},
  ["B"], "The recurrent contribution is zero at t = 1, so h_1 = ReLU(2 * 2) = 4.")

a(T_RNN, "advanced", 4, "single_choice",
  "Continuing that cell with x_2 = -1, w_hh = 1, w_xh = 2 and h_1 = 4, what is h_2?",
  {"A": "0",
   "B": "2",
   "C": "4",
   "D": "6"},
  ["B"], "h_2 = ReLU(1 * 4 + 2 * (-1)) = ReLU(2) = 2, so the ReLU does not clip in this step.")

a(T_RNN, "advanced", 3, "single_choice",
  "With w_hy = 0.5 and an output y_t = ReLU(w_hy * h_t), what is y_1 when h_1 = 4?",
  {"A": "0.5",
   "B": "2",
   "C": "4",
   "D": "8"},
  ["B"], "y_1 = ReLU(0.5 * 4) = 2.")

a(T_RNN, "advanced", 4, "single_choice",
  "In a recurrent cell with only ReLU non-linearities, all inputs positive and all weights positive, what goes wrong for long sequences, and how does a standard Elman cell differ?",
  {"A": "Vanishing gradients; the standard cell is worse because tanh saturates",
   "B": "Exploding gradients; a standard Elman cell passes the state through tanh, which bounds it and instead risks vanishing gradients",
   "C": "The hidden state becomes constant; the standard cell has the same issue",
   "D": "Nothing goes wrong; ReLU cells are preferred for long sequences"},
  ["B"], "With no bounded non-linearity, repeated multiplication by weights greater than one makes the state and its gradient grow without limit.")

a(T_RNN, "intermediate", 2, "single_choice",
  "How would you fix a recurrent cell that suffers from exploding activations because all weights and inputs are positive?",
  {"A": "Increase the learning rate",
   "B": "Use a bounded activation such as tanh or sigmoid, or initialise with a zero-centred distribution",
   "C": "Remove the recurrent connection",
   "D": "Train for fewer iterations"},
  ["B"], "Either bound the signal so it cannot grow, or make positive and negative contributions cancel on average.")


a(T_RNN, "intermediate", 2, "single_choice",
  "Why are recurrent neural networks suitable for time-series problems?",
  {"A": "Because they process the whole sequence in parallel",
   "B": "Because the hidden state carries information from earlier time steps, capturing temporal correlation",
   "C": "Because they need fewer parameters than fully connected networks",
   "D": "Because they are translation invariant"},
  ["B"], "Neighbouring samples in a time series are correlated, and the recurrence is exactly the mechanism that lets earlier samples influence later predictions.")

a(T_RNN, "intermediate", 2, "single_choice",
  "What is the main benefit of an LSTM compared to an Elman cell?",
  {"A": "It has fewer parameters",
   "B": "Its gated cell state preserves gradients over long sequences, mitigating the vanishing gradient problem",
   "C": "It does not require backpropagation through time",
   "D": "It can process variable-length sequences, which the Elman cell cannot"},
  ["B"], "The additive cell state gives gradients a route through time that is not repeatedly squashed by a saturating non-linearity.")

# ---------------- Unsupervised ---------------------------------------------


a(T_UNS, "intermediate", 2, "single_choice",
  "An architecture that maps an input to a compressed representation and reconstructs it is used for self-representation learning. What is it called?",
  {"A": "A generative adversarial network",
   "B": "An autoencoder",
   "C": "A U-Net",
   "D": "A residual network"},
  ["B"], "Training targets the input itself, which makes it unsupervised, and the bottleneck forces a compact representation.")

a(T_UNS, "advanced", 3, "single_choice",
  "How does a conditional GAN let a user request a specific kind of generated image?",
  {"A": "By retraining the generator for each request",
   "B": "By giving both generator and discriminator an additional input that encodes the target class",
   "C": "By filtering the generated samples after training",
   "D": "By using a larger noise vector"},
  ["B"], "The training set must then contain labelled examples of each target category so the discriminator can learn the conditional distribution.")


# ---------------- Visualization ---------------------------------------------

a(T_VIS, "intermediate", 2, "single_choice",
  "Kernel weights are hard to interpret. What do you visualise instead to understand a convolutional layer?",
  {"A": "The gradients of the loss",
   "B": "The feature maps, i.e. the activations the layer produces for a given input",
   "C": "The bias values",
   "D": "The learning rate schedule"},
  ["B"], "Activations show what the layer actually responds to for a concrete image, which is far more interpretable than the raw filter coefficients.")


# ---------------- Segmentation and detection --------------------------------

a(T_SEG, "intermediate", 2, "single_choice",
  "Name a measure that can evaluate segmentation but not plain classification.",
  {"A": "Accuracy",
   "B": "Intersection over Union",
   "C": "Precision",
   "D": "Cross-entropy loss"},
  ["B"], "IoU and the Dice coefficient compare predicted and true regions, which only makes sense when the prediction has spatial extent.")

a(T_SEG, "intermediate", 2, "single_choice",
  "Which statement about semantic segmentation is CORRECT?",
  {"A": "It can differentiate between different classes in an image, assigning a class label per pixel",
   "B": "It draws a bounding box around the object of interest",
   "C": "It treats multiple objects of the same class as separate entities",
   "D": "It can only find one object per image"},
  ["A"], "Distinguishing separate objects of the same class is instance segmentation; bounding boxes are object detection.")

a(T_SEG, "advanced", 3, "single_choice",
  "Can a pixel-wise segmentation be converted into a bounding box?",
  {"A": "No, the two representations are incompatible",
   "B": "Yes, by taking the extent of the segmented region",
   "C": "Only for convex objects",
   "D": "Only if the segmentation is binary"},
  ["B"], "The conversion loses information and does not work in the other direction, which is why segmentation labels are the richer annotation.")

a(T_SEG, "advanced", 3, "single_choice",
  "You must count the people in a room to check it is below capacity. Which task fits best?",
  {"A": "Semantic segmentation, since it labels every person pixel",
   "B": "Object detection, since it produces one instance per person and instances can be counted",
   "C": "Image classification, since the answer is a single number",
   "D": "Denoising, since the images are noisy"},
  ["B"], "Semantic segmentation merges all people into one class region, so overlapping people cannot be told apart to be counted.")

a(T_SEG, "advanced", 3, "single_choice",
  "A U-Net-like model is missing one key concept compared to the real U-Net. Which one?",
  {"A": "Batch normalization",
   "B": "Skip connections from the encoder to the decoder",
   "C": "Dropout in the bottleneck",
   "D": "A softmax output"},
  ["B"], "Those connections carry high-resolution spatial detail that the downsampling path would otherwise discard.")

a(T_SEG, "advanced", 3, "multiple_choice",
  "Why is classifying each pixel independently with fully connected layers a poor approach to segmentation? (Select all that apply)",
  {"A": "Fully connected layers are not translation invariant, so an object at a new location is harder to segment",
   "B": "The number of parameters is far larger than for a convolutional network",
   "C": "Fully connected layers cannot produce more than two output classes",
   "D": "The approach discards the spatial context around each pixel"},
  ["A", "B", "D"], "The class count is not the issue; the problems are the loss of weight sharing, the parameter explosion and the missing spatial context.")

# ---------------- Reinforcement learning ------------------------------------



# ---------------- Common practices ------------------------------------------

a(T_CP, "intermediate", 2, "single_choice",
  "In which scenario would you use under- or oversampling?",
  {"A": "To counter class imbalance during training",
   "B": "To evaluate a segmentation task",
   "C": "Inside the dropout layer to boost the influence of certain weights",
   "D": "To create artificial data with variational autoencoders"},
  ["A"], "Undersampling removes majority samples and oversampling repeats minority samples so the classes contribute more equally to the loss.")


a(T_CP, "intermediate", 2, "single_choice",
  "How should the FINAL performance of a fine-tuned network be evaluated?",
  {"A": "Accuracy on the validation set",
   "B": "A metric such as an ROC curve computed on the held-out test set",
   "C": "Mean precision over training, validation and test data combined",
   "D": "Recall on the training set"},
  ["B"], "The validation set guided model selection, so it is no longer unbiased; only untouched test data gives an honest estimate.")


a(T_CP, "advanced", 3, "single_choice",
  "A network trained on 32x32 images ends with flatten and fully connected layers. How do you adapt it to accept arbitrarily sized images and still output a vector of length 10?",
  {"A": "Resize every input to 32x32",
   "B": "Replace the flatten and fully connected layers with convolutional layers and average pooling",
   "C": "Add a recurrent layer at the end",
   "D": "Retrain the whole network from scratch"},
  ["B"], "Convolutions have no fixed input size, and global average pooling collapses whatever spatial extent remains into a fixed-length vector.")
