"""Questions adapted from past DL exams (SS21, WS20/21, WS21/22, SS22 + mock).
Each tests a concept whose answer is verified against the official solutions.
Tuple: (topic, difficulty, points, type, question, options, correct, explanation)
"""

E = []
def a(topic, diff, pts, qtype, q, opts, corr, expl):
    E.append({"topic": topic, "difficulty": diff, "points": pts, "type": qtype,
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

# ---------------- Common Practices / data handling -------------------------
a(T_CP, "basics", 1, "single_choice",
  "Which of the following is NOT a common technique to tackle class imbalance?",
  {"A": "Weighting the loss with the inverse class frequency", "B": "Data augmentation",
   "C": "Oversampling the minority class", "D": "Batch normalization"},
  ["D"], "Batch normalization normalizes activations; it does nothing about imbalanced label distributions.")

a(T_CP, "basics", 1, "single_choice",
  "What is ensembling?",
  {"A": "Occluding different areas of the input image for visualization",
   "B": "A network with multiple output heads for different tasks",
   "C": "Multiple networks trained on the same task whose predictions are combined, e.g. by majority vote",
   "D": "Parallel paths with different kernel sizes inside one network"},
  ["C"], "An ensemble combines several independently trained models to reduce variance.")

a(T_CP, "advanced", 3, "single_choice",
  "You build a food-image classifier. Which of these dataset situations is NOT a confound?",
  {"A": "Photos were taken with two different cameras, assigned randomly regardless of label",
   "B": "Car images were shot in daylight while pedestrian images were shot in rain",
   "C": "All T-shirt photos show women while all hoodie photos show men",
   "D": "Spanish audio was recorded with a different microphone than Italian audio"},
  ["A"], "A nuisance factor is only a confound when it correlates with the label; random camera assignment does not.")

a(T_CP, "intermediate", 2, "single_choice",
  "You have a model pre-trained on a similar task. What is the standard way to reuse it for your new classification task?",
  {"A": "Freeze the feature-extraction layers and retrain the classification layers at the end",
   "B": "Retrain only the input layer",
   "C": "Retrain the feature extractor and keep the original classifier",
   "D": "Pick random layers to form a new model"},
  ["A"], "Transfer learning typically keeps learned features and retrains the task-specific head.")

a(T_CP, "basics", 1, "single_choice",
  "A dataset contains 80% dog images and 20% cat images. A model reaches 80% accuracy. Why is this not impressive?",
  {"A": "Accuracy cannot be computed on imbalanced data",
   "B": "A model that always predicts 'dog' already achieves 80%",
   "C": "80% is below the theoretical minimum",
   "D": "The classes must first be normalized"},
  ["B"], "With imbalance, the majority-class baseline sets the bar; 80% equals always predicting dog.")

a(T_CP, "intermediate", 2, "single_choice",
  "A mask/no-mask classifier reaches 98.1% accuracy, but the test data contains 981 'mask' and 19 'no mask' samples. What is the main doubt?",
  {"A": "The learning rate was too high",
   "B": "The classes are highly imbalanced, so accuracy is misleading",
   "C": "98.1% is impossible",
   "D": "The confusion matrix must be symmetric"},
  ["B"], "With 98% majority class, near-98% accuracy can be achieved while failing the minority class; use balancing or loss weighting.")

a(T_CP, "intermediate", 2, "single_choice",
  "Which is a suitable way to evaluate the FINAL performance of a fine-tuned network?",
  {"A": "Accuracy on the training set",
   "B": "Receiver operating characteristics curve on the test set",
   "C": "Recall on the training set",
   "D": "Mean precision on a mix of training, validation and test data"},
  ["B"], "Final evaluation must use held-out test data; training-set metrics measure fit, not generalization.")

a(T_CP, "intermediate", 2, "single_choice",
  "You annotate every piece of trash with a bounding box, but the task is only to classify 'contains trash: yes/no'. Is this weakly supervised learning?",
  {"A": "Yes, because bounding boxes are weak labels",
   "B": "No — the labels carry MORE information than the task requires",
   "C": "Yes, because the task is binary",
   "D": "No, because trash detection is unsupervised"},
  ["B"], "Weak supervision means labels carry less information than the task needs; here it is the opposite.")

a(T_CP, "basics", 1, "single_choice",
  "What is the name of the method that re-uses pre-trained weights for a related task?",
  {"A": "Transfer learning", "B": "Curriculum learning", "C": "Self-distillation", "D": "Bagging"},
  ["A"], "Reusing weights trained on one task as initialization for another is transfer learning.")

a(T_CP, "basics", 1, "single_choice",
  "Which statement about input data normalization is true?",
  {"A": "It is unnecessary because networks adapt during training",
   "B": "It should be computed per sample independently",
   "C": "Test data should be normalized with statistics computed on the test set",
   "D": "A common strategy is normalizing the data to zero mean and unit variance"},
  ["D"], "Standardization uses training-set statistics and is applied identically to validation/test data.")

a(T_CP, "intermediate", 3, "multiple_choice",
  "Which of the following help to reduce overfitting? (Select all that apply)",
  {"A": "Data augmentation", "B": "Dropout layers",
   "C": "Switching from SGD to full-batch gradient descent", "D": "Training for more epochs"},
  ["A", "B"], "Augmentation and dropout regularize; batch mode and longer training do not reduce overfitting.")

# ---------------- Neural Networks ------------------------------------------
a(T_NN, "basics", 1, "single_choice",
  "Why does initialization matter for optimizing deep networks?",
  {"A": "Because the optimization problem is generally non-convex",
   "B": "Because the problem is convex",
   "C": "To reduce the number of parameters",
   "D": "So training always reaches the same minimum"},
  ["A"], "In a non-convex landscape, the starting point influences which minimum is reached and how fast.")

a(T_NN, "intermediate", 2, "single_choice",
  "Which statement about weight/bias initialization is TRUE?",
  {"A": "If the bias is 0, its gradient is always 0 too",
   "B": "Initializing the bias with 0 fixes the dying ReLU problem",
   "C": "It is important to calibrate the variance of the weights",
   "D": "Initialization matters because the problem is convex"},
  ["C"], "Schemes like Xavier/He scale the weight variance to the fan-in so activations neither vanish nor explode.")

a(T_NN, "intermediate", 2, "single_choice",
  "Which statement about initialization is FALSE?",
  {"A": "Initialization is important because deep learning problems are convex",
   "B": "A small positive bias can help against dying ReLUs",
   "C": "With all-zero weights, the gradient w.r.t. the weights is zero",
   "D": "Xavier initialization takes the number of input features into account"},
  ["A"], "The problems are non-convex; that is exactly why initialization matters.")

a(T_NN, "basics", 1, "single_choice",
  "What is the correct order to train a network with backpropagation and SGD? (D: init weights, C: forward pass, A: compute error, E: update weights, B: iterate)",
  {"A": "D → B → C → A → E", "B": "D → C → A → E → B",
   "C": "D → A → C → E → B", "D": "D → E → A → B → C"},
  ["B"], "Initialize, forward, measure error, update, and repeat until converged.")

a(T_NN, "intermediate", 2, "single_choice",
  "All weights AND biases are initialized to zero. Hidden activations are ReLU, the final activation is a sigmoid. For input x=(1,1,1,1), the output is:",
  {"A": "0", "B": "1", "C": "0.5", "D": "-1"},
  ["C"], "Every pre-activation is 0, ReLU(0)=0, and the final sigmoid(0)=0.5.")

a(T_NN, "basics", 1, "single_choice",
  "An unknown final activation produced the output -0.0001. Which function could it be?",
  {"A": "ReLU", "B": "Sigmoid", "C": "Softmax", "D": "Leaky ReLU"},
  ["D"], "ReLU, sigmoid and softmax never output negative values; leaky ReLU (and tanh) can.")

a(T_NN, "basics", 1, "single_choice",
  "Which function does NOT fulfill the requirements for a useful activation function in deep learning?",
  {"A": "tanh(x)", "B": "2x", "C": "max(x, 0)", "D": "1/(1+e^-x)"},
  ["B"], "2x is linear, so stacking layers with it collapses to a single linear map.")

a(T_NN, "basics", 1, "single_choice",
  "Why is the signum function not used as an activation in deep learning?",
  {"A": "It does not introduce a non-linearity",
   "B": "Its derivative is either 0 or undefined for all inputs",
   "C": "It cannot output negative values",
   "D": "It is too expensive to compute"},
  ["B"], "With zero/undefined derivative everywhere, no gradient can flow, so gradient-based training fails.")

a(T_NN, "basics", 1, "single_choice",
  "Which function models the all-or-nothing response of biological neurons?",
  {"A": "The threshold (step) function", "B": "The identity", "C": "The exponential", "D": "The logarithm"},
  ["A"], "A threshold unit fires fully once the input exceeds a level and stays silent otherwise.")

a(T_NN, "basics", 1, "single_choice",
  "Can the XOR problem be solved by a single-layer perceptron?",
  {"A": "Yes", "B": "No — at least one hidden layer is needed",
   "C": "No — at least two hidden layers are needed", "D": "Only with support vector machines"},
  ["B"], "XOR is not linearly separable; one hidden layer with a non-linearity suffices.")

a(T_NN, "advanced", 3, "single_choice",
  "Two fully connected layers with NO activation in between (ŷ = σ(W₂(W₁x + b₁) + b₂)) are equivalent to a single layer ŷ = σ(W̃x + b̃) with:",
  {"A": "W̃ = W₁W₂, b̃ = b₁ + b₂", "B": "W̃ = W₂W₁, b̃ = W₂b₁ + b₂",
   "C": "W̃ = W₂ + W₁, b̃ = W₂b₁", "D": "No such equivalence exists"},
  ["B"], "Multiplying out gives W₂W₁x + W₂b₁ + b₂ — without non-linearities depth adds nothing.")

a(T_NN, "intermediate", 2, "single_choice",
  "Your model gives very different predictions across training runs, yet the average performance is high. The model has:",
  {"A": "High bias, high variance", "B": "Low bias, high variance",
   "C": "High bias, low variance", "D": "Low bias, low variance"},
  ["B"], "Run-to-run spread is variance; good average performance indicates low bias.")

a(T_NN, "basics", 1, "single_choice",
  "What is the purpose of the backpropagation algorithm?",
  {"A": "It computes the forward pass",
   "B": "It computes all gradients required for optimizing the network",
   "C": "It initializes the network",
   "D": "It updates the weights directly"},
  ["B"], "Backprop applies the chain rule to obtain gradients; the optimizer then performs the update.")

a(T_NN, "intermediate", 3, "single_choice",
  "A friend proposes the activation f(x)=0 for x<-0.5, x on [-0.5,0.5], 1 for x>0.5 and claims SGD trains well with it. What is the problem?",
  {"A": "It is not continuous", "B": "The gradient vanishes almost everywhere outside [-0.5, 0.5]",
   "C": "It cannot be evaluated on GPUs", "D": "It outputs values above 1"},
  ["B"], "Outside the linear part the derivative is exactly zero, so saturated units get no learning signal.")

a(T_NN, "basics", 1, "single_choice",
  "A network block computes ŷ = σ₂(x + w₂·σ₁(b₁ + w₁x)). Which architecture does this resemble?",
  {"A": "LeNet", "B": "A ResNet block", "C": "An LSTM cell", "D": "VGG"},
  ["B"], "The '+ x' is a skip (identity) connection around the transformation — the ResNet idea.")

# ---------------- Loss and Optimization ------------------------------------
a(T_LO, "basics", 1, "single_choice",
  "For a binary classifier whose single output should lie between 0 and 1, which final activation is appropriate?",
  {"A": "Softmax", "B": "Sigmoid", "C": "ReLU", "D": "Tanh"},
  ["B"], "A scalar probability needs the sigmoid; softmax on one scalar always outputs 1.")

a(T_LO, "basics", 1, "single_choice",
  "Which loss matches binary classification with a sigmoid output f(x) and label y ∈ {0,1}?",
  {"A": "L = -y ln f(x) - (1-y) ln(1 - f(x))", "B": "L = (f(x) - y)⁴",
   "C": "L = |f(x)| + |y|", "D": "L = max(0, f(x) - y)"},
  ["A"], "This is binary cross-entropy, the maximum-likelihood loss under a Bernoulli model.")

a(T_LO, "basics", 1, "single_choice",
  "A confusion matrix shows 980 true positives, 18 false positives, 1 false negative, 1 true negative (1000 samples). The accuracy is:",
  {"A": "98.1%", "B": "99.9%", "C": "50%", "D": "89.0%"},
  ["A"], "(980+1)/1000 = 98.1% — and it hides the near-total failure on the negative class.")

a(T_LO, "intermediate", 2, "single_choice",
  "Bad design or fine? A binary classifier ends with ReLU, then a sigmoid, and everything with sigmoid ≥ 0.5 is 'positive'.",
  {"A": "Fine — probabilities are guaranteed",
   "B": "Bad — ReLU output is ≥ 0, so the sigmoid is always ≥ 0.5 and everything is classified positive",
   "C": "Bad — sigmoid cannot follow ReLU technically",
   "D": "Fine — the threshold adapts during training"},
  ["B"], "sigmoid(z) ≥ 0.5 for all z ≥ 0; after ReLU there are no negative inputs left.")

a(T_LO, "intermediate", 2, "single_choice",
  "Training loss curves for the same task: which noise ordering is expected?",
  {"A": "SGD noisiest, mini-batch in between, full-batch smoothest",
   "B": "Full-batch noisiest, SGD smoothest",
   "C": "All three look identical",
   "D": "Mini-batch is always noisiest"},
  ["A"], "Smaller batches give noisier gradient estimates; the full batch gives the smoothest curve.")

a(T_LO, "intermediate", 2, "single_choice",
  "You train with FULL-batch gradient descent and the data is not shuffled. Does shuffling help?",
  {"A": "Yes, it changes every update",
   "B": "No — each update uses the whole training set, so the order within it is irrelevant",
   "C": "Yes, but only for images",
   "D": "No, shuffling is never useful in deep learning"},
  ["B"], "Order matters for stochastic/mini-batch updates, not when the full set is averaged per step.")

a(T_LO, "intermediate", 3, "single_choice",
  "A conditional GAN is trained with mini-batches where ALL dog images come first, then all cat images. A colleague says you must shuffle. Right?",
  {"A": "No, GANs are order-invariant",
   "B": "Yes — with sorted data the loss (and the generator's output) shifts drastically between class blocks, making optimization much harder",
   "C": "No, shuffling only matters for full-batch training",
   "D": "Yes, but only because of batch normalization"},
  ["B"], "Mini-batch updates follow the current batch distribution; class-sorted streams cause drift and instability.")

a(T_LO, "basics", 1, "single_choice",
  "What is the purpose of momentum in optimizers?",
  {"A": "It manipulates the learning rate to avoid exploding gradients",
   "B": "It stabilizes training by keeping a moving average over previous gradients",
   "C": "It averages samples inside a batch",
   "D": "It measures training stability"},
  ["B"], "Momentum accumulates past gradient directions, accelerating consistent directions and damping oscillation.")

a(T_LO, "advanced", 3, "single_choice",
  "What distinguishes Nesterov Accelerated Gradient (NAG) from classical momentum?",
  {"A": "It uses no learning rate",
   "B": "It evaluates the gradient at a look-ahead position (after the momentum step) instead of the current weights",
   "C": "It only works with full-batch training",
   "D": "It removes the momentum term entirely"},
  ["B"], "NAG 'peeks ahead' along the velocity before computing the gradient, giving a correction effect.")

a(T_LO, "advanced", 3, "single_choice",
  "For an already-trained network f and an image x with label y=0, an adversarial example is created by optimizing:",
  {"A": "The weights of f to minimize ||f(x)||²",
   "B": "The input x itself, e.g. minimizing L = ||f(x) - y||² = ||f(x)||² w.r.t. x",
   "C": "The learning rate", "D": "A new dataset"},
  ["B"], "Adversarial attacks hold the weights fixed and take gradient steps on the input.")

a(T_LO, "basics", 1, "single_choice",
  "Minimizing binary cross-entropy corresponds to maximum-likelihood estimation under which distribution?",
  {"A": "Gaussian", "B": "Bernoulli", "C": "Poisson", "D": "Uniform"},
  ["B"], "Two mutually exclusive outcomes with probability p and 1-p follow a Bernoulli distribution.")

a(T_LO, "basics", 1, "single_choice",
  "Which final activation should be used for a multi-class problem with one-hot-encoded, mutually exclusive labels?",
  {"A": "Softmax", "B": "Sigmoid", "C": "ReLU", "D": "LeakyReLU"},
  ["A"], "Softmax produces a probability distribution over the classes that sums to 1.")

a(T_LO, "intermediate", 2, "single_choice",
  "The same model must predict 'contains horse' AND 'contains dog' (both can be true). Which output activation is suitable?",
  {"A": "Softmax over the two outputs",
   "B": "One sigmoid per output, since the labels are not mutually exclusive",
   "C": "ReLU", "D": "Argmax"},
  ["B"], "Multi-label problems need independent per-class probabilities; softmax would force competition.")

a(T_LO, "intermediate", 2, "single_choice",
  "Predictions with threshold 0.5 — image a: p(Horse)=0.8 (true: yes), b: p=0.4 (true: yes), c: p=0.7 (true: yes). The accuracy for class 'Horse' is:",
  {"A": "1/3", "B": "2/3", "C": "1", "D": "0"},
  ["B"], "Predictions yes/no/yes vs truth yes/yes/yes → two of three correct.")

a(T_LO, "basics", 1, "single_choice",
  "Which statement about the softmax as final layer is FALSE?",
  {"A": "It assigns a probability to each class",
   "B": "The outputs for one sample depend on each other",
   "C": "It cannot be used during testing",
   "D": "It produces one vector per sample for multi-class problems"},
  ["C"], "Softmax is used at test time as well; only the loss computation is dropped.")

# ---------------- Activation Functions and CNN ------------------------------
a(T_CNN, "intermediate", 2, "single_choice",
  "Which statement about implementing a convolutional layer is FALSE?",
  {"A": "The number of kernels determines the number of output channels",
   "B": "A stride larger than one reduces the spatial size",
   "C": "A 'valid' convolution outputs an image of the same size as its input",
   "D": "The number of kernel weights is independent of the image size"},
  ["C"], "'Valid' mode shrinks the output by kernel_size-1; 'same' padding keeps the size.")

a(T_CNN, "intermediate", 2, "multiple_choice",
  "Which statements about a convolutional layer are TRUE? (Select all that apply)",
  {"A": "The total number of weights depends on the number of input channels",
   "B": "The total number of weights depends on the stride",
   "C": "It computes rotation-invariant features",
   "D": "It can process inputs of arbitrary spatial size"},
  ["A", "D"], "Kernel weights scale with input channels; stride only affects the output size. Convolutions are translation-equivariant, not rotation-invariant.")

a(T_CNN, "basics", 1, "multiple_choice",
  "Which properties do convolutional networks exploit compared to fully connected ones? (Select all that apply)",
  {"A": "Shared weights", "B": "Local connectivity",
   "C": "Full connectivity between all pixels", "D": "The grid-like structure of images"},
  ["A", "B", "D"], "Convolutions reuse a small local kernel across positions, matching image structure.")

a(T_CNN, "basics", 1, "single_choice",
  "For a 2-D convolution with odd kernel width k and stride 1, 'same' output size requires padding per side of:",
  {"A": "k", "B": "(k-1)/2", "C": "k/2 + 1", "D": "2k"},
  ["B"], "Half the kernel overhang on each side: n_p = (k-1)/2 for odd k.")

a(T_CNN, "advanced", 3, "single_choice",
  "A stride-s convolution is implemented as a stride-1 convolution followed by subsampling. What must the backward pass do?",
  {"A": "Nothing special",
   "B": "Pad the incoming error tensor with zeros at the rows/columns that were discarded in the forward pass",
   "C": "Average the error tensor over the stride window",
   "D": "Transpose the kernels"},
  ["B"], "Discarded positions received no output, so their gradient contribution is zero — insert zeros there.")

a(T_CNN, "intermediate", 2, "single_choice",
  "In max pooling, how is the gradient routed in the backward pass?",
  {"A": "Evenly to all positions of the window",
   "B": "Entirely to the position that held the maximum in the forward pass",
   "C": "To the smallest element",
   "D": "It is discarded"},
  ["B"], "Only the argmax influenced the output, so it receives the full gradient; the rest get zero.")

a(T_CNN, "intermediate", 3, "single_choice",
  "A (10,10,3) image: option 1 flattens it and uses a fully connected layer with 5 outputs; option 2 uses a conv layer with five 10×10 kernels in 'valid' mode. Which is true?",
  {"A": "Option 1 has more parameters", "B": "Option 2 has more parameters",
   "C": "Both are mathematically equivalent", "D": "Option 2 cannot produce 5 outputs"},
  ["C"], "A full-size valid kernel per output neuron is exactly a fully connected layer in disguise.")

a(T_CNN, "intermediate", 2, "single_choice",
  "What is the purpose of a 1×1 convolution ('bottleneck layer')?",
  {"A": "It increases the spatial resolution",
   "B": "It computes inner products per position and can reduce the channel dimension, saving parameters and computation",
   "C": "It replaces the activation function",
   "D": "It performs pooling"},
  ["B"], "1×1 convolutions mix channels pointwise — a cheap, learnable dimensionality reduction.")

a(T_CNN, "advanced", 4, "single_choice",
  "A CONV-3-32 layer ('same' padding, stride 1) processes a 32×32×3 input. How many weights does it have (ignoring biases)?",
  {"A": "32·3·3² = 864", "B": "32·32·3 = 3072", "C": "3·3² = 27", "D": "32·3 = 96"},
  ["A"], "Each of the 32 kernels spans 3 input channels with a 3×3 window: 32·3·9.")

a(T_CNN, "basics", 1, "single_choice",
  "What are feature maps in a CNN?",
  {"A": "The kernels themselves", "B": "The activations generated by applying the kernels",
   "C": "The loss values per pixel", "D": "The pooling indices"},
  ["B"], "Each kernel produces one activation map showing where its pattern responds.")

a(T_CNN, "basics", 1, "single_choice",
  "What is the difference between convolution and cross-correlation?",
  {"A": "There is none",
   "B": "Convolution flips the kernel; cross-correlation does not",
   "C": "Cross-correlation only works in 1-D",
   "D": "Convolution requires square kernels"},
  ["B"], "A convolution equals a cross-correlation with a flipped kernel and vice versa — deep learning frameworks typically implement cross-correlation.")

# ---------------- Regularization -------------------------------------------
a(T_REG, "intermediate", 2, "multiple_choice",
  "Which statements about batch normalization are TRUE? (Select all that apply)",
  {"A": "It normalizes the input distribution of the following layer",
   "B": "It normalizes the weights of each layer",
   "C": "It has trainable parameters",
   "D": "It can be skipped during inference"},
  ["A", "C"], "BN standardizes activations and rescales them with learnable γ and β; at test time it runs with stored statistics.")

a(T_REG, "intermediate", 2, "single_choice",
  "Which effect is credited to batch normalization during training?",
  {"A": "It smooths the loss landscape", "B": "It makes the model convex",
   "C": "It eliminates the need for a learning rate", "D": "It removes all overfitting"},
  ["A"], "A smoother optimization landscape allows higher learning rates and faster convergence.")

a(T_REG, "advanced", 3, "single_choice",
  "How does batch normalization behave differently between training and testing?",
  {"A": "It is disabled during testing",
   "B": "Training uses batch statistics and updates a moving average; testing uses the stored (training) statistics",
   "C": "Testing recomputes statistics on the test set",
   "D": "There is no difference"},
  ["B"], "Per-batch statistics would make test predictions depend on the batch — hence frozen moving averages.")

a(T_REG, "intermediate", 2, "single_choice",
  "Comparing weight histograms after training: run 1 shows a sharp peak at exactly 0, run 2 shows a narrower Gaussian than the unregularized run. Which norms were used?",
  {"A": "Run 1: L2, run 2: L1", "B": "Run 1: L1, run 2: L2",
   "C": "Both L1", "D": "Both L2"},
  ["B"], "L1 drives weights exactly to zero (sparsity); L2 shrinks all weights, reducing the variance.")

a(T_REG, "basics", 1, "single_choice",
  "How does the keep probability in dropout relate to the strength of regularization?",
  {"A": "Higher keep probability means stronger regularization",
   "B": "Lower keep probability (dropping more units) means stronger regularization",
   "C": "The keep probability has no influence",
   "D": "Dropout does not regularize"},
  ["B"], "Dropping more units forces more redundancy — keep probability 1.0 disables dropout entirely.")

a(T_REG, "intermediate", 2, "single_choice",
  "Histograms of activations drift away from mean 0 / variance 1 layer by layer although inputs were normalized. Name the problem and a counter-measure.",
  {"A": "Mode collapse — use minibatch discrimination",
   "B": "Internal covariate shift — add batch normalization layers",
   "C": "Vanishing gradients — remove all activations",
   "D": "Overfitting — collect more data"},
  ["B"], "The shifting layer-input distribution is countered by normalizing activations inside the network.")

a(T_REG, "basics", 1, "single_choice",
  "What is the general purpose of regularization?",
  {"A": "To reach zero training loss faster",
   "B": "To trade a bit of training fit for better generalization on unseen data",
   "C": "To increase model capacity",
   "D": "To speed up inference"},
  ["B"], "Regularization counters overfitting — the bias/variance trade-off in action.")

a(T_REG, "intermediate", 2, "multiple_choice",
  "Which statements about adversarial examples are TRUE? (Select all that apply)",
  {"A": "A slightly perturbed input can yield a completely different prediction",
   "B": "They are generated by GANs",
   "C": "They cannot occur in real photographs",
   "D": "They also exist for other ML methods such as SVMs"},
  ["A", "D"], "Adversarial fragility is a general phenomenon of learned decision boundaries, not a GAN artifact.")

# ---------------- RNN --------------------------------------------------------
a(T_RNN, "basics", 1, "single_choice",
  "Which sampling strategy for generating sequences from a trained RNN does NOT exist?",
  {"A": "Greedy sampling", "B": "Beam search", "C": "Recognition sampling", "D": "Random sampling"},
  ["C"], "Greedy, beam and random sampling are standard; 'recognition sampling' is made up.")

a(T_RNN, "basics", 1, "single_choice",
  "What role does the hidden state play in an Elman RNN?",
  {"A": "It stores the weights",
   "B": "It carries time-dependent context — a short-term memory connecting time steps",
   "C": "It holds the loss value",
   "D": "It is only used during testing"},
  ["B"], "The hidden state is what makes the network recurrent: information flows from step to step.")

a(T_RNN, "basics", 1, "single_choice",
  "What advantage does an LSTM have over a simple RNN?",
  {"A": "Fewer parameters",
   "B": "A cell state that serves as long-term memory, making long dependencies easier to learn",
   "C": "It needs no training",
   "D": "It processes images faster"},
  ["B"], "The gated cell state provides an almost unimpeded gradient path across many time steps.")

a(T_RNN, "advanced", 3, "single_choice",
  "During TBPTT, why is it incorrect to update the hidden-gate weights WHILE iterating backwards through the time series?",
  {"A": "The optimizer would diverge",
   "B": "The cell shares its weights across all time steps — changing them mid-backward changes the function being differentiated, so the gradients no longer match",
   "C": "Weights may only be updated once per epoch",
   "D": "The learning rate would need rescaling"},
  ["B"], "The remedy is to accumulate the gradients over time and apply one update after the backward pass.")

a(T_RNN, "advanced", 3, "single_choice",
  "Truncated backpropagation through time (TBPTT) addresses which problem, and how?",
  {"A": "Overfitting — by dropping time steps randomly",
   "B": "The high cost of a full-sequence update — by splitting long sequences into smaller, overlapping chunks",
   "C": "Exploding gradients — by clipping",
   "D": "Class imbalance — by resampling"},
  ["B"], "Updating only after a full long sequence is expensive; TBPTT updates on overlapping sub-sequences.")

a(T_RNN, "intermediate", 2, "multiple_choice",
  "Which problems are associated with the simple Elman cell? (Select all that apply)",
  {"A": "Small weights multiplied over many steps can cause vanishing gradients",
   "B": "Long-term memory loss",
   "C": "Many-to-many mappings are impossible",
   "D": "Skip connections cause memory loss"},
  ["A", "B"], "Repeated multiplication with the same weights shrinks (or explodes) gradients, and old context fades.")

a(T_RNN, "advanced", 4, "single_choice",
  "In a recurrent cell without a bounded non-linearity, all inputs xₜ > 0 and weights w_hh, w_xh > 0. For long sequences one risks:",
  {"A": "Vanishing outputs", "B": "Exploding gradients — a tanh in a standard Elman cell would bound the state to (-1,1)",
   "C": "Nothing, the setup is safe", "D": "Underflow of the loss"},
  ["B"], "Positive weights repeatedly multiplied grow without bound; the tanh in standard cells limits the state.")

a(T_RNN, "intermediate", 2, "single_choice",
  "A binary-cross-entropy loss is attached directly to a recurrent cell whose output is not bounded. What problem occurs?",
  {"A": "The logarithm cannot handle values outside [0,1] — a sigmoid must squash the outputs first",
   "B": "BCE only works for images",
   "C": "The cell forgets its state",
   "D": "Nothing"},
  ["A"], "ln(ŷ) requires ŷ in (0,1); without a sigmoid the loss is undefined for out-of-range outputs.")

a(T_RNN, "basics", 1, "single_choice",
  "Which application is a natural fit for a recurrent neural network?",
  {"A": "Classifying single, independent images",
   "B": "Analyzing ECG signals, where neighboring samples are correlated in time",
   "C": "Sorting a list of numbers",
   "D": "Computing image histograms"},
  ["B"], "RNNs shine when successive samples carry temporal dependencies (ECG, weather, language).")

# ---------------- Unsupervised ----------------------------------------------
a(T_UNS, "basics", 1, "single_choice",
  "In an encoder-decoder network, which part can be used on its own to create synthetic samples?",
  {"A": "The encoder of a VAE", "B": "The decoder of a VAE",
   "C": "The discriminator of a GAN", "D": "The pooling layers"},
  ["B"], "Sampling the latent distribution and decoding generates new data; the VAE decoder is the generator.")

a(T_UNS, "basics", 1, "single_choice",
  "In an autoencoder figure, the part that maps the input to the bottleneck and the part that reconstructs from it are called:",
  {"A": "Generator and discriminator", "B": "Encoder and decoder",
   "C": "Actor and critic", "D": "Teacher and student"},
  ["B"], "Encoder compresses, decoder reconstructs — the bottleneck in between is the code.")

a(T_UNS, "intermediate", 2, "single_choice",
  "What is the main difference between U-Nets and plain autoencoders?",
  {"A": "U-Nets have no decoder",
   "B": "U-Nets add skip connections from encoder to decoder levels",
   "C": "Autoencoders cannot use convolutions",
   "D": "U-Nets require labels for reconstruction"},
  ["B"], "The skips carry high-resolution detail past the bottleneck — crucial for segmentation.")

a(T_UNS, "intermediate", 3, "single_choice",
  "How is a DENOISING autoencoder trained?",
  {"A": "On labels from a human annotator",
   "B": "The input is corrupted with a noise model (e.g. Gaussian) and the network learns to reconstruct the original",
   "C": "By maximizing the noise",
   "D": "With a discriminator"},
  ["B"], "Reconstructing clean data from corrupted input forces robust representations — and enables in-painting.")

a(T_UNS, "intermediate", 3, "single_choice",
  "What distinguishes a VARIATIONAL autoencoder from a standard one?",
  {"A": "It has no bottleneck",
   "B": "It compresses inputs into a constrained latent DISTRIBUTION (e.g. Gaussian) instead of a free latent vector",
   "C": "It uses no decoder",
   "D": "It requires labeled data"},
  ["B"], "The latent space is regularized toward a known distribution, so sampling from it yields valid new data.")

a(T_UNS, "intermediate", 2, "single_choice",
  "A linear autoencoder (no non-linearities) trained with L2 loss learns a generalization of:",
  {"A": "K-means", "B": "PCA", "C": "A decision tree", "D": "Softmax regression"},
  ["B"], "Without non-linearities the optimal bottleneck spans the principal subspace of the data.")

a(T_UNS, "intermediate", 2, "single_choice",
  "How is a GAN trained?",
  {"A": "Generator and discriminator minimize the same loss together",
   "B": "A min-max game: the discriminator maximizes classification of real vs. fake, the generator minimizes the discriminator's success",
   "C": "Only the generator is trained",
   "D": "With cross-validation"},
  ["B"], "Generator maps noise to samples; discriminator judges real vs. generated — adversarial objectives.")

a(T_UNS, "intermediate", 2, "single_choice",
  "You want users to pick 'forest', 'lake', 'mountains' etc. and get matching generated images. Which GAN type and training data do you need?",
  {"A": "A vanilla GAN with unlabeled images",
   "B": "A conditional GAN — both networks receive a class encoding, and the training images need environment labels",
   "C": "A discriminator only",
   "D": "A GAN trained on noise alone"},
  ["B"], "Conditioning inputs steer generation; training therefore needs (image, label) pairs.")

a(T_UNS, "intermediate", 2, "single_choice",
  "After 100 GAN epochs the loss values look like at the start. Must you assume nothing was learned?",
  {"A": "Yes, constant loss always means no progress",
   "B": "No — generator and discriminator may both have improved equally well, keeping the losses balanced",
   "C": "Yes, GAN losses must go to zero",
   "D": "No, losses are meaningless in general"},
  ["B"], "In the adversarial game, mutual improvement can leave the equilibrium losses unchanged.")

a(T_UNS, "advanced", 3, "single_choice",
  "Test users complain that all images from your GAN look nearly identical. What happened, and what is a counter-strategy?",
  {"A": "Overfitting — early stopping",
   "B": "Mode collapse — mini-batch discrimination or unrolled GANs",
   "C": "Vanishing gradients — ReLU",
   "D": "Data leakage — new test split"},
  ["B"], "The generator found one output family that fools the discriminator; diversity penalties counteract it.")

# ---------------- Architectures ---------------------------------------------
a(T_ARCH, "basics", 1, "multiple_choice",
  "Which architectures contain BOTH convolutional layers and skip connections? (Select all that apply)",
  {"A": "U-Net", "B": "LeNet", "C": "VGG16", "D": "ResNet"},
  ["A", "D"], "U-Net skips encoder features to the decoder; ResNet adds identity shortcuts. LeNet/VGG have neither.")

a(T_ARCH, "basics", 1, "multiple_choice",
  "Which features are NOT used in LeNet? (Select all that apply)",
  {"A": "Pooling layers", "B": "Convolutional layers", "C": "ReLU non-linearities", "D": "Skip connections"},
  ["C", "D"], "LeNet used convolutions, subsampling and tanh/sigmoid — ReLU and skips came later.")

a(T_ARCH, "intermediate", 2, "multiple_choice",
  "What are advantages of making a network deeper? (Select all that apply)",
  {"A": "Exponential feature reuse", "B": "Less memory consumption",
   "C": "Increasingly abstract features", "D": "Ability to approximate increasingly complex functions"},
  ["A", "C", "D"], "Depth builds feature hierarchies and expressiveness — at the cost of memory, not in its favor.")

a(T_ARCH, "intermediate", 2, "single_choice",
  "Roughly how does model capacity relate to a network's design?",
  {"A": "It is fixed by the number of training samples",
   "B": "It is linked to the variety of functions the network can approximate and grows with depth/parameters",
   "C": "It is unrelated to architecture",
   "D": "It only depends on the optimizer"},
  ["B"], "Capacity describes the richness of representable functions — closely tied to the bias/variance trade-off.")

a(T_ARCH, "intermediate", 2, "single_choice",
  "A pretrained CNN ends with flatten + fully connected layers and was trained on 32×32 images. To process arbitrarily-sized images while keeping a length-10 output, you should:",
  {"A": "Resize all images to 32×32 forever",
   "B": "Replace flatten + FC with 1×1 (or n×n) convolutions and global average pooling",
   "C": "Remove all convolutions",
   "D": "Add more FC layers"},
  ["B"], "Convolutional heads are size-agnostic; global pooling collapses any spatial extent to a fixed vector.")

# ---------------- Visualization & Attention ---------------------------------
a(T_VIS, "basics", 1, "single_choice",
  "Which of the following is NOT a technique to visualize important image areas of a classifier?",
  {"A": "Saliency maps", "B": "Occlusion", "C": "Guided backpropagation", "D": "Inception"},
  ["D"], "Inception is an architecture module, not a visualization method.")

a(T_VIS, "intermediate", 2, "single_choice",
  "How are saliency maps generated, and what serves as the pseudo loss?",
  {"A": "The accuracy is backpropagated",
   "B": "The classification score of the target class is used as pseudo loss and its gradient w.r.t. the input is visualized",
   "C": "The weights are plotted directly",
   "D": "The input is blurred repeatedly"},
  ["B"], "Backpropagating the class score to the input shows which pixels influence the decision most.")

a(T_VIS, "intermediate", 2, "single_choice",
  "Your saliency maps show the network ignores the face for smile detection. Training it additionally on related tasks (glasses detection, pose) is called:",
  {"A": "Curriculum learning", "B": "Multi-task learning with auxiliary tasks",
   "C": "Bagging", "D": "Distillation"},
  ["B"], "Auxiliary tasks share features and can steer attention toward the relevant regions.")

# ---------------- Deep RL ----------------------------------------------------
a(T_RL, "basics", 1, "single_choice",
  "In reinforcement learning, what is the difference between exploitation and exploration?",
  {"A": "There is none",
   "B": "Exploitation uses the currently known best action; exploration tries potentially suboptimal new actions to find better returns",
   "C": "Exploration is only used during testing",
   "D": "Exploitation samples random actions"},
  ["B"], "Balancing both is essential — pure exploitation gets stuck in locally optimal behavior.")

a(T_RL, "basics", 1, "single_choice",
  "Which statement about reinforcement learning is CORRECT?",
  {"A": "Exploiting one known good action suffices during training",
   "B": "Exploration should be used during training to try out new action sequences",
   "C": "Exploration should be used during testing",
   "D": "Exploitation enforces new action sequences"},
  ["B"], "Training needs exploration (e.g. epsilon-greedy); at test time the learned policy is exploited.")

a(T_RL, "intermediate", 3, "single_choice",
  "Which statement about RL methods is WRONG?",
  {"A": "A good policy aims to maximize the future return",
   "B": "The Bellman equations form a linear system solvable for small problems",
   "C": "Q-learning is an off-policy method that needs no model of the environment dynamics",
   "D": "Temporal-difference learning is an on-policy method that needs information about the environment dynamics"},
  ["D"], "TD learning is model-free — it learns from sampled transitions without knowing the dynamics.")

a(T_RL, "intermediate", 2, "single_choice",
  "In epsilon-greedy action selection, the agent:",
  {"A": "Always takes the greedy action",
   "B": "Takes a random action with probability ε and the currently best-valued action otherwise",
   "C": "Always acts randomly",
   "D": "Follows the reward gradient"},
  ["B"], "ε controls the exploration rate; the rest of the time the highest Q-value action is exploited.")

a(T_RL, "intermediate", 2, "single_choice",
  "Why does a purely greedy policy on immediate rewards fail in grid-world style tasks?",
  {"A": "Because rewards are always negative",
   "B": "It only exploits the next action's reward and cannot look ahead over multiple steps",
   "C": "Greedy policies are not computable",
   "D": "It explores too much"},
  ["B"], "Maximizing one-step reward ignores state transitions and long-term return.")

a(T_RL, "basics", 1, "single_choice",
  "In the RL interaction loop, the agent sends ___ to the environment and receives ___ back.",
  {"A": "states; actions", "B": "actions; the next state and a reward",
   "C": "rewards; losses", "D": "gradients; weights"},
  ["B"], "Agent acts (aₜ); environment answers with state sₜ₊₁ and reward rₜ₊₁.")

# ---------------- Segmentation & Object Detection ----------------------------
a(T_SEG, "basics", 1, "single_choice",
  "What are the two main tasks of object detection?",
  {"A": "Finding bounding boxes and classifying them",
   "B": "Boundary search between objects",
   "C": "Super-resolution of regions of interest",
   "D": "In-painting missing image parts"},
  ["A"], "Detection = where (localization via boxes) + what (class per box).")

a(T_SEG, "intermediate", 2, "single_choice",
  "Which statement about YOLO vs. (Fast) R-CNN is TRUE?",
  {"A": "YOLO produces candidate regions that are passed to a CNN",
   "B": "YOLO combines bounding-box prediction and classification in ONE network",
   "C": "Fast R-CNN is generally faster",
   "D": "Fast R-CNN does real-time detection while YOLO cannot"},
  ["B"], "That single forward pass is why YOLO is called a single-shot detector and runs in real time.")

a(T_SEG, "basics", 1, "single_choice",
  "Why is YOLO called a 'Single-Shot Detector' (SSD)?",
  {"A": "It only detects one object",
   "B": "It combines box prediction and classification in one model and one forward pass",
   "C": "It uses a single pixel",
   "D": "It needs a single training image"},
  ["B"], "No separate proposal stage — everything happens in one pass.")

a(T_SEG, "basics", 1, "multiple_choice",
  "Which statements are TRUE? (Select all that apply)",
  {"A": "The goal of segmentation is drawing bounding boxes",
   "B": "Semantic segmentation can be considered pixel-wise classification",
   "C": "A pixel-wise segmentation of an object can be converted into a bounding box",
   "D": "Instance segmentation can only find one instance per class"},
  ["B", "C"], "Segmentation labels pixels; boxes follow from the mask extent. Instance segmentation separates many instances.")

a(T_SEG, "basics", 1, "single_choice",
  "You must check whether the number of people in a room is below capacity. Semantic segmentation or object detection?",
  {"A": "Semantic segmentation, because it labels every pixel",
   "B": "Object detection, because detecting person instances allows counting them",
   "C": "Neither works",
   "D": "Only classification"},
  ["B"], "Counting needs instances; semantic masks of 'person' pixels merge people together.")

a(T_SEG, "advanced", 3, "single_choice",
  "In segmentation evaluation with pᵢⱼ = pixels of true class i predicted as class j, the metric Σᵢ pᵢᵢ / Σᵢ Σⱼ pᵢⱼ is:",
  {"A": "Mean Intersection over Union", "B": "Pixel Accuracy",
   "C": "Frequency Weighted IoU", "D": "Mean class-wise pixel accuracy"},
  ["B"], "Correct pixels over all pixels — the plain pixel accuracy.")

a(T_SEG, "advanced", 4, "single_choice",
  "With the same notation, the per-class Intersection over Union of class i is:",
  {"A": "pᵢᵢ / (Σⱼ pᵢⱼ + Σⱼ pⱼᵢ − pᵢᵢ)", "B": "pᵢᵢ / Σⱼ pᵢⱼ",
   "C": "Σⱼ pᵢⱼ / pᵢᵢ", "D": "pᵢᵢ · Σⱼ pⱼᵢ"},
  ["A"], "Intersection pᵢᵢ over union = predicted ∪ ground-truth pixels of the class (counting the overlap once).")

a(T_SEG, "intermediate", 2, "multiple_choice",
  "Which metrics are commonly used to evaluate semantic segmentation? (Select all that apply)",
  {"A": "Pixel Accuracy", "B": "Mean Intersection over Union",
   "C": "Frequency Weighted IoU", "D": "Perplexity"},
  ["A", "B", "C"], "Perplexity is a language-model metric; the others are standard for segmentation.")

a(T_SEG, "intermediate", 2, "single_choice",
  "Why are fully connected layers on flattened pixels ill-suited for segmenting street scenes?",
  {"A": "They cannot output more than one value",
   "B": "They are not translation invariant and need vastly more parameters than convolutions",
   "C": "They cannot be trained with SGD",
   "D": "They require grayscale input"},
  ["B"], "Reoccurring objects at different positions need shared, local filters — exactly what convolutions provide.")
