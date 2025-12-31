import numpy as np
from hmmlearn import hmm

# Set random seed for reproducibility
np.random.seed(42)

# Define the HMM parameters
n_components = 2  # Number of states
n_features = 1    # Number of observation features

# Create a Gaussian HMM
model = hmm.GaussianHMM(n_components=n_components, covariance_type="diag")

# Define transition matrix (rows must sum to 1)
model.startprob_ = np.array([0.6, 0.4])
model.transmat_ = np.array([[0.7, 0.3],
                            [0.4, 0.6]])

# Define means and covariances for each state
model.means_ = np.array([[0.0], [3.0]])
model.covars_ = np.array([[0.5], [0.5]])

# Generate synthetic observation data
X, Z = model.sample(100)  # 100 samples

# Create a new HMM instance
new_model = hmm.GaussianHMM(n_components=n_components, covariance_type="diag", n_iter=100)

# Fit the model to the data
new_model.fit(X)

# Print the learned parameters
print("Transition matrix:")
print(new_model.transmat_)
print("Means:")
print(new_model.means_)
print("Covariances:")
print(new_model.covars_)

# Predict the hidden states for the observed data
hidden_states = new_model.predict(X)

print("Hidden states:")
print(hidden_states)