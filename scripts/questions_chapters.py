"""Chapter-wise questions written in the style of the past exam papers.

Replaces the old definitional set ("What does X do?") with the four patterns the
real papers actually use:

  * statement evaluation - "Which of these is/are true?"
  * scenario            - "You train X and see Y. What does that tell you?"
  * design critique     - "Is this a sensible choice?"
  * short calculation

House style, so the bank reads like it was written by a person and not padded
out by a machine:

  * options stay short and roughly the same length as each other, so the longest
    option is not a free giveaway
  * plain words, no stacked subordinate clauses
  * explanations are one sentence, two at most
  * no em dashes, no "it is important to note that"

Everything here is grounded in the lecture notes under lectures/.
"""

K = []


def a(topic, diff, pts, qtype, q, opts, corr, expl):
    K.append({"topic": topic, "difficulty": diff, "points": pts, "type": qtype,
              "question": q, "options": opts, "correct_answers": corr,
              "explanation": expl, "source": "lecture notes"})


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
# Introduction
# =========================================================================

a(T_INTRO, "basics", 1, "single_choice",
  "What does a single neuron compute before its activation is applied?",
  {"A": "A weighted sum of the inputs plus a bias",
   "B": "The distance to the nearest class centre",
   "C": "The variance of the inputs",
   "D": "The product of all inputs"},
  ["A"], "Everything else in a layer is built on this one affine operation.")

a(T_INTRO, "intermediate", 2, "multiple_choice",
  "Which of these separate deep learning from classical machine learning? (Select all that apply)",
  {"A": "Features are learned rather than hand-designed",
   "B": "Representation and classifier are trained together",
   "C": "Much more training data is usually needed",
   "D": "No optimisation is involved"},
  ["A", "B", "C"], "Deep models are still trained by optimisation. What changed is that nobody designs the features by hand.")

a(T_INTRO, "intermediate", 2, "single_choice",
  "You have 200 labelled images and a set of features that already work well. What should you try first?",
  {"A": "A deep network trained from scratch",
   "B": "A classical model on those features",
   "C": "A deeper network with no regularisation",
   "D": "A network trained without validation data"},
  ["B"], "200 samples is far too few to learn a representation. Fine-tuning a pretrained network would be the other sensible option.")

a(T_INTRO, "advanced", 3, "single_choice",
  "Your model scores 99% on training data and 62% on validation data. What is happening?",
  {"A": "It is underfitting",
   "B": "It is overfitting",
   "C": "The learning rate is too small",
   "D": "The validation set is too big"},
  ["B"], "The fix is more data, augmentation or regularisation, not more capacity.")

a(T_INTRO, "advanced", 3, "single_choice",
  "Several training runs give very different predictions, but the average score is good. What does that mean?",
  {"A": "High bias, high variance",
   "B": "Low bias, high variance",
   "C": "High bias, low variance",
   "D": "Low bias, low variance"},
  ["B"], "Good average means the model class fits the problem, so bias is low. Disagreement between runs is variance.")

a(T_INTRO, "basics", 1, "single_choice",
  "What does model capacity refer to?",
  {"A": "The memory the model needs",
   "B": "The range of functions it can fit",
   "C": "The size of the training set",
   "D": "The largest usable batch size"},
  ["B"], "Capacity grows with width and depth and sits at the heart of the bias-variance trade-off.")

a(T_INTRO, "intermediate", 2, "single_choice",
  "Why did the XOR result damage early neural network research?",
  {"A": "It showed networks can never approximate functions",
   "B": "A limit of one linear layer was read as a limit of the whole idea",
   "C": "It proved backpropagation was wrong",
   "D": "It showed convolution was required"},
  ["B"], "One hidden layer solves XOR. The result was correct but got over-generalised.")

a(T_INTRO, "intermediate", 2, "multiple_choice",
  "Which of these enabled the deep learning breakthrough around 2012? (Select all that apply)",
  {"A": "Large labelled datasets",
   "B": "Training on GPUs",
   "C": "Activations that do not saturate",
   "D": "The invention of backpropagation"},
  ["A", "B", "C"], "Backpropagation was decades old by then. Scale and a few training tricks were what changed.")

a(T_INTRO, "basics", 1, "single_choice",
  "What separates supervised from unsupervised learning?",
  {"A": "Only supervised learning uses networks",
   "B": "Supervised learning trains against given labels",
   "C": "Unsupervised learning needs more compute",
   "D": "Unsupervised learning cannot be measured"},
  ["B"], "Unsupervised objectives still exist, they just come from the data rather than from labels.")

a(T_INTRO, "advanced", 3, "single_choice",
  "All your class A photos were shot outdoors and all class B photos indoors. Why is that a problem?",
  {"A": "The images have different sizes",
   "B": "Lighting separates the classes, so the model can learn that instead",
   "C": "Outdoor images cannot be normalised",
   "D": "It is fine if the dataset is large"},
  ["B"], "The model takes whichever shortcut is easiest, and that shortcut breaks as soon as the correlation does.")

a(T_INTRO, "intermediate", 2, "single_choice",
  "A model underfits badly. Which change is most likely to help?",
  {"A": "Add dropout",
   "B": "Increase the model capacity",
   "C": "Shrink the training set",
   "D": "Add more weight decay"},
  ["B"], "Dropout and weight decay both fight overfitting, so they would make underfitting worse.")

a(T_INTRO, "basics", 1, "single_choice",
  "Why is a training, validation and test split used rather than just training and test?",
  {"A": "To make training faster",
   "B": "So tuning decisions do not contaminate the final score",
   "C": "Because test sets are usually mislabelled",
   "D": "To reduce the parameter count"},
  ["B"], "Once you tune on a split, its score is no longer an honest estimate.")

# =========================================================================
# Neural Networks
# =========================================================================

a(T_NN, "basics", 1, "single_choice",
  "What does backpropagation compute?",
  {"A": "The updated weights",
   "B": "Gradients of the loss for every parameter",
   "C": "The forward activations",
   "D": "The best learning rate"},
  ["B"], "Applying those gradients is the optimizer's job, which is why any optimizer can be swapped in.")

a(T_NN, "intermediate", 2, "single_choice",
  "You stack two fully connected layers with nothing between them. What have you built?",
  {"A": "A model with twice the capacity",
   "B": "Something equivalent to one fully connected layer",
   "C": "A model that cannot be trained",
   "D": "A convolutional layer"},
  ["B"], "Two affine maps compose into one. Depth only pays off with a non-linearity in between.")

a(T_NN, "intermediate", 2, "multiple_choice",
  "Which statements about vanishing gradients are true? (Select all that apply)",
  {"A": "Saturating activations make it worse",
   "B": "Early layers learn more slowly than late ones",
   "C": "Long sequences make it more likely",
   "D": "Dropout is the standard cure"},
  ["A", "B", "C"], "Dropout targets overfitting. The cures here are better activations, normalisation and skip connections.")

a(T_NN, "basics", 1, "single_choice",
  "Why does each layer learn a bias as well as weights?",
  {"A": "It keeps activations positive",
   "B": "It lets the boundary miss the origin",
   "C": "It normalises the inputs",
   "D": "It stops weights growing"},
  ["B"], "Without a bias every layer is pinned to the origin, which is a real restriction.")

a(T_NN, "advanced", 3, "single_choice",
  "You set every weight in a layer to the same non-zero value. What happens?",
  {"A": "Training is slower but works",
   "B": "The units stay identical and never differentiate",
   "C": "Gradients explode at once",
   "D": "The biases break the tie"},
  ["B"], "Identical weights give identical gradients, so the whole layer behaves like one unit.")

a(T_NN, "advanced", 4, "single_choice",
  "All weights and biases are zero, hidden units use ReLU and the output uses sigmoid. You feed in x = (1,1,1,1). What comes out?",
  {"A": "0",
   "B": "0.5",
   "C": "1",
   "D": "-1"},
  ["B"], "Every pre-activation is 0, ReLU(0) is 0, and sigmoid(0) is 0.5.")

a(T_NN, "intermediate", 2, "single_choice",
  "A fully connected layer maps 100 inputs to 50 outputs. How many parameters, biases included?",
  {"A": "150",
   "B": "5000",
   "C": "5050",
   "D": "5100"},
  ["C"], "100 x 50 weights plus one bias per output gives 5050.")

a(T_NN, "intermediate", 2, "single_choice",
  "What does the universal approximation theorem actually promise?",
  {"A": "One hidden layer can approximate any continuous function",
   "B": "Gradient descent finds the global optimum",
   "C": "Deeper is always better",
   "D": "Few hidden units are needed"},
  ["A"], "It is an existence result only. It says nothing about how wide the layer must be or whether training will find it.")

a(T_NN, "advanced", 3, "single_choice",
  "Given that one hidden layer is enough in theory, why build deep networks?",
  {"A": "Deep networks have convex losses",
   "B": "Depth reuses features, so fewer units are needed",
   "C": "Deep networks never overfit",
   "D": "Shallow networks cannot use ReLU"},
  ["B"], "The width a shallow network would need is often impractical. Depth expresses the same thing far more compactly.")

a(T_NN, "advanced", 3, "single_choice",
  "You feed a uniform grey image into a trained classifier. Are all class scores equal?",
  {"A": "Yes, the input has no class information",
   "B": "No, each class has different weights",
   "C": "Yes, if the output is a softmax",
   "D": "Only for a batch size of one"},
  ["B"], "Equal scores would need identical weight vectors for every class, which training never produces.")

a(T_NN, "advanced", 3, "single_choice",
  "Your loss turns into NaN partway through training. What is the first thing to suspect?",
  {"A": "The learning rate is too high",
   "B": "The batch size is too small",
   "C": "The validation set is too large",
   "D": "Dropout was left on"},
  ["A"], "Lower the rate, clip the gradients, and check for a log of zero in the loss.")

a(T_NN, "intermediate", 2, "single_choice",
  "Which quantity does a fully connected layer have to keep from its forward pass?",
  {"A": "Its own output",
   "B": "Its input",
   "C": "The learning rate",
   "D": "Nothing at all"},
  ["B"], "The weight gradient is built from the stored input and the incoming error.")

a(T_NN, "intermediate", 2, "multiple_choice",
  "Which statements about model capacity are true? (Select all that apply)",
  {"A": "It reflects the range of functions available",
   "B": "Depth increases it",
   "C": "It ties into the bias-variance trade-off",
   "D": "Raising it always raises bias"},
  ["A", "B", "C"], "More capacity usually lowers bias and raises variance, so the last option has it backwards.")

a(T_NN, "basics", 1, "single_choice",
  "In what order do the forward and backward passes run?",
  {"A": "Forward input to loss, backward loss to input",
   "B": "Both input to loss",
   "C": "Both loss to input",
   "D": "Trainable layers first"},
  ["A"], "Each layer's gradient depends on the one above it, so the backward pass must reverse the order.")

a(T_NN, "advanced", 3, "single_choice",
  "Adding more layers to a plain network makes the training error go up. What does that suggest?",
  {"A": "Overfitting",
   "B": "An optimisation problem, not a generalisation one",
   "C": "The labels are wrong",
   "D": "The batch size is too large"},
  ["B"], "Overfitting would lower the training error. This is the degradation problem that motivated ResNet.")

# =========================================================================
# Loss and Optimization
# =========================================================================

a(T_LO, "basics", 1, "single_choice",
  "How does a gradient descent step change a weight?",
  {"A": "Adds the scaled gradient",
   "B": "Subtracts the scaled gradient",
   "C": "Replaces it with the gradient",
   "D": "Multiplies it by the gradient"},
  ["B"], "The gradient points uphill, so minimising means stepping against it.")

a(T_LO, "intermediate", 2, "single_choice",
  "What does the learning rate control?",
  {"A": "How many samples each update uses",
   "B": "How far each step moves",
   "C": "How many layers get updated",
   "D": "How often validation runs"},
  ["B"], "Too large and it overshoots, too small and training crawls.")

a(T_LO, "intermediate", 2, "multiple_choice",
  "Which statements about SGD versus full-batch gradient descent are true? (Select all that apply)",
  {"A": "SGD gradients are noisier",
   "B": "SGD makes many more updates per epoch",
   "C": "The noise can help escape poor minima",
   "D": "Full-batch descent needs shuffling"},
  ["A", "B", "C"], "Full-batch uses the whole set for each update, so the order it sees the data in makes no difference.")

a(T_LO, "intermediate", 2, "single_choice",
  "Three loss curves are very noisy, mildly noisy and smooth. Which method produced the smooth one?",
  {"A": "Single-sample SGD",
   "B": "Full-batch gradient descent",
   "C": "Mini-batch with batch size 8",
   "D": "Mini-batch with batch size 2"},
  ["B"], "Averaging over more samples lowers the variance of the gradient estimate.")

a(T_LO, "basics", 1, "single_choice",
  "Which loss goes with a softmax output for multi-class problems?",
  {"A": "Mean squared error",
   "B": "Cross entropy",
   "C": "Hinge loss",
   "D": "Mean absolute error"},
  ["B"], "Cross entropy is the negative log-likelihood of the right class under the softmax.")

a(T_LO, "intermediate", 2, "single_choice",
  "Which loss suits a regression task with roughly Gaussian noise?",
  {"A": "Cross entropy",
   "B": "Squared error",
   "C": "Hinge loss",
   "D": "Binary cross entropy"},
  ["B"], "Squared error is the maximum likelihood choice under Gaussian noise.")

a(T_LO, "advanced", 3, "single_choice",
  "Minimising binary cross entropy is maximum likelihood under which distribution?",
  {"A": "Gaussian",
   "B": "Bernoulli",
   "C": "Poisson",
   "D": "Uniform"},
  ["B"], "Each sample is one binary trial, so the likelihood is Bernoulli.")

a(T_LO, "advanced", 3, "single_choice",
  "Your binary classifier ends with ReLU, then sigmoid, and thresholds at 0.5. Is this sensible?",
  {"A": "Yes, the sigmoid bounds the output",
   "B": "No, nothing can score below 0.5",
   "C": "Yes, if you raise the threshold",
   "D": "No, because sigmoid saturates"},
  ["B"], "ReLU output is never negative and sigmoid(0) is 0.5, so every sample comes out positive.")

a(T_LO, "advanced", 3, "single_choice",
  "An unknown final activation produced -0.0001. Which one could it be?",
  {"A": "ReLU",
   "B": "Tanh",
   "C": "Sigmoid",
   "D": "Softmax"},
  ["B"], "The other three cannot produce a negative number. Leaky ReLU would also fit.")

a(T_LO, "intermediate", 2, "single_choice",
  "Why decay the learning rate as training goes on?",
  {"A": "Gradients grow over time",
   "B": "A big step cannot settle into a minimum",
   "C": "It reduces the parameter count",
   "D": "It stops gradients vanishing"},
  ["B"], "The step that made early progress is too coarse near the end, so the loss just bounces around.")

a(T_LO, "intermediate", 2, "multiple_choice",
  "Which statements about momentum are true? (Select all that apply)",
  {"A": "It builds a velocity from past gradients",
   "B": "It damps oscillation across a ravine",
   "C": "Values near 0.9 are common",
   "D": "It replaces the learning rate"},
  ["A", "B", "C"], "A learning rate is still needed. Momentum changes how the gradient is applied, not whether it is scaled.")

a(T_LO, "advanced", 3, "single_choice",
  "What does Adam add over plain momentum?",
  {"A": "A second moment, giving per-parameter step sizes",
   "B": "A larger learning rate",
   "C": "Gradient clipping",
   "D": "Weight decay"},
  ["A"], "Dividing by the typical gradient size makes each parameter's step roughly scale-free.")

a(T_LO, "advanced", 3, "single_choice",
  "Why does Adam apply bias correction?",
  {"A": "The moment estimates start at zero and read too low",
   "B": "The gradients can be negative",
   "C": "The learning rate is too high early on",
   "D": "The bias terms are otherwise ignored"},
  ["A"], "A running average starting from zero underestimates until enough terms build up.")

a(T_LO, "advanced", 3, "single_choice",
  "Would an activation that is flat below -0.5, linear in between, and flat above 0.5 train well?",
  {"A": "Yes, it is a bounded ReLU",
   "B": "No, units in the flat parts get no gradient",
   "C": "Yes, bounded outputs help",
   "D": "No, it is discontinuous"},
  ["B"], "It is continuous, so that is not the issue. The flat regions kill the learning signal.")

a(T_LO, "intermediate", 2, "single_choice",
  "A model predicts 0.8, 0.4 and 0.7 for three positive samples, thresholded at 0.5. What is the accuracy?",
  {"A": "1/3",
   "B": "2/3",
   "C": "3/3",
   "D": "0"},
  ["B"], "Only the 0.4 falls below the threshold.")

a(T_LO, "advanced", 3, "multiple_choice",
  "Training loss sits high and flat from the first epoch. What is worth checking? (Select all that apply)",
  {"A": "Whether the learning rate is far too small",
   "B": "Whether labels line up with inputs",
   "C": "Whether the model has enough capacity",
   "D": "Whether dropout should be added"},
  ["A", "B", "C"], "A flat high loss means underfitting or a bug. Dropout would only make it worse.")

a(T_LO, "advanced", 3, "single_choice",
  "You feed a GAN sorted batches: all dogs, then all cats. Why is that bad?",
  {"A": "The batches are too large",
   "B": "Each batch gradient is biased towards one class",
   "C": "The discriminator cannot handle two classes",
   "D": "It is fine within one epoch"},
  ["B"], "Mini-batch methods assume each batch represents the data, and sorted batches break that.")

a(T_LO, "basics", 1, "single_choice",
  "What does a loss function return for one mini-batch?",
  {"A": "One value per sample",
   "B": "A single number",
   "C": "One value per class",
   "D": "A matrix of gradients"},
  ["B"], "Gradient descent needs a scalar, so per-sample losses are summed or averaged first.")

# =========================================================================
# Activation Functions and CNN
# =========================================================================

a(T_CNN, "basics", 1, "single_choice",
  "What does ReLU return for the inputs (-2, 0, 3)?",
  {"A": "(0, 0, 3)",
   "B": "(-2, 0, 3)",
   "C": "(0, 0, 1)",
   "D": "(2, 0, 3)"},
  ["A"], "Negatives are clamped to zero, everything else passes through.")

a(T_CNN, "intermediate", 2, "single_choice",
  "Why is ReLU usually preferred to sigmoid in hidden layers?",
  {"A": "It is bounded, so activations cannot blow up",
   "B": "Its gradient is 1 on the positive side",
   "C": "It has trainable parameters",
   "D": "It is easier to differentiate"},
  ["B"], "The sigmoid derivative peaks at 0.25 and nearly vanishes in its tails, so gradients shrink layer by layer.")

a(T_CNN, "intermediate", 2, "single_choice",
  "What problem does leaky ReLU fix?",
  {"A": "Exploding gradients",
   "B": "Units that stop learning once their input stays negative",
   "C": "Overfitting",
   "D": "Slow convergence on the positive side"},
  ["B"], "A small negative slope keeps a gradient alive so the unit can recover.")

a(T_CNN, "basics", 1, "single_choice",
  "What does softmax guarantee about its output?",
  {"A": "Entries are non-negative and sum to one",
   "B": "Entries lie between -1 and 1",
   "C": "Exactly one entry is 1",
   "D": "Entries are sorted"},
  ["A"], "That is what lets the output be read as a probability distribution.")

a(T_CNN, "intermediate", 2, "multiple_choice",
  "Which statements about a convolutional layer are true? (Select all that apply)",
  {"A": "Weight count depends on input channels",
   "B": "Weight count depends on the stride",
   "C": "It accepts inputs of any spatial size",
   "D": "It gives rotation invariant features"},
  ["A", "C"], "Stride changes where the kernel lands, not how many weights it has, and convolution gives translation equivariance rather than rotation invariance.")

a(T_CNN, "intermediate", 2, "single_choice",
  "Why does a convolutional layer need far fewer weights than a fully connected one?",
  {"A": "It uses fewer bits per weight",
   "B": "One kernel is reused at every position",
   "C": "It ignores colour channels",
   "D": "It only sees part of the image"},
  ["B"], "Weight sharing also encodes the idea that a useful pattern is worth spotting anywhere.")

a(T_CNN, "intermediate", 2, "single_choice",
  "An X by X image feeds a fully connected layer with Z outputs. How many weights, ignoring bias?",
  {"A": "X * Z",
   "B": "X^2 * Z",
   "C": "X^2 + Z",
   "D": "X * Z^2"},
  ["B"], "Every pixel connects to every output. A convolution with N kernels of size K needs only N * K^2.")

a(T_CNN, "intermediate", 2, "single_choice",
  "Input width 32, kernel width 5, stride 1, no padding. What is the output width?",
  {"A": "27",
   "B": "28",
   "C": "30",
   "D": "32"},
  ["B"], "(32 - 5) / 1 + 1 = 28.")

a(T_CNN, "advanced", 3, "single_choice",
  "Input width 32, kernel width 3, stride 2, padding 1. What is the output width?",
  {"A": "15",
   "B": "16",
   "C": "17",
   "D": "31"},
  ["B"], "(32 - 3 + 2) / 2 + 1 = 16, so stride 2 halves it.")

a(T_CNN, "basics", 1, "single_choice",
  "A layer applies 16 kernels to a 3 channel input. How many output channels?",
  {"A": "3",
   "B": "16",
   "C": "19",
   "D": "48"},
  ["B"], "Each kernel spans all input channels and yields one feature map.")

a(T_CNN, "intermediate", 2, "single_choice",
  "Which claim about a valid convolution is false?",
  {"A": "It keeps the input size",
   "B": "It uses no padding",
   "C": "It drops partial-overlap positions",
   "D": "Its output is smaller than same padding gives"},
  ["A"], "That describes same padding. Valid convolution shrinks each dimension by k-1.")

a(T_CNN, "advanced", 3, "single_choice",
  "What is the receptive field of a unit after two stacked 3x3 convolutions, stride 1?",
  {"A": "3x3",
   "B": "5x5",
   "C": "6x6",
   "D": "9x9"},
  ["B"], "Each layer widens it by 2. Two 3x3 layers beat one 5x5 on parameter count and add a non-linearity.")

a(T_CNN, "intermediate", 2, "single_choice",
  "What is a 1x1 convolution good for?",
  {"A": "Raising the spatial resolution",
   "B": "Mixing channels and changing their number cheaply",
   "C": "Widening the receptive field",
   "D": "Replacing the activation"},
  ["B"], "It is a per-pixel linear map across channels, often used to cut depth before an expensive layer.")

a(T_CNN, "advanced", 3, "single_choice",
  "What does a dilated convolution buy you?",
  {"A": "Fewer channels",
   "B": "A wider receptive field at no extra parameter cost",
   "C": "Guaranteed translation invariance",
   "D": "Faster training"},
  ["B"], "Gaps between the kernel taps widen the field fast with depth, which is why segmentation models like it.")

a(T_CNN, "intermediate", 2, "multiple_choice",
  "Which statements about pooling are true? (Select all that apply)",
  {"A": "It shrinks the spatial dimensions",
   "B": "It has no trainable parameters",
   "C": "It adds some translation tolerance",
   "D": "It increases the channel count"},
  ["A", "B", "C"], "Pooling works inside each channel, so the depth is untouched.")

a(T_CNN, "basics", 1, "single_choice",
  "A 2x2 pooling window with stride 2 is applied to a 32x32 map. What comes out?",
  {"A": "8x8",
   "B": "16x16",
   "C": "30x30",
   "D": "32x32"},
  ["B"], "Stride 2 halves both spatial dimensions.")

a(T_CNN, "advanced", 3, "single_choice",
  "What does max pooling have to remember for its backward pass?",
  {"A": "The window averages",
   "B": "Where the maxima were",
   "C": "The whole input",
   "D": "Nothing, it has no parameters"},
  ["B"], "Only the winning element affected the output, so only it receives gradient.")

a(T_CNN, "basics", 1, "single_choice",
  "What does a flatten layer do between convolutions and a dense layer?",
  {"A": "Averages each channel to one value",
   "B": "Reshapes the feature maps into a vector",
   "C": "Normalises the activations",
   "D": "Cuts the channel count"},
  ["B"], "Averaging per channel is global average pooling, a different thing. Flatten keeps every value.")

a(T_CNN, "advanced", 3, "single_choice",
  "A 256x256x3 image goes through Conv2d(3, 16, 3, padding=1) then back to 3 channels the same way. What shape comes out?",
  {"A": "254 x 254 x 3",
   "B": "256 x 256 x 3",
   "C": "128 x 128 x 16",
   "D": "256 x 256 x 16"},
  ["B"], "A 3x3 kernel with padding 1 and stride 1 preserves the spatial size.")

a(T_CNN, "advanced", 3, "single_choice",
  "Why is a stride above 1 sometimes called subsampling?",
  {"A": "It averages nearby pixels",
   "B": "It only evaluates the kernel every s positions",
   "C": "It cuts the channel count",
   "D": "It samples positions at random"},
  ["B"], "That is why a strided convolution can be done as stride 1 followed by dropping rows and columns.")

a(T_CNN, "advanced", 3, "single_choice",
  "Why does an even kernel need uneven padding to keep the input size?",
  {"A": "It has no centre pixel to balance around",
   "B": "It has twice the weights",
   "C": "The stride must also be even",
   "D": "It does not, padding is the same"},
  ["A"], "An odd kernel pads (k-1)/2 on each side. For an even one no integer works on both sides.")

# =========================================================================
# Regularization
# =========================================================================

a(T_REG, "basics", 1, "single_choice",
  "What is regularisation for?",
  {"A": "Speeding up convergence",
   "B": "Improving generalisation by limiting complexity",
   "C": "Shrinking the model file",
   "D": "Removing the validation set"},
  ["B"], "It trades a little training accuracy for a smaller gap to unseen data.")

a(T_REG, "intermediate", 2, "multiple_choice",
  "Which of these are regularisation techniques? (Select all that apply)",
  {"A": "Dropout",
   "B": "Weight decay",
   "C": "Data augmentation",
   "D": "Raising the learning rate"},
  ["A", "B", "C"], "A larger learning rate just destabilises training.")

a(T_REG, "intermediate", 2, "multiple_choice",
  "Which statements comparing L1 and L2 are true? (Select all that apply)",
  {"A": "L1 pushes many weights to exactly zero",
   "B": "L2 shrinks large weights hardest",
   "C": "Both add a term to the loss",
   "D": "L1 is smooth everywhere"},
  ["A", "B", "C"], "It is L2 that is smooth. The absolute value has a kink at zero.")

a(T_REG, "advanced", 3, "single_choice",
  "A weight histogram shows a tall spike exactly at zero. Which regulariser was used?",
  {"A": "L2",
   "B": "L1",
   "C": "Dropout",
   "D": "None"},
  ["B"], "L2 shrinks weights towards zero without reaching it. L1 has constant gradient, so it arrives.")

a(T_REG, "advanced", 3, "single_choice",
  "Your model overfits and you suspect many input features are useless. Which regulariser first?",
  {"A": "L2, since it shrinks everything",
   "B": "L1, since it zeroes irrelevant weights",
   "C": "A bigger batch size",
   "D": "Removing the biases"},
  ["B"], "L2 would shrink those weights but leave them contributing noise.")

a(T_REG, "intermediate", 2, "single_choice",
  "What is dropout actually attacking?",
  {"A": "Vanishing gradients",
   "B": "Units that only work alongside particular partners",
   "C": "Exploding activations",
   "D": "Class imbalance"},
  ["B"], "If any partner might vanish, the layer has to learn more redundant features.")

a(T_REG, "basics", 1, "single_choice",
  "What does dropout do at inference time?",
  {"A": "Drops the same fraction as in training",
   "B": "Nothing, the full network is used",
   "C": "Drops units but doubles the outputs",
   "D": "Removes itself from the model"},
  ["B"], "Predictions need to be deterministic, which is why the scaling correction happens during training.")

a(T_REG, "advanced", 3, "single_choice",
  "Inverted dropout divides surviving activations by the keep probability during training. Why?",
  {"A": "It makes the activations larger, so training converges sooner",
   "B": "It keeps the expected activation the same, so testing needs no rescaling",
   "C": "It removes the need to store the mask used in the forward pass",
   "D": "It lets gradients bypass the layer during backpropagation"},
  ["B"], "The correction has to happen somewhere. Doing it in training leaves inference clean.")

a(T_REG, "basics", 1, "single_choice",
  "What does batch normalisation normalise?",
  {"A": "The layer weights",
   "B": "The activations, using batch statistics",
   "C": "The learning rate",
   "D": "The gradients"},
  ["B"], "It then applies a learned scale and shift so the network can undo it if that helps.")

a(T_REG, "advanced", 3, "single_choice",
  "Why can batch normalisation not use batch statistics at test time?",
  {"A": "Batches are too small then",
   "B": "A prediction would depend on the other samples in the batch",
   "C": "The statistics are undefined",
   "D": "It would be too slow"},
  ["B"], "The same image could get different answers depending on what it was batched with, so stored running estimates are used.")

a(T_REG, "advanced", 3, "single_choice",
  "In convolutional batch normalisation, what are the statistics computed over?",
  {"A": "Each pixel position separately",
   "B": "The batch and all positions, one pair per channel",
   "C": "Each sample separately",
   "D": "The whole tensor at once"},
  ["B"], "It mirrors weight sharing: one kernel applies everywhere, so its outputs are pooled everywhere.")

a(T_REG, "intermediate", 2, "single_choice",
  "Batch normalisation starts with scale 1 and shift 0. Why those values?",
  {"A": "The layer starts as an identity on the normalised signal",
   "B": "They force zero mean output",
   "C": "They lock the distribution",
   "D": "They make it non-trainable"},
  ["A"], "Starting from the identity means the layer does not disturb training before it has learned anything.")

a(T_REG, "advanced", 3, "multiple_choice",
  "Which statements about batch normalisation are true? (Select all that apply)",
  {"A": "It smooths the loss surface",
   "B": "It normalises the weights",
   "C": "It can be skipped at inference",
   "D": "It reduces drift in layer inputs"},
  ["A", "D"], "It normalises activations, and skipping it at inference would break the trained network.")

a(T_REG, "advanced", 3, "single_choice",
  "Why is batch normalisation said to regularise a little?",
  {"A": "It adds a penalty to the loss",
   "B": "Batch statistics inject noise into each sample",
   "C": "It removes parameters",
   "D": "It lowers the learning rate"},
  ["B"], "The effect fades as batches grow and the statistics settle.")

a(T_REG, "intermediate", 2, "single_choice",
  "Why does data augmentation act as a regulariser?",
  {"A": "It reduces how many parameters the network has to fit",
   "B": "It widens the training distribution, so memorising gets harder",
   "C": "It lowers the effective learning rate as training proceeds",
   "D": "It rescales the activations of each layer to zero mean"},
  ["B"], "It also builds in invariances you already know the task has.")

a(T_REG, "intermediate", 2, "single_choice",
  "What is early stopping?",
  {"A": "Stopping when the training loss flattens",
   "B": "Stopping when validation stops improving, keeping the best model",
   "C": "Cutting the learning rate when progress slows",
   "D": "Dropping layers during training"},
  ["B"], "It limits how far optimisation drifts from the starting point, which is a form of regularisation.")

a(T_REG, "advanced", 3, "single_choice",
  "What causes internal covariate shift?",
  {"A": "Updates to earlier layers changing what later layers see",
   "B": "Test data drawn from another population",
   "C": "A learning rate that is too small",
   "D": "A non-convex loss"},
  ["A"], "The second option is dataset shift, a different problem entirely.")

a(T_REG, "basics", 1, "single_choice",
  "What does the regularisation weight control?",
  {"A": "The learning rate",
   "B": "How much the penalty counts against the data term",
   "C": "The dropout fraction",
   "D": "The batch size"},
  ["B"], "Too large and the model underfits, too small and it does nothing.")

# =========================================================================
# Recurrent Neural Networks
# =========================================================================

a(T_RNN, "basics", 1, "single_choice",
  "What does the hidden state of a recurrent cell hold?",
  {"A": "The network parameters",
   "B": "A summary of the sequence so far",
   "C": "The current gradient",
   "D": "The sequence length"},
  ["B"], "It is the only route by which earlier inputs reach later outputs.")

a(T_RNN, "intermediate", 2, "single_choice",
  "Why do recurrent networks suit time series?",
  {"A": "They process all steps at once",
   "B": "Their state carries information between steps",
   "C": "They need fewer parameters",
   "D": "They ignore input order"},
  ["B"], "Ignoring order would defeat the point. The recurrence is exactly what makes them order-dependent.")

a(T_RNN, "intermediate", 2, "single_choice",
  "Image captioning takes one image and returns a sentence. What mapping is that?",
  {"A": "One to one",
   "B": "One to many",
   "C": "Many to one",
   "D": "Many to many"},
  ["B"], "Sentiment scoring of a whole review is the mirror image, many to one.")

a(T_RNN, "advanced", 4, "single_choice",
  "A cell computes h_t = ReLU(h_{t-1} + 2 x_t) with h_0 = 0. For x = (2, -1), what is h_2?",
  {"A": "0",
   "B": "2",
   "C": "4",
   "D": "6"},
  ["B"], "h_1 = ReLU(4) = 4, then h_2 = ReLU(4 - 2) = 2.")

a(T_RNN, "advanced", 3, "single_choice",
  "Your recurrent cell uses only ReLU and all weights and inputs are positive. What happens over a long sequence?",
  {"A": "The state settles at 1",
   "B": "The state and gradients grow without limit",
   "C": "The state decays to zero",
   "D": "The state oscillates"},
  ["B"], "A bounded activation like tanh prevents this, at the cost of making vanishing gradients the bigger risk.")

a(T_RNN, "advanced", 3, "single_choice",
  "Why must weights not be updated step by step while backpropagating through time?",
  {"A": "The learning rate would need rescaling",
   "B": "The function would change while it is being differentiated",
   "C": "Optimizer state would be lost",
   "D": "The hidden state would reset"},
  ["B"], "Gradients are accumulated across all steps and applied once at the end.")

a(T_RNN, "intermediate", 2, "multiple_choice",
  "Which statements about backpropagation through time are true? (Select all that apply)",
  {"A": "The network is unrolled over the sequence",
   "B": "Gradients are summed across time steps",
   "C": "Truncating it bounds memory use",
   "D": "Each step has its own weights"},
  ["A", "B", "C"], "Sharing weights across time is what makes a network recurrent in the first place.")

a(T_RNN, "intermediate", 2, "single_choice",
  "What does gradient clipping fix in a recurrent network?",
  {"A": "Vanishing gradients",
   "B": "Exploding gradients",
   "C": "Overfitting",
   "D": "Class imbalance"},
  ["B"], "Vanishing gradients need architectural fixes such as gating, not clipping.")

a(T_RNN, "intermediate", 2, "single_choice",
  "What is the main thing an LSTM buys you over a simple recurrent cell?",
  {"A": "Fewer parameters",
   "B": "A gated cell state that carries gradients further",
   "C": "No need for backpropagation through time",
   "D": "Faster inference"},
  ["B"], "The cell state is updated additively, so gradients are not squashed at every step.")

a(T_RNN, "basics", 1, "single_choice",
  "Which activations are used inside LSTM gates?",
  {"A": "ReLU and softmax",
   "B": "Sigmoid and tanh",
   "C": "Linear and softmax",
   "D": "ELU and leaky ReLU"},
  ["B"], "A gate needs an output between 0 and 1 to act as a soft switch, which is what sigmoid gives.")

a(T_RNN, "advanced", 3, "single_choice",
  "How does a GRU differ from an LSTM?",
  {"A": "It adds a third gate",
   "B": "It merges gates and drops the separate cell state",
   "C": "It cannot model long dependencies",
   "D": "It needs no training"},
  ["B"], "Fewer parameters and slightly faster training, with accuracy usually close enough that the choice is empirical.")

a(T_RNN, "intermediate", 2, "single_choice",
  "What does a bidirectional recurrent network add?",
  {"A": "Half the parameters",
   "B": "A reverse pass, so each step sees future context",
   "C": "Immunity to vanishing gradients",
   "D": "Support for variable lengths"},
  ["B"], "It only works when the whole sequence is available up front, so it rules out live generation.")

a(T_RNN, "intermediate", 2, "single_choice",
  "What is the encoder's job in a sequence-to-sequence model?",
  {"A": "Generating the output tokens",
   "B": "Turning the input into a representation for the decoder",
   "C": "Computing the loss",
   "D": "Shuffling the data"},
  ["B"], "The split is what lets input and output have different lengths.")

a(T_RNN, "advanced", 3, "single_choice",
  "Why was attention added to encoder-decoder models?",
  {"A": "To cut the parameter count",
   "B": "One fixed context vector is a bottleneck for long inputs",
   "C": "To remove the encoder",
   "D": "To parallelise training"},
  ["B"], "Parallel training came later with transformers. Attention was first bolted onto recurrent models.")

a(T_RNN, "intermediate", 2, "single_choice",
  "What is teacher forcing?",
  {"A": "Feeding the true previous token instead of the model's own guess",
   "B": "Raising the learning rate on the last layer of the decoder",
   "C": "Averaging the predictions of two separately trained models",
   "D": "Freezing the encoder so only the decoder keeps training"},
  ["A"], "It speeds up early training but leaves a mismatch with inference, where only the model's own output exists.")

a(T_RNN, "intermediate", 2, "single_choice",
  "Which sequence sampling strategy does not exist?",
  {"A": "Greedy sampling",
   "B": "Recognition sampling",
   "C": "Random sampling",
   "D": "Beam search"},
  ["B"], "Beam search keeps several partial hypotheses alive rather than committing at each step.")

a(T_RNN, "intermediate", 2, "single_choice",
  "A recurrent output goes straight into cross entropy with no final activation. What is wrong?",
  {"A": "Cross entropy is not differentiable",
   "B": "It expects probabilities, not unbounded values",
   "C": "The loss would be zero",
   "D": "Recurrent cells cannot classify"},
  ["B"], "The log in the loss is undefined for non-positive inputs.")

# =========================================================================
# Unsupervised Learning
# =========================================================================

a(T_UNS, "basics", 1, "single_choice",
  "What does an autoencoder learn?",
  {"A": "A map from inputs to labels",
   "B": "A compact code the input can be rebuilt from",
   "C": "The best learning rate",
   "D": "A distribution over labels"},
  ["B"], "The bottleneck forces it to keep only what reconstruction needs.")

a(T_UNS, "advanced", 3, "single_choice",
  "You build an autoencoder whose code is larger than its input, with no other constraint. What happens?",
  {"A": "It learns a richer representation",
   "B": "It can just copy the input and learn nothing",
   "C": "It cannot be trained",
   "D": "It becomes equivalent to PCA"},
  ["B"], "An overcomplete autoencoder needs sparsity, noise or a penalty to force it to find structure.")

a(T_UNS, "intermediate", 2, "single_choice",
  "What makes a denoising autoencoder different?",
  {"A": "It has no decoder",
   "B": "It rebuilds clean input from a corrupted copy",
   "C": "It uses labels",
   "D": "It cannot use convolutions"},
  ["B"], "Copying no longer works, so the model has to learn the structure of the data.")

a(T_UNS, "advanced", 3, "single_choice",
  "What does a variational autoencoder encode each input to?",
  {"A": "A single point in latent space",
   "B": "A distribution over latent space",
   "C": "A class label",
   "D": "A binary code"},
  ["B"], "Its loss pairs reconstruction with a term pulling those distributions towards a prior, which makes sampling possible.")

a(T_UNS, "advanced", 3, "single_choice",
  "Why does a VAE need the reparameterisation trick?",
  {"A": "To cut parameters",
   "B": "Sampling blocks gradients, so the randomness is moved aside",
   "C": "To make the decoder deterministic",
   "D": "To normalise the latent space"},
  ["B"], "Writing the sample as mean plus sigma times noise leaves a differentiable path back to the encoder.")

a(T_UNS, "basics", 1, "single_choice",
  "What are the two networks in a GAN?",
  {"A": "Encoder and decoder",
   "B": "Generator and discriminator",
   "C": "Actor and critic",
   "D": "Teacher and student"},
  ["B"], "The generator makes samples from noise and the discriminator tries to spot them.")

a(T_UNS, "intermediate", 2, "single_choice",
  "How is a GAN trained?",
  {"A": "Each network is trained to convergence in turn",
   "B": "As a min-max game between the two networks",
   "C": "By minimising reconstruction error",
   "D": "By maximising data likelihood directly"},
  ["B"], "The generator improves precisely by making the discriminator's job harder.")

a(T_UNS, "advanced", 3, "single_choice",
  "What is mode collapse?",
  {"A": "The discriminator becomes perfect",
   "B": "The generator only produces a narrow set of outputs",
   "C": "The weights go to zero",
   "D": "The loss goes negative"},
  ["B"], "A few samples reliably fool the discriminator, so the generator never explores further.")

a(T_UNS, "advanced", 3, "single_choice",
  "How does a conditional GAN let you ask for a specific kind of sample?",
  {"A": "By retraining for each request",
   "B": "By feeding both networks a class input",
   "C": "By filtering afterwards",
   "D": "By enlarging the noise vector"},
  ["B"], "The training data has to be labelled so the discriminator can judge realism given the class.")

a(T_UNS, "intermediate", 2, "single_choice",
  "What is PCA for?",
  {"A": "Grouping data points into a fixed number of labelled classes",
   "B": "Finding directions of greatest variance to reduce dimensions",
   "C": "Generating new samples that resemble the training data",
   "D": "Penalising large weights so a network generalises better"},
  ["B"], "The components are the leading eigenvectors of the covariance matrix.")

a(T_UNS, "intermediate", 2, "single_choice",
  "What does k-means do on each iteration?",
  {"A": "Assigns points to the nearest centre, then moves the centres",
   "B": "Trains a small network to predict the cluster of each point",
   "C": "Computes the eigenvectors of the data covariance matrix",
   "D": "Assigns the true class label to every point in the set"},
  ["A"], "It reaches a local optimum that depends on where the centres started.")

a(T_UNS, "advanced", 3, "single_choice",
  "What can DBSCAN do that k-means cannot?",
  {"A": "Run faster on every dataset",
   "B": "Find non-spherical clusters without being told how many",
   "C": "Guarantee a global optimum",
   "D": "Work without a distance measure"},
  ["B"], "The trade is that you now have to pick a density threshold and a radius instead.")

a(T_UNS, "intermediate", 2, "single_choice",
  "Why are learned word embeddings better than one-hot vectors?",
  {"A": "They use less memory only",
   "B": "Similar words end up close together",
   "C": "They need no data",
   "D": "They prevent overfitting"},
  ["B"], "One-hot vectors sit at equal distance from each other, so they carry no similarity information.")

a(T_UNS, "advanced", 3, "multiple_choice",
  "Which of these objectives are unsupervised? (Select all that apply)",
  {"A": "Rebuilding the input through a bottleneck",
   "B": "Matching a generated distribution to the data",
   "C": "Grouping samples by similarity",
   "D": "Cross entropy against human labels"},
  ["A", "B", "C"], "The last one is the definition of supervised learning.")

a(T_UNS, "intermediate", 2, "single_choice",
  "In an encoder-decoder diagram, what does the narrow middle represent?",
  {"A": "The loss function",
   "B": "The bottleneck, or latent code",
   "C": "The output layer",
   "D": "The batch dimension"},
  ["B"], "Its size decides how much the model is allowed to keep.")

# =========================================================================
# Common Practices
# =========================================================================

a(T_CP, "basics", 1, "single_choice",
  "What is one epoch?",
  {"A": "One parameter update",
   "B": "One full pass over the training set",
   "C": "One forward pass",
   "D": "One validation run"},
  ["B"], "An epoch contains many updates, one per mini-batch.")

a(T_CP, "intermediate", 2, "single_choice",
  "Why report the final score on a test set rather than the validation set?",
  {"A": "Validation sets are too small",
   "B": "Tuning on validation makes its score optimistic",
   "C": "Test sets are easier",
   "D": "Validation sets have no labels"},
  ["B"], "Every decision made by looking at a split leaks a little information about it.")

a(T_CP, "intermediate", 2, "single_choice",
  "What does k-fold cross-validation give you?",
  {"A": "Faster training",
   "B": "A steadier estimate by averaging over splits",
   "C": "Immunity to overfitting",
   "D": "More training data"},
  ["B"], "Most useful on small datasets, where one split can be unlucky. The cost is training k times.")

a(T_CP, "intermediate", 2, "single_choice",
  "When would you use over- or undersampling?",
  {"A": "To handle class imbalance",
   "B": "To evaluate segmentation",
   "C": "To tune dropout",
   "D": "To generate synthetic data"},
  ["A"], "Weighting the loss by inverse class frequency does much the same without touching the data.")

a(T_CP, "intermediate", 2, "single_choice",
  "Which metric suits a heavily imbalanced binary problem?",
  {"A": "Accuracy",
   "B": "F1 or area under the ROC curve",
   "C": "Training loss",
   "D": "Parameter count"},
  ["B"], "Predicting the majority class for everything can score above 95% accuracy while detecting nothing.")

a(T_CP, "basics", 1, "single_choice",
  "What does the F1 score combine?",
  {"A": "Accuracy and loss",
   "B": "Precision and recall",
   "C": "True and false positives",
   "D": "Train and test error"},
  ["B"], "It is their harmonic mean, so both have to be decent for it to be high.")

a(T_CP, "intermediate", 2, "multiple_choice",
  "Which statements about transfer learning are true? (Select all that apply)",
  {"A": "Early layers learn generic features that transfer",
   "B": "It helps most when the new dataset is small",
   "C": "The final layer usually gets replaced",
   "D": "Both tasks need the same labels"},
  ["A", "B", "C"], "Identical labels would make the whole exercise pointless.")

a(T_CP, "advanced", 3, "single_choice",
  "Why is random search often better than grid search over several hyperparameters?",
  {"A": "It always reaches a good setting in fewer total trials",
   "B": "Grid search wastes trials repeating values of the parameter that matters",
   "C": "It is guaranteed to land on the global optimum eventually",
   "D": "It can be run without holding out any validation data"},
  ["B"], "Random search samples a fresh value on every axis, so it explores the important one far better.")

a(T_CP, "advanced", 3, "single_choice",
  "Your network was trained on 32x32 images and ends in flatten plus dense layers. How do you let it take any size?",
  {"A": "Resize every incoming image down to 32x32 before the network",
   "B": "Swap the dense layers for convolutions and global average pooling",
   "C": "Add a recurrent layer that reads the feature map row by row",
   "D": "Train a separate copy of the network at each resolution"},
  ["B"], "Convolutions have no fixed input size and global pooling collapses whatever is left.")

a(T_CP, "intermediate", 2, "single_choice",
  "Why normalise input features?",
  {"A": "It reduces the number of parameters the model has to learn",
   "B": "Mismatched scales make the loss surface awkward to descend",
   "C": "It removes outliers that would otherwise dominate the loss",
   "D": "It increases the range of functions the model can fit"},
  ["B"], "A stretched loss surface makes gradient descent zig-zag and forces a smaller learning rate.")

a(T_CP, "intermediate", 2, "single_choice",
  "Which statistics should normalise the test set?",
  {"A": "Those computed on the test set",
   "B": "Those computed on the training set",
   "C": "Those of each sample separately",
   "D": "Fixed values of 0 and 1"},
  ["B"], "Using test statistics would apply a different transform than the model was trained under.")

a(T_CP, "basics", 1, "single_choice",
  "Why switch a model to evaluation mode before inference?",
  {"A": "To free memory",
   "B": "So dropout and batch norm behave correctly",
   "C": "To reset the weights",
   "D": "To turn on gradients"},
  ["B"], "Forget it and dropout stays active, making predictions noisy and irreproducible.")

a(T_CP, "intermediate", 2, "single_choice",
  "Your training loss falls while validation loss climbs from epoch 12. What do you do?",
  {"A": "Train longer",
   "B": "Stop around epoch 12 and keep that model",
   "C": "Raise the learning rate",
   "D": "Enlarge the validation set"},
  ["B"], "The point where the two curves part is exactly what early stopping looks for.")

a(T_CP, "intermediate", 2, "single_choice",
  "The loss does not move at all from the first iteration. What is the likely cause?",
  {"A": "The updates are not reaching the parameters",
   "B": "The batch size is too large",
   "C": "The validation set is small",
   "D": "There are too many layers"},
  ["A"], "A perfectly flat loss usually means a zero learning rate or an optimizer that never got the parameters.")

# =========================================================================
# Architectures
# =========================================================================

a(T_ARCH, "basics", 1, "single_choice",
  "What is a skip connection?",
  {"A": "A link that adds a block's input to its output",
   "B": "A link that drops a layer during training",
   "C": "A link between two networks",
   "D": "A link that bypasses the loss"},
  ["A"], "It gives gradients a short path back and lets a block fall back to the identity.")

a(T_ARCH, "intermediate", 2, "single_choice",
  "What was ResNet's key idea?",
  {"A": "Parallel paths with different kernel sizes",
   "B": "Learning a residual on top of the identity",
   "C": "Replacing convolution with attention",
   "D": "Dropping pooling entirely"},
  ["B"], "That is what made networks over a hundred layers deep trainable.")

a(T_ARCH, "intermediate", 2, "single_choice",
  "What is VGG known for?",
  {"A": "Introducing skip connections",
   "B": "Stacking small 3x3 convolutions instead of large kernels",
   "C": "Introducing attention",
   "D": "Dropping dense layers"},
  ["B"], "Its uniform design made it a popular backbone, though its dense layers are parameter heavy.")

a(T_ARCH, "advanced", 3, "single_choice",
  "What does an Inception module do?",
  {"A": "Runs several kernel sizes side by side and concatenates",
   "B": "Removes all pooling",
   "C": "Adds recurrence",
   "D": "Applies dropout everywhere"},
  ["A"], "1x1 convolutions cut the depth first so the wider kernels stay affordable.")

a(T_ARCH, "advanced", 3, "single_choice",
  "Inside a residual block the stride and channel count change. What happens to the shortcut?",
  {"A": "Nothing, addition broadcasts",
   "B": "It gets a 1x1 convolution to match shapes",
   "C": "It becomes a concatenation",
   "D": "The block splits in two"},
  ["B"], "Addition needs matching shapes on both branches.")

a(T_ARCH, "intermediate", 2, "single_choice",
  "What is the core mechanism of a transformer?",
  {"A": "Recurrence",
   "B": "Self-attention over all positions at once",
   "C": "Dilated convolution",
   "D": "Clustering of tokens"},
  ["B"], "Constant path length between positions avoids the long-range decay that limits recurrent models.")

a(T_ARCH, "intermediate", 2, "single_choice",
  "How does a Vision Transformer feed an image to the model?",
  {"A": "One token per pixel",
   "B": "One token per fixed-size patch",
   "C": "The whole image as one token",
   "D": "One token per channel"},
  ["B"], "Attention cost grows quadratically with length, so a token per pixel would be far too expensive.")

a(T_ARCH, "basics", 1, "single_choice",
  "What does global average pooling produce from C feature maps?",
  {"A": "A vector of length C",
   "B": "A map at half the size",
   "C": "A single number",
   "D": "One value per pixel"},
  ["A"], "Because the spatial extent disappears, the classifier stops depending on input resolution.")

a(T_ARCH, "intermediate", 2, "multiple_choice",
  "Which features does LeNet not use? (Select all that apply)",
  {"A": "Skip connections",
   "B": "Pooling layers",
   "C": "ReLU activations",
   "D": "Convolutional layers"},
  ["A", "C"], "LeNet predates both. It used sigmoid and tanh, and skip connections arrived with ResNet.")

a(T_ARCH, "advanced", 3, "single_choice",
  "Two stacked 3x3 convolutions replace one 5x5. What is gained?",
  {"A": "A wider receptive field",
   "B": "Fewer parameters and an extra non-linearity",
   "C": "Fewer channels",
   "D": "Faster inference only"},
  ["B"], "Both cover 5x5, but the pair uses 18 weights per channel pair instead of 25.")

# =========================================================================
# Visualization and Attention
# =========================================================================

a(T_VIS, "intermediate", 2, "single_choice",
  "What does a saliency map show?",
  {"A": "The first layer's kernels",
   "B": "Which pixels the prediction is most sensitive to",
   "C": "The label distribution",
   "D": "The loss over time"},
  ["B"], "A quick way to check the model is looking at the object and not the background.")

a(T_VIS, "intermediate", 2, "single_choice",
  "What is Grad-CAM for?",
  {"A": "Speeding up training",
   "B": "A class-specific heat map from a convolutional layer",
   "C": "Compressing a model",
   "D": "Augmenting data"},
  ["B"], "It weights feature maps by their gradients, so the result is coarse but tied to one class.")

a(T_VIS, "intermediate", 2, "single_choice",
  "Deeper kernels are hard to read directly. What do people look at instead?",
  {"A": "The learning rate",
   "B": "The activations for a given input",
   "C": "The bias values",
   "D": "The batch statistics"},
  ["B"], "Activations show what the layer responds to on a real image.")

a(T_VIS, "intermediate", 2, "single_choice",
  "Which of these is not a way to highlight important image regions?",
  {"A": "Saliency maps",
   "B": "Inception",
   "C": "Occlusion",
   "D": "Guided backpropagation"},
  ["B"], "Inception is an architecture, not an interpretation method.")

a(T_VIS, "advanced", 3, "single_choice",
  "In self-attention, where do query, key and value come from?",
  {"A": "Three separately trained networks",
   "B": "Three learned projections of the same input",
   "C": "The labels",
   "D": "A fixed lookup table"},
  ["B"], "Attending to projections of the same sequence is what makes it self-attention.")

a(T_VIS, "intermediate", 2, "single_choice",
  "Why do transformers need positional encoding?",
  {"A": "To normalise attention weights",
   "B": "Attention alone would treat a shuffled sequence the same",
   "C": "To cut parameters",
   "D": "To prevent overfitting"},
  ["B"], "Recurrent and convolutional models get position from their structure. Attention does not.")

a(T_VIS, "advanced", 3, "single_choice",
  "What does multi-head attention add over one head?",
  {"A": "Faster convergence only",
   "B": "Several attention patterns in different subspaces",
   "C": "Guaranteed sparse weights",
   "D": "Freedom from positional encoding"},
  ["B"], "One head might track nearby words, another long-range links, which a single averaged head would blur.")

a(T_VIS, "intermediate", 2, "single_choice",
  "In an attention diagram, what does a thicker line between two tokens mean?",
  {"A": "A larger attention weight",
   "B": "A longer distance",
   "C": "A shared embedding",
   "D": "A gradient path"},
  ["A"], "Line thickness or opacity is the usual way to draw how much one token attends to another.")

# =========================================================================
# Deep Reinforcement Learning
# =========================================================================

a(T_RL, "basics", 1, "single_choice",
  "What does Q-learning estimate?",
  {"A": "The probability of each action",
   "B": "The expected return of an action in a state",
   "C": "The transition probabilities",
   "D": "The reward function"},
  ["B"], "The policy follows by taking the argmax, so no model of the environment is needed.")

a(T_RL, "intermediate", 2, "single_choice",
  "What is the difference between exploration and exploitation?",
  {"A": "Exploitation takes the best known action, exploration tries others",
   "B": "Exploitation is for training, exploration for testing",
   "C": "Exploration maximises immediate reward",
   "D": "They mean the same thing"},
  ["A"], "A purely exploitative agent can settle on a decent action and never find a better one.")

a(T_RL, "basics", 1, "single_choice",
  "What does epsilon-greedy do?",
  {"A": "Always picks the best-valued action",
   "B": "Picks randomly with probability epsilon, greedily otherwise",
   "C": "Picks in proportion to value",
   "D": "Explores only in episode one"},
  ["B"], "Epsilon is usually annealed so the agent explores early and exploits later.")

a(T_RL, "advanced", 3, "single_choice",
  "Why does DQN keep a replay buffer?",
  {"A": "To cut the memory the agent needs while it is learning",
   "B": "Consecutive transitions are correlated, and sampling breaks that up",
   "C": "To make the reward signal differentiable end to end",
   "D": "To remove the need for a separate target network"},
  ["B"], "It also lets each transition be reused, which matters when interaction is expensive.")

a(T_RL, "advanced", 3, "single_choice",
  "What is the target network in DQN for?",
  {"A": "Choosing actions",
   "B": "Holding the bootstrap target still between updates",
   "C": "Computing rewards",
   "D": "Replacing the replay buffer"},
  ["B"], "Bootstrapping from a network that changes every step means chasing a moving target.")

a(T_RL, "intermediate", 2, "single_choice",
  "What does the discount factor do?",
  {"A": "Rescales every reward into the range 0 to 1 before use",
   "B": "Weights near rewards above distant ones and keeps the return finite",
   "C": "Sets how large a step each value update takes",
   "D": "Decides how often the agent picks a random action"},
  ["B"], "Close to 1 makes the agent far-sighted, small values make it short-sighted.")

a(T_RL, "advanced", 3, "single_choice",
  "Which claim about reinforcement learning is wrong?",
  {"A": "A good policy maximises expected future return",
   "B": "Temporal difference learning needs the environment dynamics",
   "C": "Q-learning is off-policy",
   "D": "Bellman equations are solvable exactly for small problems"},
  ["B"], "Temporal difference learning is model-free and bootstraps from sampled transitions.")

a(T_RL, "advanced", 3, "single_choice",
  "What do actor-critic methods combine?",
  {"A": "Two value functions",
   "B": "A policy that acts with a value function that judges",
   "C": "Supervised and unsupervised learning",
   "D": "Two environments"},
  ["B"], "The critic gives the actor a lower-variance signal than the raw return would.")

# =========================================================================
# Segmentation
# =========================================================================

a(T_SEG, "basics", 1, "single_choice",
  "What does semantic segmentation produce?",
  {"A": "A class label for every pixel",
   "B": "A box around each object",
   "C": "One label for the image",
   "D": "A separate mask per object"},
  ["A"], "It does not tell two objects of the same class apart. That is instance segmentation.")

a(T_SEG, "intermediate", 2, "single_choice",
  "How does instance segmentation differ from semantic segmentation?",
  {"A": "It works only on grayscale",
   "B": "It separates individual objects of the same class",
   "C": "It uses no convolutions",
   "D": "It only outputs boxes"},
  ["B"], "Two touching cars become one region under semantic segmentation but two masks under instance.")

a(T_SEG, "advanced", 3, "single_choice",
  "You need to count people in a room. Which task fits?",
  {"A": "Semantic segmentation",
   "B": "Object detection",
   "C": "Image classification",
   "D": "Denoising"},
  ["B"], "Segmentation merges everyone into one region, so overlapping people cannot be counted.")

a(T_SEG, "intermediate", 2, "single_choice",
  "Which metric works for segmentation but not plain classification?",
  {"A": "Accuracy",
   "B": "Intersection over Union",
   "C": "Cross entropy",
   "D": "Precision"},
  ["B"], "IoU and Dice compare regions, which only means something when a prediction has area.")

a(T_SEG, "intermediate", 2, "single_choice",
  "What defines U-Net?",
  {"A": "It has no downsampling",
   "B": "Skip connections from the encoder to the decoder",
   "C": "Only dense layers",
   "D": "No training needed"},
  ["B"], "Without them the decoder knows roughly where an object is but not where its edge is.")

a(T_SEG, "advanced", 3, "single_choice",
  "What does a fully convolutional network replace to give a dense output?",
  {"A": "The pooling layers",
   "B": "The dense layers",
   "C": "The activations",
   "D": "The loss"},
  ["B"], "Dense layers fix the input size and throw away spatial layout.")

a(T_SEG, "advanced", 3, "multiple_choice",
  "Why is classifying each pixel separately with dense layers a poor plan? (Select all that apply)",
  {"A": "It throws away context around the pixel",
   "B": "The parameter count explodes",
   "C": "It loses weight sharing across positions",
   "D": "It cannot handle more than two classes"},
  ["A", "B", "C"], "The class count is not the obstacle. The lost context and sharing are.")

a(T_SEG, "intermediate", 2, "single_choice",
  "Can a segmentation mask be turned into a bounding box?",
  {"A": "No, they are incompatible",
   "B": "Yes, by taking the extent of the region",
   "C": "Only for convex shapes",
   "D": "Only if it is binary"},
  ["B"], "It works one way only, which is why masks are the more expensive annotation.")

a(T_SEG, "intermediate", 2, "single_choice",
  "What does panoptic segmentation combine?",
  {"A": "A classification head with a regression head for box corners",
   "B": "Semantic labels for regions with instance masks for objects",
   "C": "Two separate architectures whose outputs are averaged",
   "D": "The training and inference passes into a single network"},
  ["B"], "Sky and road are handled semantically, cars and people get their own masks.")

# =========================================================================
# Top-up: thin chapters and basics-level questions, so every chapter has
# enough depth and a mixed paper can hold its 45/35/20 split.
# =========================================================================

a(T_INTRO, "basics", 1, "single_choice",
  "What is a training sample made of in supervised learning?",
  {"A": "An input paired with its target",
   "B": "An input with no target attached",
   "C": "A target with no matching input",
   "D": "A batch of inputs sharing a target"},
  ["A"], "Without the target there is nothing to compute a loss against.")

a(T_INTRO, "basics", 1, "single_choice",
  "What is an activation function for?",
  {"A": "Scaling the learning rate",
   "B": "Adding non-linearity between layers",
   "C": "Normalising the input",
   "D": "Choosing the batch size"},
  ["B"], "Without one, stacking layers gains you nothing.")

a(T_INTRO, "basics", 1, "single_choice",
  "What is a hyperparameter?",
  {"A": "A weight the optimizer adjusts during training",
   "B": "A setting chosen before training, like the learning rate",
   "C": "The value the loss function returns each step",
   "D": "A gradient computed during the backward pass"},
  ["B"], "Weights are learned, hyperparameters are picked by you or by a search.")

a(T_INTRO, "intermediate", 2, "single_choice",
  "Your training and validation losses are both high and close together. What is going on?",
  {"A": "Overfitting",
   "B": "Underfitting",
   "C": "Data leakage",
   "D": "The learning rate is too small only"},
  ["B"], "Overfitting shows as a gap between the two. Both high means the model is not fitting at all yet.")

a(T_INTRO, "basics", 1, "single_choice",
  "What is a mini-batch?",
  {"A": "A small subset of the training set used for one update",
   "B": "A network with fewer layers than the full model",
   "C": "A shortened training run used to check the setup",
   "D": "A reduced set of classes used for a quick test"},
  ["A"], "It trades gradient accuracy for many more updates per epoch.")

a(T_INTRO, "intermediate", 2, "single_choice",
  "You get near-perfect validation accuracy on the first epoch. What should you check?",
  {"A": "Whether the learning rate is too high",
   "B": "Whether training data leaked into validation",
   "C": "Whether the batch size is too small",
   "D": "Whether dropout is on"},
  ["B"], "Results that look too good usually mean the split is broken, not that the model is brilliant.")

a(T_INTRO, "intermediate", 2, "single_choice",
  "What is the bias-variance trade-off about?",
  {"A": "Speed against memory",
   "B": "Systematic error against sensitivity to the training set",
   "C": "Depth against width",
   "D": "Training against inference"},
  ["B"], "Simple models err systematically, flexible ones swing with whichever data they saw.")

a(T_NN, "basics", 1, "single_choice",
  "What does a layer's weight matrix do to its input?",
  {"A": "Applies a linear map",
   "B": "Sorts the values",
   "C": "Normalises the values",
   "D": "Removes negatives"},
  ["A"], "The bias then shifts it, and the activation adds the non-linearity.")

a(T_NN, "basics", 1, "single_choice",
  "Which layer type has no parameters to learn?",
  {"A": "Fully connected",
   "B": "ReLU",
   "C": "Convolutional",
   "D": "Batch normalisation"},
  ["B"], "Batch normalisation does have a learned scale and shift on top of its statistics.")

a(T_NN, "basics", 1, "single_choice",
  "Why are weights initialised randomly?",
  {"A": "To make runs reproducible",
   "B": "To break symmetry between units",
   "C": "To cut the parameter count",
   "D": "To speed up the forward pass"},
  ["B"], "Identical starting weights leave every unit in a layer learning the same thing.")

a(T_NN, "intermediate", 2, "single_choice",
  "What is Xavier initialisation trying to keep steady?",
  {"A": "The learning rate",
   "B": "The variance of the signal through the layers",
   "C": "The number of active units",
   "D": "The loss value"},
  ["B"], "Shrink it and the signal dies out, grow it and the activations explode.")

a(T_NN, "intermediate", 2, "single_choice",
  "Why does He initialisation use a factor of 2 where Xavier does not?",
  {"A": "It assumes ReLU, which discards half the signal",
   "B": "It assumes mini-batches",
   "C": "It assumes a bias term",
   "D": "It assumes Adam"},
  ["A"], "Doubling the initial variance makes up for what the ReLU cuts away.")

a(T_LO, "basics", 1, "single_choice",
  "What does an optimizer need besides the current weights?",
  {"A": "The gradient of the loss for those weights",
   "B": "The full training set it is fitting to",
   "C": "The score the model reached on validation",
   "D": "The layer structure of the whole network"},
  ["A"], "That separation is what lets one optimizer serve any layer type.")

a(T_LO, "basics", 1, "single_choice",
  "What is a gradient?",
  {"A": "The direction of steepest increase of the loss",
   "B": "The value the loss function currently takes",
   "C": "The step size used when updating the weights",
   "D": "The current numerical value of the weight"},
  ["A"], "Which is why descent moves in the opposite direction.")

a(T_CNN, "basics", 1, "single_choice",
  "What is the output range of a sigmoid?",
  {"A": "0 to 1",
   "B": "-1 to 1",
   "C": "0 to infinity",
   "D": "-infinity to infinity"},
  ["A"], "Which is why it can stand in for a probability. Tanh covers -1 to 1.")

a(T_CNN, "basics", 1, "single_choice",
  "What is the output range of tanh?",
  {"A": "0 to 1",
   "B": "-1 to 1",
   "C": "0 to infinity",
   "D": "-infinity to infinity"},
  ["B"], "Being zero-centred is one reason it is often preferred to sigmoid inside a network.")

a(T_CNN, "basics", 1, "single_choice",
  "How many channels does pooling return from a 64 channel input?",
  {"A": "1",
   "B": "32",
   "C": "64",
   "D": "128"},
  ["C"], "Pooling works inside each channel, so only the spatial size changes.")

a(T_CNN, "basics", 1, "single_choice",
  "What does same padding with stride 1 achieve?",
  {"A": "The output keeps the input size",
   "B": "The output shrinks",
   "C": "The channels double",
   "D": "The kernel halves"},
  ["A"], "Zero padding replaces the border pixels the kernel would otherwise cost you.")

a(T_REG, "basics", 1, "single_choice",
  "What does dropout do during training?",
  {"A": "Deletes units permanently",
   "B": "Switches off a random subset each iteration",
   "C": "Lowers the learning rate",
   "D": "Normalises activations"},
  ["B"], "A different subset each time, so the network behaves like an ensemble of thinner ones.")

a(T_REG, "basics", 1, "single_choice",
  "Which penalty tends to produce sparse weights?",
  {"A": "L1",
   "B": "L2",
   "C": "Dropout",
   "D": "Batch normalisation"},
  ["A"], "Its gradient has constant size, so it pushes small weights all the way to zero.")

a(T_RNN, "basics", 1, "single_choice",
  "What problem do long sequences cause when training recurrent networks?",
  {"A": "Gradients vanish or explode",
   "B": "The batch size must shrink",
   "C": "The loss becomes non-differentiable",
   "D": "The hidden state disappears"},
  ["A"], "Repeated multiplication through time either shrinks or amplifies the signal.")

a(T_RNN, "basics", 1, "single_choice",
  "What is truncated backpropagation through time?",
  {"A": "Limiting how many steps back the gradient is traced",
   "B": "Dropping the hidden state",
   "C": "Training on shorter sequences only",
   "D": "Removing the recurrence"},
  ["A"], "It bounds the memory and compute a long sequence would otherwise need.")

a(T_UNS, "basics", 1, "single_choice",
  "What kind of data does unsupervised learning work with?",
  {"A": "Unlabelled data",
   "B": "Labelled data only",
   "C": "Image data only",
   "D": "Time series only"},
  ["A"], "The objective comes from the data itself rather than from targets.")

a(T_UNS, "basics", 1, "single_choice",
  "What are the two halves of an autoencoder called?",
  {"A": "Generator and discriminator",
   "B": "Encoder and decoder",
   "C": "Actor and critic",
   "D": "Backbone and head"},
  ["B"], "The encoder compresses to the code, the decoder rebuilds from it.")

a(T_UNS, "intermediate", 2, "single_choice",
  "What does the generator in a GAN take as input?",
  {"A": "Real training images",
   "B": "A random noise vector",
   "C": "Class labels only",
   "D": "The discriminator's weights"},
  ["B"], "It learns to map that noise onto something that passes for real data.")

a(T_UNS, "intermediate", 2, "single_choice",
  "Why is GAN training often unstable?",
  {"A": "The two networks chase each other rather than a fixed target",
   "B": "The loss is not differentiable",
   "C": "There are too few parameters",
   "D": "The data is unlabelled"},
  ["A"], "Each network's objective shifts as the other improves, so there is no fixed thing to converge to.")

a(T_UNS, "intermediate", 2, "single_choice",
  "How would you pick k for k-means when it is not known?",
  {"A": "Always use k equal to 2",
   "B": "Try several and look for a knee in the error curve",
   "C": "Use the number of features",
   "D": "It cannot be chosen"},
  ["B"], "The elbow method and silhouette scores are the usual heuristics.")

a(T_UNS, "advanced", 3, "single_choice",
  "A linear autoencoder trained with squared error learns a subspace. Which one?",
  {"A": "A random subspace",
   "B": "The same one PCA finds",
   "C": "The null space of the data",
   "D": "The full input space"},
  ["B"], "Without a non-linearity it can do no better than the leading principal components.")

a(T_UNS, "intermediate", 2, "single_choice",
  "What does the latent space of a generative model let you do?",
  {"A": "Sample new data by drawing a code and decoding it",
   "B": "Speed up training",
   "C": "Label the training data",
   "D": "Remove the decoder"},
  ["A"], "Which is why a VAE bothers to shape that space towards a known prior.")

a(T_VIS, "basics", 1, "single_choice",
  "What does occlusion testing involve?",
  {"A": "Blocking part of the image and watching the prediction change",
   "B": "Removing a layer and measuring how much accuracy drops",
   "C": "Dropping training samples to see which ones mattered",
   "D": "Hiding the labels and checking the model still agrees"},
  ["A"], "Wherever covering the image hurts the score most is where the model was looking.")

a(T_VIS, "basics", 1, "single_choice",
  "What do first-layer convolution kernels typically learn on natural images?",
  {"A": "Edges and simple colour blobs",
   "B": "Whole objects such as faces or cars",
   "C": "The class labels used in training",
   "D": "Patterns with no visible structure"},
  ["A"], "Later layers combine these into textures, parts and eventually objects.")

a(T_VIS, "intermediate", 2, "single_choice",
  "Why do people visualise networks at all?",
  {"A": "To speed up inference",
   "B": "To check the model is using sensible evidence",
   "C": "To reduce parameters",
   "D": "To pick the batch size"},
  ["B"], "A model can be right for the wrong reason, and visualisation is how you catch that.")

a(T_VIS, "advanced", 3, "single_choice",
  "Attention weights across a sequence must satisfy which property?",
  {"A": "They sum to one over the attended positions",
   "B": "They are all equal",
   "C": "They are binary",
   "D": "They are negative"},
  ["A"], "They come from a softmax, so they form a distribution over positions.")

a(T_RL, "basics", 1, "single_choice",
  "What does an agent receive from the environment after acting?",
  {"A": "A new state and a reward",
   "B": "A gradient for its parameters",
   "C": "A label for the correct action",
   "D": "A batch of training examples"},
  ["A"], "That loop of state, action, reward is the whole setting.")

a(T_RL, "basics", 1, "single_choice",
  "What is a policy?",
  {"A": "A rule mapping states to actions",
   "B": "The function giving reward for each step",
   "C": "The model of how the environment moves",
   "D": "The factor discounting distant rewards"},
  ["A"], "Learning a good one is the point of the whole exercise.")

a(T_RL, "intermediate", 2, "single_choice",
  "What makes Q-learning off-policy?",
  {"A": "It learns about the greedy policy while acting differently",
   "B": "It needs no reward",
   "C": "It cannot use a neural network",
   "D": "It works only offline"},
  ["A"], "Which is what lets it learn from a replay buffer of older behaviour.")

a(T_RL, "intermediate", 2, "single_choice",
  "Why is reinforcement learning harder than supervised learning?",
  {"A": "The reward may be delayed and there is no labelled correct action",
   "B": "The networks involved are much larger than in supervised work",
   "C": "The observations are always images, which are costly to process",
   "D": "The objective cannot be optimised with gradient methods"},
  ["A"], "Credit assignment across a long sequence of actions is the core difficulty.")

a(T_ARCH, "basics", 1, "single_choice",
  "What does depth mean in a network?",
  {"A": "The number of layers between input and output",
   "B": "The number of channels",
   "C": "The batch size",
   "D": "The number of classes"},
  ["A"], "Width is the number of units or channels in a layer.")

a(T_ARCH, "intermediate", 2, "single_choice",
  "Why do modern architectures often drop large dense layers at the end?",
  {"A": "They hold most of the parameters and tie the model to one input size",
   "B": "They cannot be trained by backpropagation like other layers",
   "C": "They produce no usable gradient for the layers beneath them",
   "D": "They are far slower to compute than an equivalent convolution"},
  ["A"], "Global average pooling replaces them and removes both problems at once.")

a(T_ARCH, "intermediate", 2, "single_choice",
  "What is a backbone in a vision model?",
  {"A": "The feature extractor shared across tasks",
   "B": "The loss function",
   "C": "The optimizer",
   "D": "The data loader"},
  ["A"], "Detection and segmentation models bolt task-specific heads onto a common backbone.")

a(T_SEG, "basics", 1, "single_choice",
  "What does object detection output?",
  {"A": "A box and a class for each object found",
   "B": "A class label for every pixel in the image",
   "C": "A single class label for the whole image",
   "D": "A reconstruction of the original image"},
  ["A"], "Because it gives one entry per object, its output can be counted.")

a(T_SEG, "basics", 1, "single_choice",
  "What does IoU measure?",
  {"A": "Overlap between the predicted and true regions",
   "B": "The value the loss function reached at the end",
   "C": "How many distinct classes the model can output",
   "D": "How long the model took to finish training"},
  ["A"], "Intersection divided by union, so 1 means a perfect match.")

a(T_SEG, "intermediate", 2, "single_choice",
  "Why is the encoder-decoder shape common in segmentation?",
  {"A": "The encoder builds context, the decoder restores resolution",
   "B": "It roughly halves the parameters a flat network would need",
   "C": "It removes the need for pixel-level labels during training",
   "D": "It trains considerably faster than a flat convolutional stack"},
  ["A"], "Downsampling widens the receptive field, and the decoder puts the detail back.")

a(T_CP, "basics", 1, "single_choice",
  "What does a confusion matrix show?",
  {"A": "Predicted classes against the true ones",
   "B": "How the loss changed over training time",
   "C": "The distribution of the learned weights",
   "D": "The size of the gradients in each layer"},
  ["A"], "It exposes which classes get mistaken for which, unlike a single accuracy number.")

a(T_CP, "basics", 1, "single_choice",
  "What is precision?",
  {"A": "Correct positives out of all predicted positives",
   "B": "Correct positives out of all actual positives",
   "C": "All correct predictions over the whole test set",
   "D": "The area beneath the receiver operating curve"},
  ["A"], "Recall is the other one, correct positives out of all actual positives.")

a(T_CP, "basics", 1, "single_choice",
  "What is transfer learning?",
  {"A": "Reusing weights from one task on another",
   "B": "Moving a trained model to another machine",
   "C": "Sharing training data between two research teams",
   "D": "Converting a model into a different file format"},
  ["A"], "Most useful when the new task has too little data to learn features from scratch.")

a(T_CP, "intermediate", 2, "single_choice",
  "When fine-tuning a pretrained network on a small dataset, what is common practice?",
  {"A": "Freeze the early layers and train the later ones",
   "B": "Retrain everything at a high learning rate",
   "C": "Replace every layer",
   "D": "Train only the input layer"},
  ["A"], "Early features are generic and a small dataset would only damage them.")

# =========================================================================
# Pattern top-up. The papers lean heavily on three shapes that were still
# under-represented above: "which statements are true", "which is NOT / is
# FALSE", and "you did X and saw Y". This batch fills that gap.
# =========================================================================

a(T_NN, "intermediate", 2, "single_choice",
  "Which statement about weight initialisation is FALSE?",
  {"A": "All-zero weights leave every unit with the same gradient",
   "B": "Xavier takes the layer's input size into account",
   "C": "Initialisation matters because the loss surface is convex",
   "D": "A small positive bias can help against dying ReLUs"},
  ["C"], "Deep network losses are not convex. That is part of why the starting point matters.")

a(T_CNN, "intermediate", 2, "single_choice",
  "Which of these is NOT a reason convolutions suit images?",
  {"A": "Nearby pixels are related",
   "B": "The same pattern can appear anywhere",
   "C": "Weight sharing keeps the parameter count down",
   "D": "Images always have exactly three channels"},
  ["D"], "Grayscale, depth maps and multispectral images all work fine with convolutions.")

a(T_CNN, "intermediate", 2, "multiple_choice",
  "Which statements about activation functions are true? (Select all that apply)",
  {"A": "Sigmoid outputs sit between 0 and 1",
   "B": "Tanh is zero-centred, unlike sigmoid",
   "C": "ReLU can leave units permanently inactive",
   "D": "Softmax is normally used on hidden layers"},
  ["A", "B", "C"], "Softmax belongs at the output of a classifier, where a distribution over classes is wanted.")

a(T_LO, "intermediate", 2, "multiple_choice",
  "Which statements about the learning rate are true? (Select all that apply)",
  {"A": "Too large a rate can make the loss diverge",
   "B": "Too small a rate makes training slow",
   "C": "Decaying it late in training helps the model settle",
   "D": "Adam removes the need to set it at all"},
  ["A", "B", "C"], "Adam adapts the step per parameter but still takes a base learning rate.")

a(T_LO, "intermediate", 2, "single_choice",
  "Which statement about loss functions is FALSE?",
  {"A": "Cross entropy pairs naturally with a softmax output",
   "B": "Squared error suits regression with Gaussian noise",
   "C": "The loss must return one number per mini-batch",
   "D": "Any loss works with any output activation"},
  ["D"], "Cross entropy needs values in a valid probability range, which is why the output activation is not a free choice.")

a(T_REG, "intermediate", 2, "single_choice",
  "Which statement about dropout is FALSE?",
  {"A": "It drops a different random subset each iteration",
   "B": "It is switched off during inference",
   "C": "It fixes vanishing gradients",
   "D": "It discourages units from co-adapting"},
  ["C"], "Dropout targets overfitting. Vanishing gradients need better activations or skip connections.")

a(T_REG, "intermediate", 2, "multiple_choice",
  "Which statements about batch normalisation are true? (Select all that apply)",
  {"A": "It uses batch statistics during training",
   "B": "It uses stored running statistics at inference",
   "C": "It has a learned scale and shift",
   "D": "It replaces the need for any activation function"},
  ["A", "B", "C"], "Normalisation is linear, so a non-linearity is still needed afterwards.")

a(T_RNN, "intermediate", 2, "single_choice",
  "Which statement about recurrent networks is FALSE?",
  {"A": "The same weights are reused at every time step",
   "B": "The hidden state carries information forward",
   "C": "Every time step is processed in parallel",
   "D": "Long sequences worsen gradient problems"},
  ["C"], "Each step needs the previous hidden state, so the recurrence is inherently sequential.")

a(T_RNN, "intermediate", 2, "multiple_choice",
  "Which statements about LSTMs are true? (Select all that apply)",
  {"A": "Gates control what enters and leaves the cell state",
   "B": "The cell state is updated additively",
   "C": "They have more parameters than a simple cell",
   "D": "They avoid backpropagation through time"},
  ["A", "B", "C"], "They are still trained with backpropagation through time. The gates change how gradients flow, not the algorithm.")

a(T_UNS, "intermediate", 2, "single_choice",
  "Which statement about autoencoders is FALSE?",
  {"A": "They are trained without class labels",
   "B": "The bottleneck limits what can be kept",
   "C": "They always need a larger code than input",
   "D": "The decoder rebuilds the input from the code"},
  ["C"], "An overcomplete code is possible but needs an extra constraint, otherwise the model just copies its input.")

a(T_UNS, "intermediate", 2, "multiple_choice",
  "Which statements about GANs are true? (Select all that apply)",
  {"A": "The generator starts from random noise",
   "B": "The discriminator does binary classification",
   "C": "Training is a min-max game",
   "D": "The generator sees the real images directly"},
  ["A", "B", "C"], "The generator only learns through the discriminator's judgement, never from the real images themselves.")

a(T_SEG, "intermediate", 2, "single_choice",
  "Which statement about segmentation is FALSE?",
  {"A": "Semantic segmentation labels every pixel",
   "B": "Instance segmentation separates objects of one class",
   "C": "IoU is a sensible evaluation measure",
   "D": "A mask carries less information than a bounding box"},
  ["D"], "It is the other way round. A mask can be reduced to a box, but not the reverse.")

a(T_CP, "intermediate", 2, "multiple_choice",
  "Which statements about splitting data are true? (Select all that apply)",
  {"A": "Validation guides model choice during development",
   "B": "The test set should be touched once, at the end",
   "C": "Normalisation uses training statistics only",
   "D": "The test set should be used for early stopping"},
  ["A", "B", "C"], "Stopping on the test set would spend the one split meant to give an unbiased final number.")

a(T_RL, "intermediate", 2, "single_choice",
  "Which statement about reinforcement learning is FALSE?",
  {"A": "The agent learns from rewards, not labelled actions",
   "B": "Exploration matters most during training",
   "C": "Rewards can be delayed by many steps",
   "D": "The optimal policy is known in advance"},
  ["D"], "If it were known there would be nothing left to learn.")

a(T_ARCH, "intermediate", 2, "single_choice",
  "Which statement about ResNet is FALSE?",
  {"A": "Skip connections let gradients bypass a block",
   "B": "A block can fall back to the identity",
   "C": "It made very deep networks trainable",
   "D": "It removed the need for any normalisation"},
  ["D"], "ResNet blocks use batch normalisation throughout.")

a(T_INTRO, "intermediate", 2, "single_choice",
  "You double the size of your training set and validation accuracy improves noticeably. What does that suggest?",
  {"A": "The model was mainly limited by data, not capacity",
   "B": "The learning rate was too high",
   "C": "The model is underfitting badly",
   "D": "The validation split is broken"},
  ["A"], "If capacity were the binding constraint, extra data would have made much less difference.")

a(T_NN, "intermediate", 2, "single_choice",
  "You train the same network twice with different random seeds and get noticeably different test scores. What is the most reasonable response?",
  {"A": "Report the average and spread over several runs",
   "B": "Report whichever run scored highest",
   "C": "Fix the seed and never mention it",
   "D": "Conclude the network is broken"},
  ["A"], "A single run tells you as much about the seed as about the model.")

a(T_LO, "intermediate", 2, "single_choice",
  "Your loss drops fast for a few hundred steps then starts climbing steadily. What would you try first?",
  {"A": "Lower the learning rate",
   "B": "Add more layers to the network",
   "C": "Increase the learning rate",
   "D": "Remove the validation set"},
  ["A"], "A loss that falls then rises usually means the steps are too big to settle once it nears a minimum.")

a(T_REG, "intermediate", 2, "single_choice",
  "You add dropout and both training and validation accuracy get worse. What is the likely explanation?",
  {"A": "The model was not overfitting, so the extra noise only hurts",
   "B": "Dropout always lowers accuracy",
   "C": "The learning rate must be raised to compensate",
   "D": "Dropout was applied at inference by mistake"},
  ["A"], "Regularisation costs capacity, which is only worth paying when there is overfitting to fix.")

a(T_CNN, "intermediate", 2, "single_choice",
  "You replace a 5x5 convolution with two stacked 3x3 convolutions and accuracy holds while parameters drop. Why does that work?",
  {"A": "The two layers cover the same receptive field",
   "B": "Smaller kernels always generalise better",
   "C": "The stride compensates for the change",
   "D": "3x3 kernels need no padding"},
  ["A"], "Two 3x3 layers see 5x5 between them, with fewer weights and an extra non-linearity thrown in.")

a(T_CP, "intermediate", 2, "single_choice",
  "Your model does well on validation but poorly once deployed. Which explanation is most plausible?",
  {"A": "Live data differs from the data the splits came from",
   "B": "The model has too few parameters",
   "C": "The learning rate was too low",
   "D": "The batch size was too small"},
  ["A"], "This is dataset shift. Validation only tells you about the distribution it was drawn from.")

a(T_RNN, "intermediate", 2, "single_choice",
  "Your recurrent model handles short sequences well but fails on long ones. What is the most likely cause?",
  {"A": "Gradients vanish over the longer span",
   "B": "The batch size is too large",
   "C": "The hidden state is too small to store the input",
   "D": "The loss function is wrong"},
  ["A"], "Gating or attention are the usual answers when longer contexts stop working.")

a(T_UNS, "intermediate", 2, "single_choice",
  "Your GAN produces convincing images but they all look nearly the same. What has happened?",
  {"A": "Mode collapse",
   "B": "Vanishing gradients",
   "C": "Overfitting to the validation set",
   "D": "The discriminator stopped training"},
  ["A"], "The generator found a few outputs that always fool the discriminator and stopped exploring.")

a(T_CP, "intermediate", 2, "single_choice",
  "You get 97% accuracy on a dataset where 97% of samples are negative. What should you conclude?",
  {"A": "The model may be predicting the majority class every time",
   "B": "The model has learned the task well",
   "C": "The dataset is too small",
   "D": "The learning rate is correct"},
  ["A"], "Check precision, recall or the confusion matrix before believing an accuracy figure on imbalanced data.")

a(T_SEG, "intermediate", 2, "single_choice",
  "Your segmentation model finds objects in roughly the right place but the edges are badly blurred. What usually helps?",
  {"A": "Skip connections carrying fine detail to the decoder",
   "B": "A larger batch size",
   "C": "A smaller learning rate",
   "D": "Removing the encoder"},
  ["A"], "Downsampling throws away the detail that sharp boundaries need, and skip connections put it back.")

a(T_ARCH, "intermediate", 2, "single_choice",
  "You make a plain network deeper and the training error rises. What does that tell you?",
  {"A": "The deeper network is harder to optimise",
   "B": "The deeper network is overfitting",
   "C": "The data is mislabelled",
   "D": "The learning rate is too low"},
  ["A"], "Overfitting would lower the training error. This is the degradation problem residual connections were built for.")

a(T_VIS, "intermediate", 2, "single_choice",
  "A saliency map shows your classifier attending to the background rather than the animal. What does that suggest?",
  {"A": "The model has latched onto a confound",
   "B": "The saliency method is broken",
   "C": "The model needs more layers",
   "D": "The learning rate is too high"},
  ["A"], "Its accuracy is real but will not survive backgrounds that break the correlation.")

a(T_NN, "intermediate", 2, "single_choice",
  "You remove all activation functions from a ten-layer network and accuracy collapses to that of a linear model. Why?",
  {"A": "The whole stack collapses into a single linear map",
   "B": "The gradients vanish",
   "C": "The weights become zero",
   "D": "The loss stops being differentiable"},
  ["A"], "Without a non-linearity anywhere, ten layers express exactly what one can.")

a(T_LO, "intermediate", 2, "single_choice",
  "You switch from batch size 256 to batch size 8 and keep everything else fixed. What should you expect?",
  {"A": "A noisier loss curve and more updates per epoch",
   "B": "A smoother loss curve",
   "C": "Fewer updates per epoch",
   "D": "No change in behaviour"},
  ["A"], "Smaller batches give a noisier gradient estimate, and the learning rate often needs adjusting too.")

a(T_REG, "intermediate", 2, "single_choice",
  "You apply batch normalisation and find you can raise the learning rate considerably. Why?",
  {"A": "Layer inputs stay on a consistent scale",
   "B": "The gradients become larger",
   "C": "The parameter count drops",
   "D": "Dropout is no longer needed"},
  ["A"], "A big step in one layer no longer throws off everything above it.")
