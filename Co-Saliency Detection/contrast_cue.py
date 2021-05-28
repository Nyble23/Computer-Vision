# This function computes contrast cue of each colour cluster that is identified in the input image,
# and returns a dictionary, containing contrast cue value of each cluster.

def calculate_contrast_cue():
  contrast_cue = defaultdict()
  N = label.shape[0]

  for k in range(0,clusters):
    sum = 0
    for i in range(0,clusters):
      if(i!=k):
        n = Counter(label)[i]
        l = np.linalg.norm(centroids[k]- centroids[i])
        sum += n*l/N

    contrast_cue[k] = sum

    return contrast_cue
