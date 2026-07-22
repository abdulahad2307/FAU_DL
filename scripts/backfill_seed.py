"""Backfill the hand-written seed questions.

The original seed set shipped without explanations and without a source tag, so
roughly a quarter of the answer review came back blank and the seed questions
could not be filtered. This script fills in both, matching on question text so
it stays correct even after ids are reassigned by merge_bank.py.

Safe to re-run: questions that already have an explanation are left alone.
"""

import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.join(HERE, "..", "data", "questions.json")

# keyed by the first 60 characters of the question text
EXPL = {
    "What most distinguishes deep learning from classical machi":
        "Classical pipelines rely on hand-engineered features; deep networks learn the representation and the classifier jointly from raw data.",
    "Why are the networks in deep learning called 'deep'?":
        "Depth refers to the number of processing layers between input and output, which is what allows hierarchical feature composition.",
    "Which event is widely credited with sparking the modern de":
        "AlexNet's 2012 ImageNet win cut the error rate dramatically and convinced the vision community that deep CNNs were worth the compute.",
    "Which combination of factors best explains why deep learni":
        "None of the three on its own was enough: the ideas existed earlier, but large labelled datasets and GPU training made them practical.",
    "What does a single artificial neuron compute before applyi":
        "The pre-activation is an affine function of the inputs; the activation function is then applied to that scalar.",
    "What is the purpose of forward propagation?":
        "Forward propagation evaluates the network to obtain predictions; gradients are only computed later in the backward pass.",
    "What does backpropagation actually compute?":
        "Backpropagation is the chain rule applied layer by layer; the optimizer is a separate step that consumes those gradients.",
    "Why must a multilayer network use non-linear activations?":
        "A composition of affine maps is itself affine, so without non-linearities the depth adds no expressive power at all.",
    "In gradient descent, how are parameters updated?":
        "The gradient points uphill, so the update moves against it, scaled by the learning rate.",
    "Which of the following are symptoms or causes of the vanis":
        "Vanishing gradients arise from repeatedly multiplying small derivatives; the learning rate can worsen training but is not the cause.",
    "What does the Universal Approximation Theorem guarantee?":
        "It is an existence result about representability. It says nothing about how many units are needed or whether training will find them.",
    "How do residual (skip) connections help train very deep ne":
        "The identity path lets the gradient bypass a block, so the effective depth for gradient flow stays small even in very deep networks.",
    "Compared with widening a network, what does adding depth m":
        "Each layer can build on the features of the previous one, so depth buys compositional structure that width alone does not.",
    "Which loss is standard for multi-class classification with":
        "Cross-entropy is the negative log-likelihood of the correct class under the softmax distribution, so the two pair naturally.",
    "Which loss is typically used for regression?":
        "Squared error corresponds to maximum likelihood under Gaussian noise, which is the usual assumption for continuous targets.",
    "How does stochastic gradient descent differ from full-batc":
        "SGD trades a noisy gradient estimate for far more updates per pass over the data, which usually converges much faster in wall-clock time.",
    "What does the learning rate control?":
        "Too large and the optimizer overshoots or diverges; too small and training crawls. It is usually the first hyperparameter to tune.",
    "What is the main benefit of using momentum in optimization":
        "Momentum accumulates a velocity across steps, damping oscillations across steep directions and accelerating along consistent ones.",
    "What two ideas does the Adam optimizer combine?":
        "Adam keeps a running first moment (momentum) and a running second moment, using the latter to scale each parameter's step individually.",
    "Why use a mini-batch rather than a single sample or the fu":
        "Mini-batches average out much of the single-sample noise while still allowing many updates per epoch, and they map well onto GPU hardware.",
    "What problem does learning-rate scheduling (e.g. decay or ":
        "A rate that worked early on becomes too coarse near a minimum, so the loss bounces around instead of settling.",
    "Which statements about convergence and overfitting are cor":
        "Low training loss says nothing about held-out performance, which is precisely why a separate validation set is needed.",
    "What is the output of the ReLU function for an input x?":
        "ReLU passes positive values unchanged and clamps everything else to zero, which is what makes it cheap and non-saturating.",
    "What is the output range of the sigmoid function?":
        "The sigmoid squashes the real line into the open interval (0, 1), which is why it can be read as a probability.",
    "What does a convolutional layer primarily do?":
        "The same kernel is applied at every position, so the layer detects a local pattern wherever it occurs and shares its weights across the image.",
    "What is the purpose of a pooling layer?":
        "Downsampling shrinks the spatial dimensions, cutting memory and computation while adding a little translation invariance.",
    "How does increasing the stride of a convolution affect the":
        "A stride of s evaluates the kernel only every s positions, so each spatial dimension shrinks by roughly a factor of s.",
    "What does 'same' padding achieve with stride 1?":
        "Zero padding compensates for the pixels the kernel would otherwise lose at the border, keeping input and output the same size.",
    "Why is ReLU often preferred over sigmoid in hidden layers ":
        "The sigmoid's derivative is at most 0.25 and near zero in its tails, so stacking many sigmoid layers shrinks gradients rapidly.",
    "What is the key advantage of a dilated (atrous) convolutio":
        "Inserting gaps between kernel taps widens the receptive field exponentially with depth while the parameter count stays fixed.",
    "Given a 32x32 input, a 5x5 filter, stride 1 and no padding":
        "With valid padding the output width is (W - k)/s + 1 = (32 - 5)/1 + 1 = 28.",
    "What is the goal of regularization?":
        "Regularization trades a little training accuracy for better generalization by restricting the effective complexity of the model.",
    "What does L2 regularization add to the loss?":
        "The squared-norm penalty is also called weight decay, because its gradient shrinks every weight proportionally on each update.",
    "What effect does L1 regularization tend to have on weights":
        "The absolute-value penalty has a constant gradient magnitude, so it keeps pushing small weights until they hit exactly zero.",
    "How does dropout regularize a network?":
        "Because any unit may disappear, the network cannot rely on specific co-adapted partners and has to learn redundant features.",
    "What does batch normalization normalize?":
        "Each channel's activations are standardised using the statistics of the current mini-batch, then rescaled by learned parameters.",
    "Why can batch normalization allow higher learning rates?":
        "Keeping layer inputs at a consistent scale stops a large step in one layer from throwing off every layer above it.",
    "What is early stopping?":
        "It uses the validation curve as the stopping signal, keeping the model from the point where generalization was best.",
    "Which of the following are legitimate regularization techn":
        "Dropout, weight decay and augmentation all restrict what the model can fit; an unbounded learning rate simply breaks training.",
    "What makes an RNN suited to sequential data?":
        "The hidden state acts as a memory summarising everything seen so far, so predictions can depend on arbitrary earlier inputs.",
    "Which gates does a standard LSTM cell use?":
        "The forget gate controls what leaves the cell state, the input gate what enters, and the output gate what is exposed as the hidden state.",
    "How does a GRU compare with an LSTM?":
        "The GRU merges the forget and input gates and drops the separate cell state, giving a cheaper cell with broadly similar accuracy.",
    "Why do LSTMs handle long-term dependencies better than van":
        "The cell state is updated additively rather than by repeated multiplication, so gradients can flow across many steps without shrinking.",
    "What does a bidirectional RNN add?":
        "Running a second pass in reverse lets each position see future context too, which helps whenever the whole sequence is available up front.",
    "In a sequence-to-sequence model, what is the role of the e":
        "The encoder produces a representation of the source sequence that the decoder conditions on when generating the output.",
    "Why was the attention mechanism introduced on top of encod":
        "A single fixed-size context vector is a bottleneck for long inputs; attention lets the decoder read from all encoder states directly.",
    "What is teacher forcing during sequence model training?":
        "Feeding the true previous token stabilises early training, though it creates a mismatch with inference, where the model sees its own outputs.",
    "What defines unsupervised learning?":
        "There is no target to compare against, so the objective is defined by the data itself, for example reconstruction or cluster compactness.",
    "What does k-means clustering do?":
        "It alternates between assigning points to the nearest centroid and recomputing centroids, converging to a local optimum.",
    "What is the main purpose of PCA?":
        "PCA projects onto the leading eigenvectors of the covariance matrix, which are the directions of greatest variance in the data.",
    "What does an autoencoder learn?":
        "The bottleneck forces the network to discard everything not needed to reconstruct the input, which is what makes the code informative.",
    "In a GAN, what are the two competing networks?":
        "The generator maps noise to samples and the discriminator tries to tell them from real data; training is the resulting min-max game.",
    "What advantage does DBSCAN have over k-means?":
        "Density-based clustering needs no cluster count and, unlike k-means, is not restricted to roughly spherical, equally sized groups.",
    "Why are learned word embeddings useful?":
        "One-hot vectors are equidistant and carry no similarity; embeddings place related words close together in a dense, low-dimensional space.",
    "Why normalize or standardize input features?":
        "Features on very different scales make the loss surface elongated, so gradient descent zig-zags and needs a smaller learning rate.",
    "What is the purpose of a validation set?":
        "It stands in for unseen data while you make modelling decisions; once you tune on it, it is no longer an unbiased estimate.",
    "What does k-fold cross-validation provide?":
        "Averaging over k splits reduces the variance of the estimate, which matters most when the dataset is small.",
    "What is transfer learning?":
        "Features learned on a large source dataset often transfer, so the new task needs far less labelled data than training from scratch.",
    "Why prefer random search over grid search for many hyperpa":
        "Grid search wastes trials repeating the same values of the parameters that do not matter, while random search samples each dimension afresh.",
    "What key idea does ResNet introduce?":
        "Learning a residual relative to the identity makes very deep stacks trainable, since a block can default to passing its input through.",
    "What is VGG known for?":
        "Two stacked 3x3 convolutions have the receptive field of one 5x5 but fewer parameters and an extra non-linearity.",
    "What does an Inception module do?":
        "Running several kernel sizes side by side lets the network choose the useful scale itself, with 1x1 convolutions keeping the cost down.",
    "What is the core mechanism of the Transformer architecture":
        "Self-attention computes a weighted combination of all positions at once, so the path between any two positions has constant length.",
    "How does a Vision Transformer (ViT) feed an image into a T":
        "Patches keep the sequence length manageable; one token per pixel would make the quadratic attention cost prohibitive.",
    "What does a saliency map show?":
        "Saliency is computed from the gradient of the output with respect to the input, highlighting the pixels the prediction is most sensitive to.",
    "What is Grad-CAM used for?":
        "It weights the feature maps of a convolutional layer by their gradients, producing a coarse but class-specific heat map.",
    "In self-attention, what do the query, key and value come f":
        "All three are different learned projections of the same sequence, which is exactly what makes the attention 'self'.",
    "Why does a Transformer need positional encoding?":
        "Attention is a set operation, so without an explicit position signal the model would treat a shuffled sequence identically.",
    "What does multi-head attention provide over single-head at":
        "Each head can specialise on a different relation, and their outputs are concatenated and projected back to the model dimension.",
    "What does Q-learning estimate?":
        "The action-value function gives the expected return of an action in a state, so the greedy policy follows from taking its argmax.",
    "What is the exploration-exploitation trade-off?":
        "Exploiting maximises immediate reward but may miss a better option; exploring costs reward now in exchange for information.",
    "What does epsilon-greedy exploration do?":
        "It is the simplest workable exploration scheme; epsilon is usually annealed so the agent explores early and exploits later.",
    "Why is experience replay used in DQN?":
        "Consecutive transitions are highly correlated, which destabilises training; sampling a buffer restores something closer to i.i.d. batches.",
    "What role does the target network play in DQN?":
        "Bootstrapping from a network that is itself changing chases a moving target; a periodically copied network keeps the target fixed for a while.",
    "What does semantic segmentation produce?":
        "The output is a label map the same size as the input, with no distinction between separate objects of the same class.",
    "How does instance segmentation differ from semantic segmen":
        "Two adjacent cars get one merged region under semantic segmentation but two separate masks under instance segmentation.",
    "What is the defining feature of the U-Net architecture?":
        "The skip connections carry high-resolution detail from the contracting path into the expanding path, sharpening the boundaries.",
    "What does a Fully Convolutional Network (FCN) replace to e":
        "Fully connected layers fix the input size and discard spatial layout; replacing them with convolutions preserves both.",
    "What does panoptic segmentation combine?":
        "Amorphous 'stuff' regions such as road or sky are handled semantically, while countable 'things' get individual instance masks.",
}


def main():
    data = json.load(open(BANK))
    qs = data["questions"]

    filled = 0
    tagged = 0
    unmatched = []

    for q in qs:
        if not q.get("explanation"):
            key = q["question"][:58]
            hit = None
            for k, v in EXPL.items():
                if q["question"].startswith(k[:50]):
                    hit = v
                    break
            if hit:
                q["explanation"] = hit
                filled += 1
            else:
                unmatched.append(q["question"][:70])
        if not q.get("source"):
            q["source"] = "seed"
            tagged += 1

    json.dump(data, open(BANK, "w"), indent=2, ensure_ascii=False)

    print(f"Filled {filled} explanations, tagged {tagged} questions as source='seed'.")
    if unmatched:
        print(f"Still missing an explanation ({len(unmatched)}):")
        for u in unmatched:
            print("  -", u)


if __name__ == "__main__":
    main()
