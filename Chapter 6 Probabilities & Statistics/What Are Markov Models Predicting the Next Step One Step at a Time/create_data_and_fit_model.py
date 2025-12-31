X, Z = model.sample(100)  # 100 samples

new_model = hmm.GaussianHMM(n_components=n_components, covariance_type="diag", n_iter=100)

new_model.fit(X)

print("Transition matrix:")
print(new_model.transmat_)
print("Means:")
print(new_model.means_)
print("Covariances:")
print(new_model.covars_)