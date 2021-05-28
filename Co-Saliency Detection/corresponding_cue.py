
# This function computes corresponding cue of each colour cluster that is identified in the input image,
# and returns a dictionary, containing contrast cue value of each cluster.

def calculate_corresponding_cue():
  corresponding_cue = defaultdict(list)

  for k in range(clusters):
    nk = Counter(label)[k]           # number of pixels in kth cluster

    for m in range(len(image_list)):
      clus_label = label_list[m]
      corresponding_cue[k].append((Counter(clus_label)[k]/nk))
      
  return corresponding_cue
