"""Original questions grounded in the course lecture notes (markdown set).
High-priority topics get more coverage; excluded topics get none.
"""

L = []
def a(topic, diff, pts, qtype, q, opts, corr, expl):
    L.append({"topic": topic, "difficulty": diff, "points": pts, "type": qtype,
              "question": q, "options": opts, "correct_answers": corr,
              "explanation": expl, "source": "lecture notes"})

T_INTRO="Introduction"; T_NN="Neural Networks"; T_LO="Loss and Optimization"
T_CNN="Activation Functions and CNN"; T_REG="Regularization"
T_RNN="Recurrent Neural Networks"; T_UNS="Unsupervised Learning"
T_CP="Common Practices"; T_ARCH="Architectures"
T_VIS="Visualization and Attention Mechanism"; T_RL="Deep Reinforcement Learning"
T_SEG="Segmentation"

# =================== INTRODUCTION (high) ===================
a(T_INTRO,"basics",1,"single_choice",
 "Who introduced the perceptron, the ancestor of modern neural networks?",
 {"A":"Rosenblatt","B":"Turing","C":"Von Neumann","D":"Hinton"},["A"],
 "Frank Rosenblatt proposed the perceptron in 1958.")
a(T_INTRO,"basics",1,"single_choice",
 "The demonstration that single-layer perceptrons cannot solve XOR contributed to:",
 {"A":"The first AI boom","B":"An 'AI winter' with reduced neural-network research","C":"The invention of GPUs","D":"The ImageNet challenge"},["B"],
 "Minsky and Papert's analysis dampened enthusiasm for perceptrons for years.")
a(T_INTRO,"basics",1,"single_choice",
 "In the classical pattern-recognition pipeline, what does deep learning replace?",
 {"A":"The data acquisition","B":"Hand-crafted feature extraction — features are learned from data","C":"The evaluation metrics","D":"The hardware"},["B"],
 "End-to-end learning folds feature design into the trainable model.")
a(T_INTRO,"intermediate",2,"single_choice",
 "Which triple best explains deep learning's breakthrough around 2012?",
 {"A":"Small data, slow CPUs, shallow nets","B":"Large labeled datasets, GPU compute, improved training techniques","C":"Rule-based systems, expert knowledge, logic","D":"Quantum computers, blockchains, big data"},["B"],
 "ImageNet-scale data plus GPUs plus tricks like ReLU/dropout enabled AlexNet's win.")
a(T_INTRO,"basics",1,"single_choice",
 "Supervised learning differs from unsupervised learning in that it:",
 {"A":"Needs no data","B":"Learns from input-label pairs rather than from unlabeled data","C":"Only works on text","D":"Cannot overfit"},["B"],
 "Supervision means ground-truth targets guide the loss.")
a(T_INTRO,"intermediate",2,"single_choice",
 "Why are separate training and test sets essential?",
 {"A":"To make training faster","B":"To measure generalization on data the model has never seen","C":"Because GPUs require it","D":"To increase the dataset size"},["B"],
 "Evaluating on training data measures memorization, not generalization.")
a(T_INTRO,"basics",1,"single_choice",
 "Which of these is a typical deep learning application area?",
 {"A":"Computer vision, speech recognition and NLP","B":"Only spreadsheet calculations","C":"Only database indexing","D":"Only file compression"},["A"],
 "Perception-style tasks with raw high-dimensional inputs are the classic strongholds.")

# =================== NEURAL NETWORKS (high) ===================
a(T_NN,"basics",1,"single_choice",
 "The Rosenblatt perceptron classifies by:",
 {"A":"Taking the sign of a weighted sum of the inputs plus bias","B":"Computing a softmax","C":"Clustering the inputs","D":"Convolving the input"},["A"],
 "sign(wᵀx + b) yields the binary decision.")
a(T_NN,"basics",1,"single_choice",
 "Geometrically, a single perceptron separates the input space with:",
 {"A":"A circle","B":"A hyperplane","C":"A spiral","D":"Arbitrary curved surfaces"},["B"],
 "The decision boundary wᵀx + b = 0 is linear.")
a(T_NN,"basics",1,"single_choice",
 "What does one full pass over the entire training set during training define?",
 {"A":"A batch","B":"An epoch","C":"An iteration","D":"A fold"},["B"],
 "Epoch = every training sample seen once; iterations count individual updates.")
a(T_NN,"intermediate",2,"single_choice",
 "A learning rate chosen far too LARGE typically causes:",
 {"A":"Very slow but stable convergence","B":"Divergence or oscillation around the minimum","C":"Guaranteed global optimum","D":"No effect"},["B"],
 "Steps overshoot the minimum; the loss can bounce or explode.")
a(T_NN,"intermediate",2,"single_choice",
 "A learning rate chosen far too SMALL typically causes:",
 {"A":"Divergence","B":"Extremely slow convergence and risk of getting stuck early","C":"Exploding gradients","D":"Immediate overfitting"},["B"],
 "Tiny steps crawl through the landscape and may stall in flat regions.")
a(T_NN,"intermediate",2,"single_choice",
 "Backpropagation is essentially an efficient application of:",
 {"A":"The chain rule of calculus on the computational graph","B":"Fourier analysis","C":"Dynamic time warping","D":"Matrix inversion"},["A"],
 "Gradients are propagated backwards node by node, reusing intermediate results.")
a(T_NN,"intermediate",3,"single_choice",
 "In high-dimensional loss landscapes, the more common obstacle (compared to bad local minima) is:",
 {"A":"Saddle points and plateaus","B":"Perfect convexity","C":"Integer constraints","D":"Disconnected domains"},["A"],
 "In many dimensions most critical points are saddles; flat regions slow training.")
a(T_NN,"basics",1,"single_choice",
 "Which statement about the bias term in a neuron is correct?",
 {"A":"It scales the weights","B":"It shifts the activation threshold, like the intercept b in y = ax + b","C":"It is always zero","D":"It only exists in CNNs"},["B"],
 "Without a bias, every decision boundary would pass through the origin.")
a(T_NN,"intermediate",2,"single_choice",
 "The vanishing gradient problem with sigmoid activations is caused by:",
 {"A":"Their derivative being at most 0.25, shrinking gradients multiplied across layers","B":"Their unbounded output","C":"Their non-differentiability","D":"Their negative outputs"},["A"],
 "Repeatedly multiplying factors < 1 makes early-layer gradients exponentially small.")
a(T_NN,"advanced",3,"single_choice",
 "Which is a correct statement about the expressiveness guaranteed by the Universal Approximation Theorem?",
 {"A":"It guarantees a training algorithm will find the approximating weights","B":"It states existence of an approximating one-hidden-layer network, saying nothing about learnability or size efficiency","C":"It requires infinitely many layers","D":"It applies only to linear functions"},["B"],
 "Existence ≠ learnability: the theorem is silent on optimization and required width.")
a(T_NN,"advanced",4,"single_choice",
 "Compared to a very wide shallow network, a deep network can represent certain functions:",
 {"A":"Only worse","B":"With exponentially fewer units, thanks to feature reuse across layers","C":"Only if it is convex","D":"Identically in all cases"},["B"],
 "Hierarchical composition lets deep nets reuse sub-features efficiently.")
a(T_NN,"basics",1,"single_choice",
 "In the layer abstraction used in the exercises, every layer implements:",
 {"A":"forward(input) and backward(error) methods","B":"Only a constructor","C":"A plotting routine","D":"A database connection"},["A"],
 "Composable forward/backward pairs are the building blocks of the framework.")
a(T_NN,"intermediate",2,"single_choice",
 "The gradient of the loss w.r.t. a layer's weights is computed in the backward pass using:",
 {"A":"Only the label","B":"The incoming error tensor combined with the stored input of the forward pass","C":"The learning rate only","D":"Random noise"},["B"],
 "That is why layers cache their inputs during forward.")
a(T_NN,"basics",1,"single_choice",
 "'Fully connected' means that each neuron of a layer:",
 {"A":"Connects only to one neuron of the previous layer","B":"Receives input from every neuron of the previous layer","C":"Has no weights","D":"Shares weights with its neighbors"},["B"],
 "Dense connectivity — hence the large parameter counts on images.")

# =================== LOSS & OPTIMIZATION (high) ===================
a(T_LO,"basics",1,"single_choice",
 "Which pairing of task and standard loss is correct?",
 {"A":"Regression → cross-entropy","B":"Regression → L2 loss, classification → cross-entropy","C":"Classification → L2 loss only","D":"Both → hinge loss only"},["B"],
 "MLE under Gaussian noise gives L2 for regression; under a categorical model it gives cross-entropy.")
a(T_LO,"intermediate",2,"single_choice",
 "Deriving the L2 loss from maximum likelihood assumes the regression targets are corrupted by:",
 {"A":"Uniform noise","B":"Gaussian noise","C":"Salt-and-pepper noise","D":"No noise"},["B"],
 "The negative log-likelihood of a Gaussian is the squared error up to constants.")
a(T_LO,"basics",1,"single_choice",
 "The softmax function turns a vector of raw scores (logits) into:",
 {"A":"Integers","B":"A probability distribution: positive values summing to 1","C":"Binary values","D":"Unbounded values"},["B"],
 "exp-normalization keeps the ordering and yields class probabilities.")
a(T_LO,"intermediate",2,"single_choice",
 "The hinge loss max(0, 1 − y·f(x)) is historically associated with:",
 {"A":"Support vector machines and maximum-margin classification","B":"K-means","C":"Autoencoders","D":"Boltzmann machines"},["A"],
 "It penalizes points inside the margin — the SVM objective's loss part.")
a(T_LO,"intermediate",2,"single_choice",
 "Why is optimizing accuracy directly with gradient descent not possible?",
 {"A":"Accuracy is too expensive","B":"Accuracy is piecewise constant, so its gradient is zero almost everywhere","C":"Accuracy is unbounded","D":"Accuracy needs labels"},["B"],
 "Surrogate losses like cross-entropy provide useful gradients instead.")
a(T_LO,"intermediate",3,"single_choice",
 "The Adam optimizer maintains, per parameter:",
 {"A":"Only the raw gradient","B":"Estimates of the first moment (mean) and second moment (uncentered variance) of the gradients, with bias correction","C":"The full Hessian","D":"A replay buffer"},["B"],
 "Adaptive per-parameter step sizes come from the moment estimates.")
a(T_LO,"intermediate",2,"single_choice",
 "What does gradient clipping address?",
 {"A":"Vanishing gradients","B":"Exploding gradients, by capping the gradient norm before the update","C":"Class imbalance","D":"Slow data loading"},["B"],
 "Especially in RNNs, rescaling oversized gradients keeps updates stable.")
a(T_LO,"intermediate",2,"single_choice",
 "Compared to plain SGD, per-parameter adaptive methods (Adagrad/RMSprop) scale the step size by:",
 {"A":"The batch size","B":"An accumulated (decayed) history of squared gradients","C":"The label frequency","D":"The number of layers"},["B"],
 "Rarely-updated parameters get relatively larger steps.")
a(T_LO,"basics",1,"single_choice",
 "A typical learning-rate schedule over a long training run:",
 {"A":"Increases the rate exponentially","B":"Starts higher for fast progress and decays (step, exponential, cosine) for fine convergence","C":"Keeps the rate at 1.0","D":"Sets the rate to zero after one epoch"},["B"],
 "Decay lets the optimizer settle into a minimum instead of bouncing around it.")
a(T_LO,"advanced",3,"single_choice",
 "A batch size that is very small (e.g. 1) primarily leads to:",
 {"A":"Noisy gradient estimates — which can even help escape sharp minima, but slows wall-clock convergence","B":"Deterministic training","C":"Exploding memory use","D":"A convex problem"},["A"],
 "Noise acts like implicit regularization; large batches give smoother but costlier steps.")
a(T_LO,"basics",1,"single_choice",
 "The last activation and the loss are usually chosen TOGETHER because:",
 {"A":"They share weights","B":"The loss assumes a particular output range/interpretation (e.g. probabilities for cross-entropy)","C":"Frameworks require it","D":"Both are optional"},["B"],
 "Sigmoid+BCE and softmax+CE are matched pairs with clean gradients.")
a(T_LO,"advanced",4,"single_choice",
 "The gradient of softmax combined with cross-entropy w.r.t. the logits simplifies to:",
 {"A":"ŷ − y (predicted probabilities minus one-hot target)","B":"y/ŷ","C":"log(ŷ)","D":"The identity"},["A"],
 "This elegant cancellation is a key reason the pair is used everywhere.")
a(T_LO,"intermediate",2,"single_choice",
 "Which observation signals CONVERGENCE of training?",
 {"A":"Loss stops decreasing significantly and gradients become small","B":"The dataset shrinks","C":"The learning rate turns negative","D":"Accuracy oscillates wildly"},["A"],
 "Settling loss and vanishing updates indicate a (local) minimum was reached.")

# =================== ACTIVATIONS & CNN (high) ===================
a(T_CNN,"basics",1,"single_choice",
 "What is the 'dying ReLU' problem?",
 {"A":"ReLU outputs explode","B":"Units stuck in the negative regime output 0 with zero gradient and stop learning permanently","C":"ReLU cannot be computed on GPUs","D":"ReLU saturates at 1"},["B"],
 "Once pre-activations stay negative, no gradient revives the unit — Leaky ReLU/ELU help.")
a(T_CNN,"basics",1,"single_choice",
 "How does Leaky ReLU differ from ReLU?",
 {"A":"It clips positive values","B":"It uses a small slope α·x instead of 0 for negative inputs","C":"It is linear everywhere","D":"It outputs probabilities"},["B"],
 "The small negative slope keeps gradients alive for negative inputs.")
a(T_CNN,"intermediate",2,"single_choice",
 "The ELU activation for x ≤ 0 computes:",
 {"A":"0","B":"α(eˣ − 1)","C":"x²","D":"−x"},["B"],
 "The smooth exponential saturation pushes mean activations toward zero.")
a(T_CNN,"basics",1,"single_choice",
 "An advantage of tanh over sigmoid as hidden activation is that tanh:",
 {"A":"Never saturates","B":"Is zero-centered, giving better-behaved gradients","C":"Outputs probabilities","D":"Has no derivative"},["B"],
 "Zero-centered outputs avoid the systematic gradient sign coupling sigmoid causes.")
a(T_CNN,"intermediate",2,"single_choice",
 "Output width of a convolution: input 32, kernel 5, stride 1, padding 2 gives:",
 {"A":"28","B":"30","C":"32","D":"36"},["C"],
 "(32 − 5 + 2·2)/1 + 1 = 32 — 'same' behavior.")
a(T_CNN,"intermediate",3,"single_choice",
 "Output width of a convolution: input 32, kernel 3, stride 2, padding 1 gives:",
 {"A":"16","B":"15","C":"17","D":"31"},["A"],
 "(32 − 3 + 2)/2 + 1 = 16 — stride 2 halves the resolution.")
a(T_CNN,"intermediate",2,"single_choice",
 "The receptive field of a unit deep in a CNN is:",
 {"A":"Always one pixel","B":"The region of the INPUT image that can influence that unit's activation","C":"The kernel size of its layer only","D":"The output size"},["B"],
 "Stacking layers (and striding/pooling) grows the effective input region per unit.")
a(T_CNN,"advanced",3,"single_choice",
 "Two stacked 3×3 convolutions (stride 1) have the same receptive field as one:",
 {"A":"3×3","B":"5×5 — but with fewer parameters and an extra non-linearity","C":"7×7","D":"9×9"},["B"],
 "The VGG insight: stacks of small kernels replace large ones efficiently.")
a(T_CNN,"basics",1,"single_choice",
 "Convolutional feature extraction is approximately equivariant to:",
 {"A":"Rotation","B":"Translation — shifting the input shifts the feature map correspondingly","C":"Scaling","D":"Color inversion"},["B"],
 "Weight sharing across positions produces the translation property.")
a(T_CNN,"basics",1,"single_choice",
 "Average pooling differs from max pooling in that it:",
 {"A":"Takes the sum of squares","B":"Outputs the mean of the window instead of the maximum","C":"Increases the resolution","D":"Learns its weights"},["B"],
 "Both downsample; max keeps the strongest response, average smooths.")
a(T_CNN,"intermediate",2,"single_choice",
 "How does the number of parameters of a conv layer depend on the input's spatial size?",
 {"A":"Linearly","B":"Quadratically","C":"Not at all — only kernel size and channel counts matter","D":"Exponentially"},["C"],
 "That independence lets one net process differently sized images.")
a(T_CNN,"intermediate",2,"single_choice",
 "Global average pooling at the end of a CNN:",
 {"A":"Increases spatial size","B":"Collapses each feature map to a single value, enabling a fixed-size output for any input size","C":"Requires labels","D":"Only works on 1×1 maps"},["B"],
 "It replaces flatten+FC heads and adds no parameters.")
a(T_CNN,"advanced",4,"single_choice",
 "A CONV layer has 64 kernels of size 5×5 on a 32-channel input. Total weights (no biases):",
 {"A":"64·32·25 = 51200","B":"64·25 = 1600","C":"32·25 = 800","D":"64·32 = 2048"},["A"],
 "kernels × input channels × kernel area.")
a(T_CNN,"basics",1,"single_choice",
 "Which output activation yields the class probabilities of a 10-class classifier?",
 {"A":"ReLU over 10 units","B":"Softmax over 10 units","C":"One sigmoid unit","D":"Max pooling"},["B"],
 "Softmax normalizes the 10 logits into a distribution.")

# =================== REGULARIZATION (high) ===================
a(T_REG,"basics",1,"single_choice",
 "Overfitting is best diagnosed by observing:",
 {"A":"Training loss only","B":"Training loss falling while validation loss rises","C":"The number of epochs","D":"GPU utilization"},["B"],
 "The generalization gap opening up is the overfitting signature.")
a(T_REG,"basics",1,"single_choice",
 "Underfitting shows itself as:",
 {"A":"Low training and low validation error","B":"High error on BOTH training and validation data","C":"Zero training loss","D":"Perfect test accuracy"},["B"],
 "The model lacks capacity or training to even fit the training set.")
a(T_REG,"intermediate",2,"single_choice",
 "L2 regularization is equivalent to which optimizer-side technique?",
 {"A":"Momentum","B":"Weight decay","C":"Gradient clipping","D":"Learning-rate warmup"},["B"],
 "Shrinking weights each step by a factor implements the L2 penalty's gradient.")
a(T_REG,"intermediate",2,"single_choice",
 "From a Bayesian view, L2 regularization corresponds to which prior on the weights?",
 {"A":"Uniform","B":"Gaussian (centered at zero)","C":"Laplacian","D":"Poisson"},["B"],
 "L1 corresponds to a Laplacian prior — hence its sparsity.")
a(T_REG,"intermediate",2,"single_choice",
 "With inverted dropout (keep probability p), what happens at TEST time?",
 {"A":"Units are dropped as in training","B":"Nothing special — activations were already scaled by 1/p during training","C":"All activations are halved","D":"The network is retrained"},["B"],
 "Scaling during training keeps expected activations consistent, so inference runs unchanged.")
a(T_REG,"basics",1,"single_choice",
 "Which of these is a form of data augmentation for images?",
 {"A":"Random crops, flips and rotations of training images","B":"Deleting the test set","C":"Increasing the learning rate","D":"Adding more layers"},["A"],
 "Label-preserving transforms multiply the effective training data.")
a(T_REG,"intermediate",2,"single_choice",
 "Early stopping works by:",
 {"A":"Stopping when training loss is zero","B":"Monitoring validation performance and keeping the best checkpoint before it degrades","C":"Halving the dataset","D":"Freezing the first layer"},["B"],
 "It restricts effective capacity by limiting optimization time.")
a(T_REG,"advanced",3,"single_choice",
 "Batch normalization at TRAINING time normalizes each channel using:",
 {"A":"Fixed constants","B":"The mean and variance computed over the current mini-batch, then applies learnable scale γ and shift β","C":"The test statistics","D":"The weight matrix"},["B"],
 "γ and β restore representational power after standardization.")
a(T_REG,"advanced",3,"single_choice",
 "Why can dropout be interpreted as an implicit ensemble?",
 {"A":"It trains several separate models","B":"Each mask trains a different sub-network with shared weights; inference approximates averaging them","C":"It duplicates the dataset","D":"It has no such interpretation"},["B"],
 "Exponentially many thinned networks share parameters.")
a(T_REG,"basics",1,"single_choice",
 "Label noise and small datasets make which failure mode more likely?",
 {"A":"Underflow","B":"Overfitting — the model memorizes noise instead of structure","C":"Exploding gradients","D":"Slow I/O"},["B"],
 "Regularization and augmentation are the standard countermeasures.")

# =================== RNN (high) ===================
a(T_RNN,"basics",1,"single_choice",
 "In the Elman cell, the new hidden state is computed from:",
 {"A":"Only the current input","B":"The previous hidden state combined with the current input, passed through a non-linearity","C":"The future inputs","D":"The loss"},["B"],
 "hₜ = f(W_hh·hₜ₋₁ + W_xh·xₜ) — recurrence in one line.")
a(T_RNN,"basics",1,"single_choice",
 "Which mapping type describes machine translation (sentence in, sentence out)?",
 {"A":"One-to-one","B":"Many-to-many (sequence to sequence)","C":"One-to-many","D":"Zero-to-one"},["B"],
 "Both sides are sequences of different lengths — the seq2seq setting.")
a(T_RNN,"basics",1,"single_choice",
 "Image captioning (one image in, sentence out) is which mapping type?",
 {"A":"One-to-many","B":"Many-to-one","C":"One-to-one","D":"Many-to-many"},["A"],
 "A single input unrolls into a generated sequence.")
a(T_RNN,"intermediate",2,"single_choice",
 "Sentiment classification of a whole review (sequence in, one label out) is:",
 {"A":"Many-to-one","B":"One-to-many","C":"One-to-one","D":"Many-to-many"},["A"],
 "The sequence is consumed and a single prediction emitted at the end.")
a(T_RNN,"intermediate",2,"single_choice",
 "Backpropagation through time (BPTT) works by:",
 {"A":"Ignoring time","B":"Unrolling the recurrence over the time steps and backpropagating through the unrolled graph","C":"Training each step separately","D":"Only using the last step"},["B"],
 "The shared weights receive summed gradient contributions from every step.")
a(T_RNN,"intermediate",3,"single_choice",
 "The LSTM forget gate:",
 {"A":"Deletes the input","B":"Controls how much of the previous CELL STATE is kept","C":"Sets the learning rate","D":"Outputs the prediction"},["B"],
 "A sigmoid gate scales cₜ₋₁ elementwise between 'erase' and 'keep'.")
a(T_RNN,"intermediate",2,"single_choice",
 "The LSTM input gate together with the candidate values decides:",
 {"A":"Which new information is written into the cell state","B":"When training stops","C":"The batch size","D":"Which layer is skipped"},["A"],
 "Write control complements the forget gate's erase control.")
a(T_RNN,"intermediate",2,"single_choice",
 "How does the GRU simplify the LSTM?",
 {"A":"It removes all gates","B":"It merges cell and hidden state and uses two gates (update, reset) instead of three","C":"It adds a convolution","D":"It doubles the parameters"},["B"],
 "Fewer parameters, often comparable performance.")
a(T_RNN,"intermediate",2,"single_choice",
 "A bidirectional RNN is appropriate when:",
 {"A":"Only past context may be used (online prediction)","B":"The whole sequence is available and future context helps, e.g. offline text tagging","C":"There is no sequence","D":"Memory is extremely limited"},["B"],
 "Two passes (forward and backward) are concatenated per time step.")
a(T_RNN,"advanced",3,"single_choice",
 "In seq2seq WITHOUT attention, the main information bottleneck is:",
 {"A":"The optimizer","B":"The single fixed-size context vector that must summarize the whole input sequence","C":"The vocabulary","D":"The batch dimension"},["B"],
 "Attention was introduced precisely to let the decoder look back at all encoder states.")
a(T_RNN,"intermediate",2,"single_choice",
 "Teacher forcing during sequence training means:",
 {"A":"A larger learning rate","B":"Feeding the ground-truth previous token as decoder input instead of the model's own prediction","C":"Training two teachers","D":"Removing the loss"},["B"],
 "It stabilizes and speeds up training but creates exposure bias at inference.")
a(T_RNN,"advanced",3,"single_choice",
 "Greedy decoding vs. beam search: beam search",
 {"A":"Is always slower AND worse","B":"Keeps the k best partial sequences per step, trading computation for better overall sequence probability","C":"Picks random tokens","D":"Requires no model"},["B"],
 "Greedy commits to the locally best token and can miss globally better sequences.")

# =================== UNSUPERVISED (high) ===================
a(T_UNS,"basics",1,"single_choice",
 "The bottleneck (code) of an undercomplete autoencoder forces the network to:",
 {"A":"Memorize every pixel","B":"Learn a compressed representation capturing the data's essential structure","C":"Output labels","D":"Grow deeper"},["B"],
 "Reconstruction through fewer dimensions demands abstraction.")
a(T_UNS,"basics",1,"single_choice",
 "A suitable loss for training an autoencoder on images is:",
 {"A":"Cross-entropy on class labels","B":"L2 (or L1) reconstruction loss between input and output","C":"Hinge loss","D":"Policy gradient"},["B"],
 "The target is the input itself — no labels needed.")
a(T_UNS,"intermediate",2,"single_choice",
 "An OVERcomplete autoencoder (code larger than input) risks:",
 {"A":"Underfitting","B":"Learning the identity mapping without extracting useful structure — unless regularized (e.g. sparsity, denoising)","C":"Vanishing outputs","D":"Nothing"},["B"],
 "Extra capacity must be constrained to force meaningful codes.")
a(T_UNS,"intermediate",3,"single_choice",
 "The VAE loss combines a reconstruction term with:",
 {"A":"An accuracy term","B":"A KL-divergence term pulling the latent distribution toward the prior (e.g. standard Gaussian)","C":"A hinge term","D":"A pooling term"},["B"],
 "The KL regularizer makes the latent space smooth and sampleable.")
a(T_UNS,"advanced",3,"single_choice",
 "The reparameterization trick in VAEs exists because:",
 {"A":"Sampling z ~ N(μ,σ²) is not differentiable w.r.t. μ,σ; writing z = μ + σ·ε with ε ~ N(0,1) restores the gradient path","B":"GPUs cannot sample","C":"The decoder has no weights","D":"KL cannot be computed"},["A"],
 "Moving the randomness into ε makes μ and σ trainable by backprop.")
a(T_UNS,"basics",1,"single_choice",
 "In a GAN, the generator receives as input:",
 {"A":"Real images","B":"A random noise vector (optionally plus a condition)","C":"The discriminator's weights","D":"Labels only"},["B"],
 "It maps latent noise to synthetic samples.")
a(T_UNS,"intermediate",2,"single_choice",
 "In a GAN, the discriminator's task is to:",
 {"A":"Generate images","B":"Classify whether a sample is real (from the dataset) or fake (from the generator)","C":"Cluster the data","D":"Normalize inputs"},["B"],
 "Its feedback is the training signal for the generator.")
a(T_UNS,"advanced",3,"single_choice",
 "A known GAN training failure where the generator maps many latent codes to few outputs is:",
 {"A":"Dying ReLU","B":"Mode collapse","C":"Covariate shift","D":"Teacher forcing"},["B"],
 "Diversity-promoting techniques (minibatch discrimination, unrolled GANs) counteract it.")
a(T_UNS,"intermediate",2,"single_choice",
 "Compared to GANs, VAEs typically produce:",
 {"A":"Sharper images but without a latent space","B":"Smoother/blurrier reconstructions but with a well-structured, easily sampleable latent space","C":"No images","D":"Only labels"},["B"],
 "The Gaussian assumptions smooth outputs; GAN samples tend to be sharper.")
a(T_UNS,"basics",1,"single_choice",
 "Which task is inherently UNsupervised?",
 {"A":"Digit classification with labels","B":"Clustering images by similarity without any labels","C":"Object detection with boxes","D":"Machine translation with parallel text"},["B"],
 "No annotations — the structure must come from the data itself.")

# =================== COMMON PRACTICES (low) ===================
a(T_CP,"basics",1,"single_choice",
 "The three standard data splits and their roles are:",
 {"A":"Train to fit, validation to tune hyperparameters/select models, test for the final unbiased evaluation","B":"All three for training","C":"Test for tuning","D":"Validation for the final report"},["A"],
 "Touching the test set during development invalidates the final estimate.")
a(T_CP,"intermediate",2,"single_choice",
 "Repeatedly tuning hyperparameters against the TEST set causes:",
 {"A":"Nothing","B":"Optimistically biased performance estimates (test-set leakage)","C":"Faster training","D":"Underfitting"},["B"],
 "The test set silently becomes a validation set — its estimate is no longer honest.")
a(T_CP,"intermediate",2,"single_choice",
 "Precision and recall are defined as:",
 {"A":"TP/(TP+FP) and TP/(TP+FN)","B":"TP/(TP+FN) and TP/(TP+FP)","C":"TN/(TN+FP) and TP/TN","D":"Both equal accuracy"},["A"],
 "Precision: how many predicted positives are right; recall: how many actual positives were found.")
a(T_CP,"intermediate",2,"single_choice",
 "The F1 score is:",
 {"A":"The arithmetic mean of precision and recall","B":"The harmonic mean of precision and recall","C":"Precision minus recall","D":"The ROC area"},["B"],
 "The harmonic mean punishes imbalance between the two.")
a(T_CP,"basics",1,"single_choice",
 "K-fold cross-validation is especially useful when:",
 {"A":"Data is abundant","B":"Data is scarce and a single split would give a noisy performance estimate","C":"GPUs are free","D":"The model is linear"},["B"],
 "Rotating the held-out fold uses all data for both training and evaluation.")
a(T_CP,"intermediate",3,"single_choice",
 "Why does RANDOM search often beat GRID search for hyperparameters?",
 {"A":"It is deterministic","B":"When only a few dimensions matter, random sampling covers each important axis with more distinct values","C":"It needs no compute","D":"It cannot miss the optimum"},["B"],
 "Grid search wastes trials repeating values along unimportant axes.")
a(T_CP,"basics",1,"single_choice",
 "Fine-tuning differs from feature extraction (frozen backbone) in that fine-tuning:",
 {"A":"Trains nothing","B":"Also updates (some) pretrained backbone weights with a small learning rate","C":"Deletes the backbone","D":"Uses no data"},["B"],
 "More adaptation, more risk of overfitting on small datasets.")
a(T_CP,"intermediate",2,"single_choice",
 "An ablation study serves to:",
 {"A":"Speed up inference","B":"Measure each component's contribution by removing/altering it and re-evaluating","C":"Augment the data","D":"Prune the test set"},["B"],
 "It separates what actually helps from what merely tags along.")

# =================== ARCHITECTURES (low) ===================
a(T_ARCH,"basics",1,"single_choice",
 "AlexNet's 2012 ImageNet win popularized which combination?",
 {"A":"Sigmoid + CPU training","B":"ReLU activations, dropout and GPU training","C":"Transformers","D":"Decision trees"},["B"],
 "These ingredients made training a large CNN on ImageNet feasible.")
a(T_ARCH,"intermediate",2,"single_choice",
 "The 'degradation problem' motivating ResNet describes:",
 {"A":"Overfitting on small data","B":"Deeper plain networks reaching HIGHER training error than shallower ones — an optimization, not overfitting, issue","C":"GPU memory limits","D":"Label noise"},["B"],
 "Identity shortcuts let extra layers default to a no-op, restoring trainability.")
a(T_ARCH,"intermediate",2,"single_choice",
 "A ResNet block computes:",
 {"A":"y = F(x) only","B":"y = F(x) + x, learning a residual on top of the identity","C":"y = x − F(x)","D":"y = F(F(x))"},["B"],
 "Learning the residual F is easier than learning the full mapping.")
a(T_ARCH,"intermediate",2,"single_choice",
 "GoogLeNet's Inception module:",
 {"A":"Uses one giant kernel","B":"Runs 1×1, 3×3, 5×5 convolutions (and pooling) in parallel and concatenates the results","C":"Removes all convolutions","D":"Is a recurrent cell"},["B"],
 "1×1 bottlenecks keep the parallel branches affordable.")
a(T_ARCH,"advanced",3,"single_choice",
 "DenseNet's characteristic connectivity is:",
 {"A":"No connections","B":"Each layer receives the concatenated feature maps of ALL preceding layers in its block","C":"Only skip over two layers","D":"Random connections"},["B"],
 "Maximal feature reuse with relatively few parameters per layer.")
a(T_ARCH,"advanced",3,"single_choice",
 "MobileNet reduces computation mainly through:",
 {"A":"Bigger kernels","B":"Depthwise separable convolutions splitting spatial filtering and channel mixing","C":"Removing activations","D":"Full-precision doubling"},["B"],
 "A depthwise conv per channel followed by 1×1 pointwise convs approximates a full conv cheaply.")
a(T_ARCH,"intermediate",2,"single_choice",
 "The Vision Transformer (ViT) feeds images to a transformer by:",
 {"A":"One pixel per token","B":"Splitting the image into fixed-size patches, embedding each as a token (plus position information)","C":"Converting to audio","D":"Using only the mean color"},["B"],
 "Patch embeddings make self-attention over image regions tractable.")

# =================== VISUALIZATION & ATTENTION (low) ===================
a(T_VIS,"basics",1,"single_choice",
 "Occlusion-based visualization works by:",
 {"A":"Backpropagating the loss","B":"Sliding a mask over the input and recording how the class score drops","C":"Plotting the weights","D":"Adding noise to labels"},["B"],
 "Score-sensitive regions reveal what the classifier relies on.")
a(T_VIS,"intermediate",2,"single_choice",
 "Grad-CAM produces its heatmap from:",
 {"A":"The raw input","B":"Gradient-weighted activation maps of a late convolutional layer","C":"The optimizer state","D":"The labels"},["B"],
 "Channel importance (via gradients) weights the spatial activations — coarse but class-discriminative.")
a(T_VIS,"intermediate",2,"single_choice",
 "t-SNE is typically used to:",
 {"A":"Train the network","B":"Visualize high-dimensional embeddings in 2-D while preserving local neighborhoods","C":"Normalize activations","D":"Prune weights"},["B"],
 "A go-to tool for inspecting learned feature spaces.")
a(T_VIS,"intermediate",3,"single_choice",
 "In scaled dot-product attention, the attention weights are computed as:",
 {"A":"softmax(QKᵀ/√d) applied to V","B":"Q + K + V","C":"ReLU(QV)","D":"KVᵀQ"},["A"],
 "Similarity of queries and keys, scaled and normalized, mixes the values.")
a(T_VIS,"intermediate",2,"single_choice",
 "Multi-head attention improves on a single head by:",
 {"A":"Using fewer parameters","B":"Attending in several learned subspaces in parallel, capturing different relationship types","C":"Removing the softmax","D":"Fixing the weights"},["B"],
 "Heads specialize (syntax, position, semantics, ...) and are concatenated.")
a(T_VIS,"basics",1,"single_choice",
 "Why do transformers need positional encoding?",
 {"A":"To save memory","B":"Because self-attention is permutation-invariant and otherwise ignores token order","C":"To increase depth","D":"For regularization"},["B"],
 "Position information must be injected explicitly into the embeddings.")
a(T_VIS,"advanced",3,"single_choice",
 "DeepDream-style visualizations are created by:",
 {"A":"Training the discriminator","B":"Optimizing the INPUT image via gradient ascent to maximize chosen activations, with regularization","C":"Pruning kernels","D":"Random cropping"},["B"],
 "The network's preferences are made visible in the input space.")

# =================== DEEP RL (low) ===================
a(T_RL,"basics",1,"single_choice",
 "The discount factor γ in the return Σ γᵏ rₜ₊ₖ controls:",
 {"A":"The learning rate","B":"How strongly future rewards count relative to immediate ones","C":"The batch size","D":"The state space size"},["B"],
 "γ close to 1: far-sighted agent; γ near 0: myopic agent.")
a(T_RL,"basics",1,"single_choice",
 "A policy π in reinforcement learning is:",
 {"A":"A dataset","B":"A mapping from states to (probabilities of) actions","C":"A loss function","D":"A network layer"},["B"],
 "It defines the agent's behavior in every state.")
a(T_RL,"intermediate",2,"single_choice",
 "The action-value function Q(s,a) estimates:",
 {"A":"The immediate reward only","B":"The expected return of taking action a in state s and following the policy afterwards","C":"The state visitation count","D":"The policy gradient"},["B"],
 "Q-values let the agent rank actions per state.")
a(T_RL,"intermediate",3,"single_choice",
 "The Bellman equation expresses the value of a state as:",
 {"A":"A constant","B":"The immediate reward plus the discounted value of the successor state(s)","C":"The product of all rewards","D":"The maximum weight"},["B"],
 "This recursive consistency underlies value iteration and Q-learning.")
a(T_RL,"intermediate",2,"single_choice",
 "In Deep Q-Networks (DQN), experience replay serves to:",
 {"A":"Store the best model","B":"Break the correlation of consecutive transitions by sampling past experiences randomly","C":"Increase the reward","D":"Render the environment"},["B"],
 "Decorrelated batches make Q-learning with neural networks stable.")
a(T_RL,"intermediate",2,"single_choice",
 "The target network in DQN:",
 {"A":"Selects actions greedily","B":"Provides slowly-updated target values, preventing the moving-target instability","C":"Stores replay data","D":"Computes rewards"},["B"],
 "Bootstrapped targets from a frozen copy stabilize training.")
a(T_RL,"advanced",3,"single_choice",
 "Actor-critic methods combine:",
 {"A":"Two datasets","B":"A policy network (actor) with a value network (critic) that evaluates the actor's actions","C":"Two replay buffers","D":"Encoder and decoder"},["B"],
 "The critic's value estimate reduces the variance of the policy gradient.")

# =================== SEGMENTATION (low) ===================
a(T_SEG,"intermediate",2,"single_choice",
 "Why does U-Net feed encoder features to the decoder via skip connections?",
 {"A":"To save memory","B":"To recover fine spatial detail lost through pooling, enabling precise boundaries","C":"To avoid training","D":"To reduce channels to one"},["B"],
 "High-resolution features from early layers sharpen the upsampled predictions.")
a(T_SEG,"intermediate",2,"single_choice",
 "Transposed ('up') convolutions are used in segmentation networks to:",
 {"A":"Reduce resolution","B":"Learn upsampling back to the input resolution","C":"Classify the whole image","D":"Normalize features"},["B"],
 "The decoder must undo the encoder's downsampling to label every pixel.")
a(T_SEG,"basics",1,"single_choice",
 "Panoptic segmentation combines:",
 {"A":"Detection and captioning","B":"Semantic segmentation ('stuff') with instance segmentation ('things')","C":"Two loss functions only","D":"Clustering and PCA"},["B"],
 "Every pixel gets a class AND, where applicable, an instance identity.")
a(T_SEG,"intermediate",2,"single_choice",
 "Non-maximum suppression (NMS) in object detection:",
 {"A":"Increases the number of boxes","B":"Removes overlapping duplicate detections, keeping the highest-scoring box per object","C":"Trains the network","D":"Normalizes pixel values"},["B"],
 "Detectors propose many boxes per object; NMS keeps one.")
a(T_SEG,"intermediate",3,"single_choice",
 "A detection counts as correct at IoU threshold 0.5 when:",
 {"A":"The class is right, regardless of the box","B":"The predicted box overlaps the ground-truth box with IoU ≥ 0.5 and the class matches","C":"The box touches the object","D":"The confidence is above 0.5"},["B"],
 "IoU gates localization quality; the threshold defines 'good enough'.")
a(T_SEG,"advanced",3,"single_choice",
 "Mask R-CNN extends Faster R-CNN by:",
 {"A":"Removing the box head","B":"Adding a parallel branch that predicts a segmentation mask for each detected instance","C":"Using no backbone","D":"Working only on video"},["B"],
 "Detection boxes plus per-instance masks = instance segmentation.")
a(T_SEG,"basics",1,"single_choice",
 "In YOLO, the image is divided into a grid where each cell:",
 {"A":"Is classified independently as one pixel","B":"Predicts bounding boxes with confidences and class probabilities directly","C":"Runs a separate network","D":"Stores the loss"},["B"],
 "Direct dense prediction is what makes YOLO fast.")
