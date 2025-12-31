n_components = 2  # Number of states
n_features = 1    # Number of observation features

model = hmm.GaussianHMM(n_components=n_components, covariance_type="diag")