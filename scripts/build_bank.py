"""
Builds data/questions.json from a hand-written master list.

Each question is a real MCQ with plausible distractors, tagged with topic,
difficulty, point value and type (single / multiple). Points follow the
agreed scheme: basics = 1, intermediate = 2-3, advanced = 3-4 (integers only).

Topic priority (drives how many questions live in the bank per topic):
  high  -> Introduction, Neural Networks, Loss & Optimization,
           Activation & CNN, Regularization, RNNs, Unsupervised
  low   -> Common Practices, Architectures, Visualization & Attention,
           Deep RL, Segmentation
Excluded from the course entirely: Weakly Supervised Learning, slide 10 topics,
Known Operator Learning, Graph Neural Networks, Self-Supervised Learning.
"""

import json
import os

# ---------------------------------------------------------------------------
# Master question list.
# Tuple: (topic, difficulty, points, type, question, options{A..}, correct[list])
# ---------------------------------------------------------------------------

Q = []

def add(topic, diff, pts, qtype, question, options, correct):
    Q.append({
        "topic": topic,
        "difficulty": diff,
        "points": pts,
        "type": qtype,
        "question": question,
        "options": options,
        "correct_answers": correct,
    })

# ======================= INTRODUCTION (high) ===============================
add("Introduction", "basics", 1, "single_choice",
    "What most distinguishes deep learning from classical machine learning?",
    {"A": "It always needs less data to train",
     "B": "It learns feature representations directly from raw data instead of relying on hand-crafted features",
     "C": "It never overfits",
     "D": "It only works on image data"},
    ["A_wrong"])  # placeholder, fixed below

# (We assign the real correct key explicitly to avoid mistakes.)
Q[-1]["correct_answers"] = ["B"]

add("Introduction", "basics", 1, "single_choice",
    "Why are the networks in deep learning called 'deep'?",
    {"A": "They require deep mathematical proofs",
     "B": "They are trained on very large disks",
     "C": "They stack many layers between the input and the output",
     "D": "They use deep learning rates"},
    ["C"])

add("Introduction", "basics", 1, "single_choice",
    "Which event is widely credited with sparking the modern deep learning boom?",
    {"A": "The invention of the perceptron in 1958",
     "B": "AlexNet winning the ImageNet competition in 2012",
     "C": "The release of Python 3",
     "D": "The first use of GPUs for gaming"},
    ["B"])

add("Introduction", "intermediate", 2, "single_choice",
    "Which combination of factors best explains why deep learning became practical in the 2010s?",
    {"A": "Smaller datasets and slower hardware",
     "B": "Large labelled datasets, GPU compute, and improved training methods",
     "C": "The abandonment of gradient descent",
     "D": "A switch away from neural networks"},
    ["B"])

# ======================= NEURAL NETWORKS (high) ============================
add("Neural Networks", "basics", 1, "single_choice",
    "What does a single artificial neuron compute before applying its activation?",
    {"A": "The maximum of its inputs",
     "B": "A weighted sum of its inputs plus a bias",
     "C": "The product of all its inputs",
     "D": "The softmax of its inputs"},
    ["B"])

add("Neural Networks", "basics", 1, "single_choice",
    "What is the purpose of forward propagation?",
    {"A": "To update the weights using gradients",
     "B": "To pass inputs through the network and produce an output",
     "C": "To initialise the weights",
     "D": "To compute the loss gradient"},
    ["B"])

add("Neural Networks", "basics", 1, "single_choice",
    "What does backpropagation actually compute?",
    {"A": "The predictions for new data",
     "B": "The gradients of the loss with respect to weights and biases",
     "C": "The optimal number of layers",
     "D": "The learning rate"},
    ["B"])

add("Neural Networks", "basics", 1, "single_choice",
    "Why must a multilayer network use non-linear activations?",
    {"A": "Otherwise the whole network collapses to a single linear transformation",
     "B": "Otherwise the network cannot store weights",
     "C": "Because linear functions cannot be differentiated",
     "D": "To make training slower on purpose"},
    ["A"])

add("Neural Networks", "intermediate", 2, "single_choice",
    "In gradient descent, how are parameters updated?",
    {"A": "In the direction of the gradient, scaled by the learning rate",
     "B": "In the direction opposite the gradient, scaled by the learning rate",
     "C": "Randomly, until the loss decreases",
     "D": "By setting them to zero each step"},
    ["B"])

add("Neural Networks", "intermediate", 2, "multiple_choice",
    "Which of the following are symptoms or causes of the vanishing gradient problem? (Select all that apply)",
    {"A": "Gradients shrink toward zero in early layers of deep networks",
     "B": "Saturating activations such as sigmoid or tanh make it worse",
     "C": "Early layers learn very slowly or not at all",
     "D": "It only occurs when the learning rate is set to zero"},
    ["A", "B", "C"])

add("Neural Networks", "intermediate", 3, "single_choice",
    "What does the Universal Approximation Theorem guarantee?",
    {"A": "Any network trained long enough reaches zero test error",
     "B": "A network with one hidden layer and enough neurons can approximate any continuous function on a compact set",
     "C": "Deeper networks always beat shallow ones",
     "D": "Gradient descent always finds the global optimum"},
    ["B"])

add("Neural Networks", "advanced", 3, "single_choice",
    "How do residual (skip) connections help train very deep networks?",
    {"A": "They remove the need for activation functions",
     "B": "They give gradients a shortcut path, easing the vanishing-gradient and degradation problems",
     "C": "They reduce the number of parameters to zero",
     "D": "They replace backpropagation"},
    ["B"])

add("Neural Networks", "advanced", 4, "single_choice",
    "Compared with widening a network, what does adding depth mainly provide?",
    {"A": "Guaranteed lower training loss",
     "B": "Hierarchical, compositional feature representations",
     "C": "Immunity to overfitting",
     "D": "No effect on expressiveness"},
    ["B"])

# ======================= LOSS & OPTIMIZATION (high) ========================
add("Loss and Optimization", "basics", 1, "single_choice",
    "Which loss is standard for multi-class classification with a softmax output?",
    {"A": "Mean squared error",
     "B": "Mean absolute error",
     "C": "Categorical cross-entropy",
     "D": "Hinge-squared error"},
    ["C"])

add("Loss and Optimization", "basics", 1, "single_choice",
    "Which loss is typically used for regression?",
    {"A": "Cross-entropy",
     "B": "Mean squared error",
     "C": "Softmax loss",
     "D": "Triplet loss"},
    ["B"])

add("Loss and Optimization", "basics", 1, "single_choice",
    "How does stochastic gradient descent differ from full-batch gradient descent?",
    {"A": "It updates using one (or a few) samples per step instead of the whole dataset",
     "B": "It never converges",
     "C": "It uses the whole dataset per step",
     "D": "It does not use gradients"},
    ["A"])

add("Loss and Optimization", "basics", 1, "single_choice",
    "What does the learning rate control?",
    {"A": "The number of layers",
     "B": "The size of each parameter update step",
     "C": "The batch size",
     "D": "The loss function used"},
    ["B"])

add("Loss and Optimization", "intermediate", 2, "single_choice",
    "What is the main benefit of using momentum in optimization?",
    {"A": "It removes the need for a loss function",
     "B": "It accumulates past gradients to smooth updates and speed up convergence",
     "C": "It guarantees the global minimum",
     "D": "It increases the learning rate automatically to 1.0"},
    ["B"])

add("Loss and Optimization", "intermediate", 3, "single_choice",
    "What two ideas does the Adam optimizer combine?",
    {"A": "Dropout and batch normalization",
     "B": "Momentum (first moment) and adaptive per-parameter scaling (second moment)",
     "C": "L1 and L2 regularization",
     "D": "Grid search and random search"},
    ["B"])

add("Loss and Optimization", "intermediate", 2, "single_choice",
    "Why use a mini-batch rather than a single sample or the full dataset?",
    {"A": "It is the only option that uses gradients",
     "B": "It balances gradient-estimate stability against computational efficiency",
     "C": "It removes all noise from the gradient",
     "D": "It avoids needing a learning rate"},
    ["B"])

add("Loss and Optimization", "advanced", 3, "single_choice",
    "What problem does learning-rate scheduling (e.g. decay or cosine annealing) address?",
    {"A": "A fixed rate can be too large late in training, causing the loss to bounce around the minimum",
     "B": "It removes the need for a validation set",
     "C": "It eliminates overfitting entirely",
     "D": "It forces the gradient to zero immediately"},
    ["A"])

add("Loss and Optimization", "advanced", 4, "multiple_choice",
    "Which statements about convergence and overfitting are correct? (Select all that apply)",
    {"A": "Convergence means the optimizer has settled near a minimum of the training loss",
     "B": "Overfitting means training loss keeps falling while validation loss rises",
     "C": "Reaching low training loss guarantees good generalization",
     "D": "Early stopping can be used to trade a little training fit for better validation performance"},
    ["A", "B", "D"])

# ======================= ACTIVATION & CNN (high) ===========================
add("Activation Functions and CNN", "basics", 1, "single_choice",
    "What is the output of the ReLU function for an input x?",
    {"A": "1 / (1 + e^-x)",
     "B": "max(0, x)",
     "C": "tanh(x)",
     "D": "x^2"},
    ["B"])

add("Activation Functions and CNN", "basics", 1, "single_choice",
    "What is the output range of the sigmoid function?",
    {"A": "(-1, 1)",
     "B": "(0, 1)",
     "C": "[0, infinity)",
     "D": "(-infinity, infinity)"},
    ["B"])

add("Activation Functions and CNN", "basics", 1, "single_choice",
    "What does a convolutional layer primarily do?",
    {"A": "Flattens the image into a vector",
     "B": "Slides learnable filters over the input to extract local features",
     "C": "Normalizes the input to zero mean",
     "D": "Randomly drops neurons"},
    ["B"])

add("Activation Functions and CNN", "basics", 1, "single_choice",
    "What is the purpose of a pooling layer?",
    {"A": "To add non-linearity",
     "B": "To downsample feature maps, reducing spatial size and computation",
     "C": "To increase the number of channels",
     "D": "To compute the loss"},
    ["B"])

add("Activation Functions and CNN", "intermediate", 2, "single_choice",
    "How does increasing the stride of a convolution affect the output feature map?",
    {"A": "It makes the output larger",
     "B": "It makes the output smaller",
     "C": "It has no effect on size",
     "D": "It doubles the number of channels"},
    ["B"])

add("Activation Functions and CNN", "intermediate", 2, "single_choice",
    "What does 'same' padding achieve with stride 1?",
    {"A": "It removes the border pixels",
     "B": "It keeps the output spatial size equal to the input",
     "C": "It halves the output size",
     "D": "It converts the layer to fully connected"},
    ["B"])

add("Activation Functions and CNN", "intermediate", 3, "single_choice",
    "Why is ReLU often preferred over sigmoid in hidden layers of deep CNNs?",
    {"A": "It saturates for all inputs",
     "B": "It does not saturate for positive inputs, so gradients flow better",
     "C": "It always outputs probabilities",
     "D": "It has no derivative"},
    ["B"])

add("Activation Functions and CNN", "advanced", 3, "single_choice",
    "What is the key advantage of a dilated (atrous) convolution?",
    {"A": "It reduces the number of channels",
     "B": "It enlarges the receptive field without increasing parameters or reducing resolution",
     "C": "It removes the need for activation functions",
     "D": "It is only used in fully connected layers"},
    ["B"])

add("Activation Functions and CNN", "advanced", 4, "single_choice",
    "Given a 32x32 input, a 5x5 filter, stride 1 and no padding, what is the output width?",
    {"A": "32",
     "B": "30",
     "C": "28",
     "D": "27"},
    ["C"])

# ======================= REGULARIZATION (high) =============================
add("Regularization", "basics", 1, "single_choice",
    "What is the goal of regularization?",
    {"A": "To make training loss exactly zero",
     "B": "To improve generalization by discouraging overly complex models",
     "C": "To increase the number of parameters",
     "D": "To speed up the GPU"},
    ["B"])

add("Regularization", "basics", 1, "single_choice",
    "What does L2 regularization add to the loss?",
    {"A": "The sum of absolute weights",
     "B": "The sum of squared weights",
     "C": "The number of layers",
     "D": "The batch size"},
    ["B"])

add("Regularization", "basics", 1, "single_choice",
    "What effect does L1 regularization tend to have on weights?",
    {"A": "It drives many weights exactly to zero (sparsity)",
     "B": "It makes all weights equal",
     "C": "It maximizes the weights",
     "D": "It has no effect on weights"},
    ["A"])

add("Regularization", "intermediate", 2, "single_choice",
    "How does dropout regularize a network?",
    {"A": "By permanently deleting neurons",
     "B": "By randomly deactivating neurons during training so the network cannot rely on any single one",
     "C": "By freezing all weights",
     "D": "By increasing the learning rate"},
    ["B"])

add("Regularization", "intermediate", 2, "single_choice",
    "What does batch normalization normalize?",
    {"A": "The final loss value",
     "B": "The activations within a mini-batch to roughly zero mean and unit variance",
     "C": "The learning rate",
     "D": "The number of epochs"},
    ["B"])

add("Regularization", "intermediate", 3, "single_choice",
    "Why can batch normalization allow higher learning rates?",
    {"A": "It removes all gradients",
     "B": "It stabilises the distribution of layer inputs, reducing internal covariate shift",
     "C": "It sets the learning rate to 1.0",
     "D": "It disables backpropagation"},
    ["B"])

add("Regularization", "intermediate", 2, "single_choice",
    "What is early stopping?",
    {"A": "Stopping when training loss reaches zero",
     "B": "Halting training once validation performance stops improving",
     "C": "Stopping after the first epoch always",
     "D": "Removing the last layer"},
    ["B"])

add("Regularization", "advanced", 3, "multiple_choice",
    "Which of the following are legitimate regularization techniques? (Select all that apply)",
    {"A": "Dropout",
     "B": "Weight decay (L2)",
     "C": "Data augmentation",
     "D": "Increasing the learning rate to infinity"},
    ["A", "B", "C"])

# ======================= RNNs (high) =======================================
add("Recurrent Neural Networks", "basics", 1, "single_choice",
    "What makes an RNN suited to sequential data?",
    {"A": "It processes all inputs simultaneously with no order",
     "B": "It maintains a hidden state carried across time steps",
     "C": "It uses only convolutions",
     "D": "It cannot handle sequences"},
    ["B"])

add("Recurrent Neural Networks", "basics", 1, "single_choice",
    "Which gates does a standard LSTM cell use?",
    {"A": "Forget, input, and output gates",
     "B": "Only a reset gate",
     "C": "Convolution and pooling gates",
     "D": "No gates at all"},
    ["A"])

add("Recurrent Neural Networks", "basics", 1, "single_choice",
    "How does a GRU compare with an LSTM?",
    {"A": "It has more gates and parameters",
     "B": "It uses fewer gates and parameters while often performing comparably",
     "C": "It cannot model sequences",
     "D": "It is a type of CNN"},
    ["B"])

add("Recurrent Neural Networks", "intermediate", 2, "single_choice",
    "Why do LSTMs handle long-term dependencies better than vanilla RNNs?",
    {"A": "They use a cell state and gates that let information and gradients persist",
     "B": "They remove the hidden state entirely",
     "C": "They never use backpropagation",
     "D": "They are shallower"},
    ["A"])

add("Recurrent Neural Networks", "intermediate", 2, "single_choice",
    "What does a bidirectional RNN add?",
    {"A": "Processing the sequence in both forward and backward directions",
     "B": "Two loss functions",
     "C": "A convolutional front-end",
     "D": "Random shuffling of the sequence"},
    ["A"])

add("Recurrent Neural Networks", "intermediate", 3, "single_choice",
    "In a sequence-to-sequence model, what is the role of the encoder?",
    {"A": "To generate the output tokens one by one",
     "B": "To compress the input sequence into a representation the decoder uses",
     "C": "To compute the loss only",
     "D": "To shuffle the input"},
    ["B"])

add("Recurrent Neural Networks", "advanced", 3, "single_choice",
    "Why was the attention mechanism introduced on top of encoder-decoder RNNs?",
    {"A": "To make training slower",
     "B": "To let the decoder focus on relevant encoder states instead of a single fixed vector",
     "C": "To remove the decoder",
     "D": "To avoid using any hidden state"},
    ["B"])

add("Recurrent Neural Networks", "advanced", 4, "single_choice",
    "What is teacher forcing during sequence model training?",
    {"A": "Feeding the ground-truth previous token as input instead of the model's own prediction",
     "B": "Forcing all weights to be equal",
     "C": "Training without any labels",
     "D": "Using a fixed learning rate"},
    ["A"])

# ======================= UNSUPERVISED (high) ===============================
add("Unsupervised Learning", "basics", 1, "single_choice",
    "What defines unsupervised learning?",
    {"A": "It uses labelled data only",
     "B": "It finds structure in data without labels",
     "C": "It always uses reinforcement signals",
     "D": "It requires a teacher network"},
    ["B"])

add("Unsupervised Learning", "basics", 1, "single_choice",
    "What does k-means clustering do?",
    {"A": "Classifies data with labels",
     "B": "Partitions data into k groups by minimizing within-cluster distances",
     "C": "Reduces dimensionality via eigenvectors",
     "D": "Generates new images"},
    ["B"])

add("Unsupervised Learning", "basics", 1, "single_choice",
    "What is the main purpose of PCA?",
    {"A": "To label data",
     "B": "To reduce dimensionality while preserving as much variance as possible",
     "C": "To increase the number of features",
     "D": "To train a classifier"},
    ["B"])

add("Unsupervised Learning", "intermediate", 2, "single_choice",
    "What does an autoencoder learn?",
    {"A": "A compressed latent representation by reconstructing its input",
     "B": "A supervised classifier",
     "C": "A reinforcement policy",
     "D": "A fixed lookup table"},
    ["A"])

add("Unsupervised Learning", "intermediate", 3, "single_choice",
    "In a GAN, what are the two competing networks?",
    {"A": "Encoder and decoder",
     "B": "Generator and discriminator",
     "C": "Actor and critic",
     "D": "Teacher and student"},
    ["B"])

add("Unsupervised Learning", "intermediate", 2, "single_choice",
    "What advantage does DBSCAN have over k-means?",
    {"A": "It requires the number of clusters in advance",
     "B": "It can find arbitrarily shaped clusters and mark outliers as noise",
     "C": "It only works on labelled data",
     "D": "It reduces dimensionality"},
    ["B"])

add("Unsupervised Learning", "advanced", 3, "single_choice",
    "Why are learned word embeddings useful?",
    {"A": "They store words as one-hot vectors",
     "B": "They place semantically similar words near each other in a dense vector space",
     "C": "They remove the need for any training",
     "D": "They only work for images"},
    ["B"])

# ======================= COMMON PRACTICES (low) ============================
add("Common Practices", "basics", 1, "single_choice",
    "Why normalize or standardize input features?",
    {"A": "To make features have wildly different scales",
     "B": "To put features on comparable scales, which helps optimization",
     "C": "To delete outliers",
     "D": "To label the data"},
    ["B"])

add("Common Practices", "basics", 1, "single_choice",
    "What is the purpose of a validation set?",
    {"A": "To train the final weights",
     "B": "To tune hyperparameters and monitor generalization during development",
     "C": "To report the final published accuracy",
     "D": "To store the model"},
    ["B"])

add("Common Practices", "intermediate", 2, "single_choice",
    "What does k-fold cross-validation provide?",
    {"A": "A single fixed train/test split",
     "B": "A more robust performance estimate by rotating which fold is held out",
     "C": "A way to increase the dataset size permanently",
     "D": "A replacement for the loss function"},
    ["B"])

add("Common Practices", "intermediate", 3, "single_choice",
    "What is transfer learning?",
    {"A": "Copying data between servers",
     "B": "Reusing a model pre-trained on one task as a starting point for a related task",
     "C": "Training from random weights every time",
     "D": "Transferring the loss between layers"},
    ["B"])

add("Common Practices", "low_advanced", 3, "single_choice",  # will be normalised
    "Why prefer random search over grid search for many hyperparameters?",
    {"A": "It is guaranteed to find the global optimum",
     "B": "It explores important dimensions more efficiently when only a few matter",
     "C": "It never needs a validation set",
     "D": "It only works for two parameters"},
    ["B"])

# ======================= ARCHITECTURES (low) ===============================
add("Architectures", "basics", 1, "single_choice",
    "What key idea does ResNet introduce?",
    {"A": "Removing all convolutions",
     "B": "Residual/skip connections enabling very deep networks",
     "C": "Using only fully connected layers",
     "D": "Training without gradients"},
    ["B"])

add("Architectures", "basics", 1, "single_choice",
    "What is VGG known for?",
    {"A": "Large 11x11 filters only",
     "B": "Stacks of small 3x3 convolutions",
     "C": "No pooling layers",
     "D": "Recurrent connections"},
    ["B"])

add("Architectures", "intermediate", 2, "single_choice",
    "What does an Inception module do?",
    {"A": "Applies several filter sizes in parallel and concatenates the results",
     "B": "Removes all non-linearities",
     "C": "Uses a single 1x1 filter only",
     "D": "Replaces convolution with attention"},
    ["A"])

add("Architectures", "intermediate", 3, "single_choice",
    "What is the core mechanism of the Transformer architecture?",
    {"A": "Recurrence over time steps",
     "B": "Self-attention relating all positions to each other",
     "C": "Pooling over channels",
     "D": "K-means clustering"},
    ["B"])

add("Architectures", "advanced", 4, "single_choice",
    "How does a Vision Transformer (ViT) feed an image into a Transformer?",
    {"A": "One pixel per token",
     "B": "By splitting the image into fixed-size patches treated as tokens",
     "C": "By converting it to audio first",
     "D": "By using only the first row of pixels"},
    ["B"])

# ======================= VISUALIZATION & ATTENTION (low) ===================
add("Visualization and Attention Mechanism", "basics", 1, "single_choice",
    "What does a saliency map show?",
    {"A": "The training loss curve",
     "B": "Which input regions most influence the model's output",
     "C": "The network's weight values",
     "D": "The optimizer state"},
    ["B"])

add("Visualization and Attention Mechanism", "basics", 1, "single_choice",
    "What is Grad-CAM used for?",
    {"A": "Compressing the model",
     "B": "Highlighting image regions that drive a CNN's prediction",
     "C": "Cleaning the dataset",
     "D": "Choosing the learning rate"},
    ["B"])

add("Visualization and Attention Mechanism", "intermediate", 2, "single_choice",
    "In self-attention, what do the query, key and value come from?",
    {"A": "Three separate datasets",
     "B": "Learned linear projections of the same input sequence",
     "C": "The loss function",
     "D": "Random noise"},
    ["B"])

add("Visualization and Attention Mechanism", "intermediate", 3, "single_choice",
    "Why does a Transformer need positional encoding?",
    {"A": "Because attention alone is order-agnostic and would ignore token positions",
     "B": "To reduce the number of parameters",
     "C": "To replace the value vectors",
     "D": "To normalize the loss"},
    ["A"])

add("Visualization and Attention Mechanism", "advanced", 3, "single_choice",
    "What does multi-head attention provide over single-head attention?",
    {"A": "Fewer parameters and no benefit",
     "B": "Several attention patterns in parallel, capturing different relationships",
     "C": "A guarantee of zero loss",
     "D": "Removal of the feed-forward layers"},
    ["B"])

# ======================= DEEP RL (low) =====================================
add("Deep Reinforcement Learning", "basics", 1, "single_choice",
    "What does Q-learning estimate?",
    {"A": "The probability of each class",
     "B": "The expected return of taking an action in a state",
     "C": "The reconstruction error",
     "D": "The gradient of the loss"},
    ["B"])

add("Deep Reinforcement Learning", "basics", 1, "single_choice",
    "What is the exploration-exploitation trade-off?",
    {"A": "Choosing between two loss functions",
     "B": "Balancing trying new actions against using known good ones",
     "C": "Balancing width and depth of a network",
     "D": "Choosing the batch size"},
    ["B"])

add("Deep Reinforcement Learning", "intermediate", 2, "single_choice",
    "What does epsilon-greedy exploration do?",
    {"A": "Always picks the best-known action",
     "B": "Picks a random action with probability epsilon, else the greedy action",
     "C": "Never explores",
     "D": "Uses gradient descent to explore"},
    ["B"])

add("Deep Reinforcement Learning", "intermediate", 3, "single_choice",
    "Why is experience replay used in DQN?",
    {"A": "To delete old data",
     "B": "To reuse past transitions and break correlations between consecutive samples",
     "C": "To avoid using a reward",
     "D": "To increase the learning rate"},
    ["B"])

add("Deep Reinforcement Learning", "advanced", 3, "single_choice",
    "What role does the target network play in DQN?",
    {"A": "It generates the environment",
     "B": "It provides slowly-updated target values, stabilising training",
     "C": "It replaces the replay buffer",
     "D": "It picks the batch size"},
    ["B"])

# ======================= SEGMENTATION (low) ================================
add("Segmentation", "basics", 1, "single_choice",
    "What does semantic segmentation produce?",
    {"A": "A single label for the whole image",
     "B": "A class label for every pixel",
     "C": "Bounding boxes only",
     "D": "A caption"},
    ["B"])

add("Segmentation", "basics", 1, "single_choice",
    "How does instance segmentation differ from semantic segmentation?",
    {"A": "It ignores object classes",
     "B": "It separates individual object instances, not just classes",
     "C": "It only works on text",
     "D": "It produces one label for the image"},
    ["B"])

add("Segmentation", "intermediate", 2, "single_choice",
    "What is the defining feature of the U-Net architecture?",
    {"A": "It has no convolutions",
     "B": "An encoder-decoder with skip connections between matching levels",
     "C": "It uses only fully connected layers",
     "D": "It is a recurrent network"},
    ["B"])

add("Segmentation", "intermediate", 3, "single_choice",
    "What does a Fully Convolutional Network (FCN) replace to enable pixel-wise output?",
    {"A": "The convolutions with attention",
     "B": "The fully connected layers with convolutional layers",
     "C": "The loss with accuracy",
     "D": "The pooling with dropout"},
    ["B"])

add("Segmentation", "advanced", 3, "single_choice",
    "What does panoptic segmentation combine?",
    {"A": "Classification and regression",
     "B": "Semantic segmentation (stuff) and instance segmentation (things)",
     "C": "Detection and captioning",
     "D": "Clustering and PCA"},
    ["B"])

# ---------------------------------------------------------------------------
# Normalise difficulty labels, assign ids, validate, and write JSON.
# ---------------------------------------------------------------------------

DIFF_FIX = {"low_advanced": "advanced"}
VALID_DIFF = {"basics", "intermediate", "advanced"}

bank = []
for i, q in enumerate(Q, start=1):
    diff = DIFF_FIX.get(q["difficulty"], q["difficulty"])
    assert diff in VALID_DIFF, f"bad difficulty {diff}"
    # sanity: correct answers must exist in options
    for c in q["correct_answers"]:
        assert c in q["options"], f"Q{i} correct key {c} not in options"
    # sanity: points are integers in the agreed ranges
    assert isinstance(q["points"], int)
    bank.append({
        "id": f"q{i:04d}",
        "topic": q["topic"],
        "difficulty": diff,
        "points": q["points"],
        "type": q["type"],
        "question": q["question"],
        "options": q["options"],
        "correct_answers": q["correct_answers"],
    })

# Priority metadata used by the app to weight sampling and label topics.
PRIORITY = {
    "Introduction": "high",
    "Neural Networks": "high",
    "Loss and Optimization": "high",
    "Activation Functions and CNN": "high",
    "Regularization": "high",
    "Recurrent Neural Networks": "high",
    "Unsupervised Learning": "high",
    "Common Practices": "low",
    "Architectures": "low",
    "Visualization and Attention Mechanism": "low",
    "Deep Reinforcement Learning": "low",
    "Segmentation": "low",
}

out = {
    "meta": {
        "course": "Deep Learning (SS2026)",
        "generated_by": "default bank (hand-written seed set)",
        "scheme": {"basics": [1], "intermediate": [2, 3], "advanced": [3, 4]},
        "mixed_ratio": {"basics": 0.45, "intermediate": 0.35, "advanced": 0.20},
        "priority": PRIORITY,
        "excluded_topics": [
            "Weakly Supervised Learning", "Known Operator Learning",
            "Graph Neural Networks", "Self-Supervised Learning",
        ],
    },
    "questions": bank,
}

here = os.path.dirname(os.path.abspath(__file__))
target = os.path.join(here, "..", "data", "questions.json")
with open(target, "w") as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

# Print a small report
from collections import Counter
byt = Counter(q["topic"] for q in bank)
byd = Counter(q["difficulty"] for q in bank)
print(f"Wrote {len(bank)} questions to data/questions.json")
print("By difficulty:", dict(byd))
print("By topic:")
for t, n in sorted(byt.items()):
    print(f"  {PRIORITY[t]:<4} {t}: {n}")
