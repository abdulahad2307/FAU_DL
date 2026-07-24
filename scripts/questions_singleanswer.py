"""Single-answer replacements for the multi-select questions.

The SS26 instructions are explicit: every question has one correct option, and
marking more than one scores zero. So multi-select questions are not just
off-style, they train a habit the exam actively penalises. merge_bank.py now
drops any question of type multiple_choice, and this module supplies a
single-answer question covering the same material.

Two shapes are used, both of which the past papers lean on heavily:

  * "Which of these is FALSE / is NOT ..."  - three true statements, one wrong
  * "Which of these is TRUE ..."            - one true statement, three wrong

Options are kept short and close in length to each other, so the longest one is
not a giveaway.
"""

S = []


def a(topic, diff, pts, q, opts, corr, expl, source="lecture notes", exercise=None):
    item = {"topic": topic, "difficulty": diff, "points": pts, "type": "single_choice",
            "question": q, "options": opts, "correct_answers": [corr],
            "explanation": expl, "source": source}
    if exercise is not None:
        item["exercise"] = exercise
    S.append(item)


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

PE = "past exams"
EX = "exercises"

# ---------------------------------------------------------------- overfitting
a(T_CP, "intermediate", 2,
  "Which of these does NOT help against overfitting?",
  {"A": "Augmenting the training images",
   "B": "Adding dropout to the dense layers",
   "C": "Training for many more epochs",
   "D": "Adding weight decay to the optimizer"},
  "C", "Training longer moves you further into overfitting once validation loss turns.", PE)

# ---------------------------------------------------------------- convolution
a(T_CNN, "intermediate", 2,
  "Which statement about a convolutional layer is FALSE?",
  {"A": "Its weight count depends on the input channels",
   "B": "Its weight count depends on the stride",
   "C": "It can handle inputs of different spatial sizes",
   "D": "Its weight count depends on the kernel size"},
  "B", "Stride changes where the kernel is evaluated, not how many weights it holds.", PE)

a(T_CNN, "intermediate", 2,
  "Which property do convolutional networks NOT rely on?",
  {"A": "Nearby pixels being related",
   "B": "The same kernel being useful anywhere",
   "C": "Every pixel connecting to every other",
   "D": "Weights being shared across positions"},
  "C", "Full connectivity is exactly what convolution replaces, and why it needs so few weights.", PE)

a(T_CNN, "intermediate", 2,
  "What does the weight count of a convolutional layer depend on?",
  {"A": "The number of kernels",
   "B": "The stride used",
   "C": "The size of the input image",
   "D": "The batch size"},
  "A", "It depends on kernel size, input channels and kernel count. Nothing else.", EX, 2)

a(T_CNN, "intermediate", 2,
  "Which statement about pooling is FALSE?",
  {"A": "It shrinks the spatial dimensions",
   "B": "It has no trainable parameters",
   "C": "It increases the channel count",
   "D": "It gives some tolerance to small shifts"},
  "C", "Pooling works inside each channel, so the depth comes out unchanged.", EX, 2)

a(T_CNN, "intermediate", 2,
  "Which statement about ReLU is FALSE?",
  {"A": "It has no parameters to learn",
   "B": "Its output is squashed between 0 and 1",
   "C": "Units stuck negative stop receiving gradient",
   "D": "Its gradient is 1 for positive inputs"},
  "B", "That range describes the sigmoid. ReLU has no upper bound at all.", EX, 1)

a(T_CNN, "intermediate", 2,
  "Which statement about activation functions is FALSE?",
  {"A": "Sigmoid outputs lie between 0 and 1",
   "B": "Tanh is zero-centred and sigmoid is not",
   "C": "Softmax is normally used on hidden layers",
   "D": "ReLU can leave units permanently inactive"},
  "C", "Softmax belongs at the output of a classifier, where you want a distribution over classes.")

# ------------------------------------------------------------ batch norm etc.
a(T_REG, "intermediate", 2,
  "Which statement about batch normalisation is FALSE?",
  {"A": "It normalises what the next layer receives",
   "B": "It has a learned scale and shift",
   "C": "It normalises the weights of each layer",
   "D": "It uses running statistics at inference"},
  "C", "It works on activations. The weights are left to the optimizer and any weight decay.", PE)

a(T_REG, "intermediate", 2,
  "Which statement about batch normalisation is TRUE?",
  {"A": "It smooths the loss surface, so larger steps work",
   "B": "It can be left out entirely at inference",
   "C": "It removes the need for an activation function",
   "D": "It rescales the weights rather than the activations"},
  "A", "Skipping it at inference would break the network, since it was trained with the transform in place.", EX, 3)

a(T_REG, "advanced", 3,
  "Which of these does NOT contribute to internal covariate shift?",
  {"A": "Earlier layers updating and shifting later inputs",
   "B": "Large steps causing big parameter changes",
   "C": "Input features left on very different scales",
   "D": "Fixing the random seed before training"},
  "D", "The seed fixes initialisation and shuffling order. It has nothing to do with distributions drifting.", PE)

a(T_REG, "intermediate", 2,
  "Which layer behaves differently during training and inference?",
  {"A": "Dropout",
   "B": "Max pooling",
   "C": "Fully connected",
   "D": "Flatten"},
  "A", "Batch normalisation is the other one, switching from batch to running statistics.", EX, 3)

a(T_REG, "intermediate", 2,
  "Which statement comparing L1 and L2 is FALSE?",
  {"A": "L1 drives many weights to exactly zero",
   "B": "L2 shrinks the largest weights hardest",
   "C": "L1 is differentiable everywhere",
   "D": "Both add a term to the loss and gradient"},
  "C", "The absolute value has a kink at zero, so L1 needs a sub-gradient there.", EX, 3)

a(T_REG, "intermediate", 2,
  "Which of these is NOT a regularisation technique?",
  {"A": "Dropout",
   "B": "Weight decay",
   "C": "Raising the learning rate",
   "D": "Data augmentation"},
  "C", "A larger learning rate destabilises training rather than restricting the model.")

a(T_REG, "intermediate", 2,
  "Which statement about adversarial examples is FALSE?",
  {"A": "They affect other methods such as SVMs too",
   "B": "They are produced by a GAN generator",
   "C": "A tiny change can flip the prediction",
   "D": "The perturbation can be hard to see"},
  "B", "They come from optimising the input against the model, not from a GAN.", PE)

# ---------------------------------------------------------------- recurrence
a(T_RNN, "intermediate", 2,
  "Which of these is NOT a problem with the simple Elman cell?",
  {"A": "Gradients shrinking over many time steps",
   "B": "Losing information from early in the sequence",
   "C": "Being unable to map many inputs to many outputs",
   "D": "Struggling to train on long sequences"},
  "C", "Many-to-many is a standard use. The real trouble is what happens to gradients over a long span.", PE)

a(T_RNN, "intermediate", 2,
  "Which statement about the LSTM is TRUE?",
  {"A": "Its cell state is updated additively",
   "B": "It has fewer parameters than a simple cell",
   "C": "It avoids backpropagation through time",
   "D": "It processes all time steps at once"},
  "A", "That additive path is what lets gradients survive a long sequence. Gates cost extra parameters.", EX, 3)

a(T_RNN, "intermediate", 2,
  "Which statement about LSTMs is FALSE?",
  {"A": "Gates decide what enters and leaves the cell state",
   "B": "They hold more parameters than a simple cell",
   "C": "They are trained without unrolling over time",
   "D": "The cell state is updated by addition"},
  "C", "They are still unrolled and trained with backpropagation through time.")

a(T_RNN, "intermediate", 2,
  "Which statement about backpropagation through time is FALSE?",
  {"A": "The network is unrolled across the sequence",
   "B": "Every time step has its own weight set",
   "C": "Gradients are summed over the time steps",
   "D": "Truncating it limits the memory needed"},
  "B", "Sharing one weight set across time is what makes the network recurrent.")

# ------------------------------------------------------------- architectures
a(T_ARCH, "intermediate", 2,
  "Which architecture uses both convolutions and skip connections?",
  {"A": "ResNet",
   "B": "VGG16",
   "C": "LeNet",
   "D": "AlexNet"},
  "A", "U-Net is another. VGG, LeNet and AlexNet are all plain stacks.", PE)

a(T_ARCH, "intermediate", 2,
  "Which feature is NOT used in LeNet?",
  {"A": "Convolutional layers",
   "B": "Pooling layers",
   "C": "Skip connections",
   "D": "Saturating activations"},
  "C", "LeNet predates ResNet. It also used tanh and sigmoid rather than ReLU.", PE)

a(T_ARCH, "intermediate", 2,
  "Which of these is NOT an advantage of making a network deeper?",
  {"A": "Features become more abstract with depth",
   "B": "It uses less memory than a shallow one",
   "C": "More complex functions can be fitted",
   "D": "Earlier features get reused by later layers"},
  "B", "More layers means more activations to store, so memory goes up rather than down.", PE)

# --------------------------------------------------------------- segmentation
a(T_SEG, "intermediate", 2,
  "Which statement about segmentation is TRUE?",
  {"A": "Semantic segmentation is classification per pixel",
   "B": "The aim of segmentation is drawing boxes",
   "C": "Instance segmentation finds one object per class",
   "D": "A mask cannot be turned into a bounding box"},
  "A", "A mask converts to a box easily. It is the reverse that loses information.", PE)

a(T_SEG, "intermediate", 2,
  "Which measure is NOT used to evaluate semantic segmentation?",
  {"A": "Mean Intersection over Union",
   "B": "Frequency weighted IoU",
   "C": "Perplexity",
   "D": "Pixel accuracy"},
  "C", "Perplexity belongs to language modelling, where it scores a predicted distribution over tokens.", PE)

a(T_SEG, "advanced", 3,
  "Which is NOT a reason to avoid classifying each pixel with dense layers?",
  {"A": "The context around the pixel is thrown away",
   "B": "The parameter count becomes enormous",
   "C": "Dense layers cannot output many classes",
   "D": "Weight sharing across positions is lost"},
  "C", "The class count is not the obstacle. The lost context and the parameter blow-up are.", PE)

# ------------------------------------------------------------------ capacity
a(T_NN, "intermediate", 2,
  "Which statement about model capacity is FALSE?",
  {"A": "It relates to the range of functions available",
   "B": "Raising it necessarily raises the bias",
   "C": "Depth is one thing that increases it",
   "D": "It sits at the heart of the bias-variance trade-off"},
  "B", "More capacity usually lowers bias and raises variance, so that has it backwards.", PE)

a(T_NN, "intermediate", 2,
  "Which statement about the forward and backward passes is FALSE?",
  {"A": "The forward pass turns input into output",
   "B": "The backward pass needs nothing from the forward pass",
   "C": "The backward pass returns the input gradient",
   "D": "Layers with parameters also get a weight gradient"},
  "B", "A dense layer has to keep its input, and ReLU has to remember which entries were positive.", EX, 1)

a(T_NN, "intermediate", 2,
  "Which statement about vanishing gradients is FALSE?",
  {"A": "Saturating activations make it worse",
   "B": "Early layers learn more slowly than late ones",
   "C": "Dropout is the usual way to fix it",
   "D": "Long sequences make it more likely"},
  "C", "Dropout is aimed at overfitting. Better activations, normalisation and skip connections are the fix here.")

# --------------------------------------------------------------- optimisation
a(T_LO, "intermediate", 2,
  "Which statement about momentum is FALSE?",
  {"A": "It builds a velocity from earlier gradients",
   "B": "It removes the need for a learning rate",
   "C": "Values near 0.9 are commonly used",
   "D": "It damps oscillation across a ravine"},
  "B", "You still set a learning rate. Momentum changes how the gradient is applied, not the step scale.", EX, 2)

a(T_LO, "intermediate", 2,
  "Which statement about SGD compared to full-batch descent is FALSE?",
  {"A": "Its gradient estimate is noisier",
   "B": "Full-batch descent needs the data shuffled",
   "C": "It makes many more updates per epoch",
   "D": "Its noise can help escape poor minima"},
  "B", "Full-batch uses the whole set for every update, so the order it sees the data in is irrelevant.")

a(T_LO, "intermediate", 2,
  "Which statement about the learning rate is FALSE?",
  {"A": "Too large a rate can make the loss diverge",
   "B": "Adam removes the need to set one",
   "C": "Too small a rate makes training crawl",
   "D": "Decaying it late helps the model settle"},
  "B", "Adam adapts the step per parameter but still takes a base rate from you.")

a(T_LO, "intermediate", 2,
  "Training loss sits high and flat from the first epoch. Which is NOT worth checking?",
  {"A": "Whether the learning rate is far too small",
   "B": "Whether the labels line up with the inputs",
   "C": "Whether dropout should be added",
   "D": "Whether the model has enough capacity"},
  "C", "A high flat loss means underfitting or a bug. Dropout would only make it worse.")

# ------------------------------------------------------------- data handling
a(T_CP, "intermediate", 2,
  "Which statement about shuffling the training data is FALSE?",
  {"A": "It stops a sample appearing twice in an epoch",
   "B": "It should be redone at the start of each epoch",
   "C": "Sorted data gives biased batch gradients",
   "D": "It does not change the loss being minimised"},
  "A", "An epoch visits each sample once either way. Shuffling changes the order, not the contents.", EX, 0)

a(T_CP, "intermediate", 2,
  "Which statement about normalising input data is FALSE?",
  {"A": "Test data uses the training statistics",
   "B": "Each sample should be normalised on its own",
   "C": "Mismatched scales make descent zig-zag",
   "D": "Zero mean and unit variance is a common choice"},
  "B", "Per-sample normalisation would erase real differences between samples and apply a different transform to each.", EX, 0)

a(T_CP, "intermediate", 2,
  "Which should you do before running a validation pass?",
  {"A": "Switch the model into evaluation mode",
   "B": "Apply the training augmentations too",
   "C": "Reset the optimizer's internal state",
   "D": "Zero the weights of the last layer"},
  "A", "Turning off gradients is the other one. Augmenting validation would make the score wobble run to run.", EX, 4)

a(T_CP, "intermediate", 2,
  "Which statement about splitting your data is FALSE?",
  {"A": "Validation guides choices during development",
   "B": "The test set should be used for early stopping",
   "C": "The test set is touched once, at the end",
   "D": "Normalisation uses training statistics only"},
  "B", "Stopping on the test set spends the one split meant to give you an honest final number.")

a(T_CP, "intermediate", 2,
  "Which statement about transfer learning is FALSE?",
  {"A": "Early layers learn features that transfer",
   "B": "Both tasks must share the same labels",
   "C": "It helps most when the new dataset is small",
   "D": "The final layer is usually replaced"},
  "B", "Identical labels would make the whole exercise pointless.")

# ------------------------------------------------------------------- general
a(T_INTRO, "intermediate", 2,
  "Which of these does NOT separate deep learning from classical machine learning?",
  {"A": "Features are learned rather than designed",
   "B": "Representation and classifier train together",
   "C": "No optimisation is involved",
   "D": "Considerably more data is usually needed"},
  "C", "Deep models are still fitted by optimisation. What changed is that nobody hand-designs the features.")

a(T_INTRO, "intermediate", 2,
  "Which of these did NOT drive the deep learning breakthrough around 2012?",
  {"A": "Large labelled datasets such as ImageNet",
   "B": "General purpose computation on GPUs",
   "C": "The first publication of backpropagation",
   "D": "Activations that do not saturate"},
  "C", "Backpropagation was decades old by then. Scale and a few training tricks were what changed.")

a(T_UNS, "intermediate", 2,
  "Which of these is NOT an unsupervised objective?",
  {"A": "Rebuilding the input through a bottleneck",
   "B": "Grouping samples by similarity",
   "C": "Cross entropy against human labels",
   "D": "Matching a generated distribution to the data"},
  "C", "That is the definition of supervised learning. The others take their signal from the data itself.")

a(T_UNS, "intermediate", 2,
  "Which statement about GANs is FALSE?",
  {"A": "The generator starts from random noise",
   "B": "The generator sees the real images directly",
   "C": "The discriminator does binary classification",
   "D": "Training is a min-max game between the two"},
  "B", "The generator only ever learns through the discriminator's verdict.")

# =========================================================================
# Scenario questions. The papers frame nearly a third of their questions as
# "you did X and observed Y" rather than as a bare definition, and after the
# multi-select conversion this bank was short on them.
# =========================================================================

a(T_LO, "intermediate", 2,
  "You train the same model twice, once with batch size 32 and once with 512, keeping the learning rate fixed. The large-batch run learns noticeably slower per epoch. Why?",
  {"A": "It makes far fewer updates per epoch",
   "B": "Its gradient estimates are much noisier",
   "C": "Large batches cannot use momentum",
   "D": "The loss function changes with batch size"},
  "A", "Fewer, better-aimed steps often lose to many rough ones, which is why the learning rate is usually scaled with the batch.")

a(T_NN, "intermediate", 2,
  "Your network trains fine for 20 layers but the training error rises when you extend it to 50. What does that point to?",
  {"A": "The deeper model is harder to optimise",
   "B": "The deeper model is overfitting",
   "C": "The labels must be wrong",
   "D": "The batch size is now too small"},
  "A", "Overfitting would push training error down, not up. Skip connections are the standard answer here.")

a(T_REG, "intermediate", 2,
  "You add batch normalisation and can suddenly train at ten times the old learning rate. What explains that?",
  {"A": "Layer inputs now stay on a steady scale",
   "B": "The gradients have become much larger",
   "C": "The network now has fewer parameters",
   "D": "Dropout is no longer doing anything"},
  "A", "A big step in one layer no longer throws off everything stacked above it.")

a(T_CNN, "intermediate", 2,
  "You swap a 7x7 convolution for three stacked 3x3 ones and accuracy holds while parameters drop. Why does that work?",
  {"A": "The stack covers the same receptive field",
   "B": "Small kernels always generalise better",
   "C": "The stride makes up the difference",
   "D": "3x3 kernels need no padding"},
  "A", "Three 3x3 layers see 7x7 between them, with fewer weights and two extra non-linearities.")

a(T_CP, "intermediate", 2,
  "Your model hits 94% on validation but 71% once it meets real production images. What is the most likely cause?",
  {"A": "Production data differs from your splits",
   "B": "The model has too few parameters",
   "C": "The learning rate was set too low",
   "D": "The batch size was too small"},
  "A", "Validation only tells you about the distribution it was drawn from.")

a(T_LO, "intermediate", 2,
  "Your loss drops quickly then starts climbing after a few hundred steps. What would you change first?",
  {"A": "Lower the learning rate",
   "B": "Add several more layers",
   "C": "Raise the learning rate",
   "D": "Drop the validation set"},
  "A", "A loss that falls then rises usually means the steps are too big to settle near a minimum.")

a(T_REG, "intermediate", 2,
  "You add dropout and both training and validation accuracy get worse. What does that suggest?",
  {"A": "There was no overfitting to fix",
   "B": "Dropout always costs accuracy",
   "C": "The learning rate must be raised",
   "D": "Dropout was left on at inference"},
  "A", "Regularisation costs capacity, which only pays off when there is a generalisation gap to close.")

a(T_RNN, "intermediate", 2,
  "Your recurrent model handles 20-step sequences well but fails on 200-step ones. What is the likely cause?",
  {"A": "Gradients vanish over the longer span",
   "B": "The batch size is now too large",
   "C": "The hidden state cannot store the input",
   "D": "The loss function stops working"},
  "A", "Gating or attention are the usual answers when longer contexts stop working.")

a(T_CP, "intermediate", 2,
  "You report 97% accuracy on a dataset where 97% of samples are negative. What should you do?",
  {"A": "Check precision and recall before believing it",
   "B": "Accept it, the model has learned the task",
   "C": "Collect more data of both classes",
   "D": "Raise the classification threshold"},
  "A", "Predicting the majority class for everything gives exactly that number while detecting nothing.")

a(T_UNS, "intermediate", 2,
  "Your GAN produces sharp images but nearly all of them look alike. What has gone wrong?",
  {"A": "Mode collapse",
   "B": "Vanishing gradients",
   "C": "Overfitting to validation",
   "D": "The discriminator has stopped learning"},
  "A", "It found a few outputs that always fool the discriminator and stopped exploring.")

a(T_SEG, "intermediate", 2,
  "Your segmentation output places objects correctly but the boundaries come out blurred. What usually helps?",
  {"A": "Skip connections into the decoder",
   "B": "A larger batch size",
   "C": "A smaller learning rate",
   "D": "Removing the encoder path"},
  "A", "Downsampling throws away the fine detail that sharp edges need, and skips put it back.")

a(T_VIS, "intermediate", 2,
  "A saliency map shows your animal classifier attending to grass rather than the animal. What does that tell you?",
  {"A": "It has latched onto a background confound",
   "B": "The saliency method is unreliable",
   "C": "The network needs more layers",
   "D": "The learning rate was too high"},
  "A", "The accuracy is real but will not survive images where that correlation breaks.")

a(T_NN, "intermediate", 2,
  "You strip every activation function out of a ten-layer network and accuracy falls to that of a linear model. Why?",
  {"A": "The whole stack collapses to one linear map",
   "B": "The gradients vanish immediately",
   "C": "All the weights go to zero",
   "D": "The loss stops being differentiable"},
  "A", "Composing affine maps gives another affine map, so ten layers express what one can.")

a(T_INTRO, "intermediate", 2,
  "You double the training set and validation accuracy jumps noticeably. What does that suggest?",
  {"A": "Data was the binding constraint, not capacity",
   "B": "The learning rate was set too high",
   "C": "The model is badly underfitting",
   "D": "The validation split is broken"},
  "A", "If capacity had been the limit, extra data would have made much less difference.")

a(T_CP, "intermediate", 2,
  "Your first epoch already gives near-perfect validation accuracy. What should you check?",
  {"A": "Whether training data leaked into validation",
   "B": "Whether the learning rate is too high",
   "C": "Whether the batch size is too small",
   "D": "Whether dropout is switched on"},
  "A", "Results that look too good almost always mean the split is broken.")

a(T_LO, "intermediate", 2,
  "Your loss does not move at all from the very first iteration. What is the most likely cause?",
  {"A": "The updates never reach the parameters",
   "B": "The batch size is too large",
   "C": "The validation set is too small",
   "D": "There are too many layers"},
  "A", "A perfectly flat loss usually means a zero learning rate or an optimizer that was never given the parameters.")

a(T_NN, "intermediate", 2,
  "Two runs of the same network with different seeds give test scores 4 points apart. What is the right response?",
  {"A": "Report the mean and spread over several runs",
   "B": "Report whichever run scored highest",
   "C": "Fix the seed and say nothing",
   "D": "Conclude the architecture is broken"},
  "A", "A single run tells you as much about the seed as about the model.")

a(T_CNN, "intermediate", 2,
  "You feed 64x64 images to a network trained on 32x32 that ends in a flatten and dense layer. It errors out. Why?",
  {"A": "The flatten produces a vector of the wrong length",
   "B": "Convolutions cannot handle 64x64 input",
   "C": "The pooling layers reject the size",
   "D": "The loss function needs a fixed size"},
  "A", "Convolutions cope fine. It is the dense layer after the flatten that expects one exact input length.")

a(T_REG, "intermediate", 2,
  "You train with dropout but forget to switch to evaluation mode at test time. What do you observe?",
  {"A": "Predictions vary between identical runs",
   "B": "The model refuses to run",
   "C": "Accuracy improves slightly",
   "D": "The loss becomes negative"},
  "A", "Dropout stays random, so the same image can get different answers each time you ask.")

a(T_LO, "advanced", 3,
  "You switch from SGD to Adam without changing the learning rate and training becomes unstable. What is the likely reason?",
  {"A": "Adam's per-parameter scaling makes steps effectively larger",
   "B": "Adam cannot be used with mini-batches",
   "C": "Adam requires a much larger batch size",
   "D": "Adam ignores the loss function"},
  "A", "Adam usually wants a smaller base rate than SGD, commonly around 1e-3.")

a(T_CP, "intermediate", 2,
  "You fine-tune a pretrained network on 300 images and it does worse than the frozen feature extractor. What would you try?",
  {"A": "Freeze the early layers and train only the head",
   "B": "Raise the learning rate across the whole model",
   "C": "Train every layer for more epochs",
   "D": "Replace every layer with a fresh one"},
  "A", "300 images is not enough to update generic early features without damaging them.")

a(T_RNN, "intermediate", 2,
  "Your recurrent model's loss occasionally spikes to a huge value mid-training. What usually fixes it?",
  {"A": "Clipping the gradient norm",
   "B": "Adding dropout to the recurrence",
   "C": "Reducing the hidden size",
   "D": "Shuffling the time steps"},
  "A", "Those spikes are exploding gradients, and clipping bounds the step they produce.")

a(T_CNN, "intermediate", 2,
  "Half the ReLU units in a layer output zero for every input in your dataset. What has happened?",
  {"A": "Those units are stuck and no longer learning",
   "B": "The layer is correctly sparse",
   "C": "The batch normalisation has failed",
   "D": "The layer is overfitting"},
  "A", "A large step can push a unit somewhere its input is always negative, and no gradient returns to bring it back.")

a(T_UNS, "intermediate", 2,
  "Your autoencoder reconstructs the training images almost perfectly but its codes are useless for anything else. What is the likely problem?",
  {"A": "The bottleneck is too wide to force compression",
   "B": "The decoder has too few layers",
   "C": "The learning rate is too low",
   "D": "The images are not normalised"},
  "A", "With enough room in the code, the network can simply copy its input across.")

a(T_SEG, "intermediate", 2,
  "You need to check whether a room is over capacity by counting people in a photo. Which task fits?",
  {"A": "Object detection",
   "B": "Semantic segmentation",
   "C": "Image classification",
   "D": "Image denoising"},
  "A", "Segmentation merges everyone into one region, so overlapping people cannot be told apart.")

a(T_ARCH, "intermediate", 2,
  "Your model must accept images of varying size but still output 10 class scores. What change achieves that?",
  {"A": "Replace the dense head with global average pooling",
   "B": "Resize every input before the first layer",
   "C": "Add a recurrent layer at the end",
   "D": "Increase the number of kernels"},
  "A", "Convolutions have no fixed input size, and global pooling collapses whatever spatial extent is left.")

a(T_REG, "advanced", 3,
  "Your model overfits and you suspect most of the 500 input features are noise. Which regulariser do you reach for?",
  {"A": "L1, since it zeroes irrelevant weights outright",
   "B": "L2, since it shrinks every weight a little",
   "C": "A larger batch size",
   "D": "Removing the bias terms"},
  "A", "L2 would shrink those weights but leave them contributing noise to every prediction.")

a(T_LO, "intermediate", 2,
  "You must pick between two models: one with 88% train and 86% validation accuracy, another with 99% train and 81% validation. Which do you ship?",
  {"A": "The first, since it generalises better",
   "B": "The second, since it fits the data better",
   "C": "Either, the difference is not meaningful",
   "D": "Neither, both are unusable"},
  "A", "Validation accuracy is the estimate of unseen performance, and the second model's gap shows clear overfitting.")

a(T_CP, "intermediate", 2,
  "Your defect detector must not miss any faulty part, and a few false alarms are acceptable. Which metric matters most?",
  {"A": "Recall",
   "B": "Precision",
   "C": "Overall accuracy",
   "D": "Training loss"},
  "A", "Recall is the share of real defects you catch. Precision would matter more if false alarms were the expensive error.")

a(T_NN, "advanced", 3,
  "You initialise a network's weights far too large and the activations saturate in the first forward pass. What follows?",
  {"A": "Gradients are near zero and learning stalls",
   "B": "The network converges unusually fast",
   "C": "The loss becomes negative",
   "D": "The batch size must be increased"},
  "A", "Saturated units sit in the flat part of their activation, where the derivative is close to nothing.")
