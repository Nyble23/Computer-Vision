
# for each image in the image list, store the following data: (x,y) --> (RGB,cluster)
img_dict = defaultdict(defaultdict)

for m in range(0,2):
  temp_dict = defaultdict()
  img = image_list[m]
  clust_label = label_list[m]

  for i in range(1,img.shape[0]):
    for j in range(1,img.shape[1]):
      temp_dict[(i,j)] = (img[i][j],clust_label[i*j])
  
  img_dict[m] = temp_dict

  
  
# this function computes the gaussian or normal distribution
def normpdf(x, var):
  denom = (2*math.pi*var)**.5
  num = math.exp(-(float(x))**2/(2*var))
  
  return num/denom



# This function computes spatial cue of each colour cluster that is identified in the input image,
# and returns a dictionary, containing contrast cue value of each cluster.
def calculate_spatial_cue():
  spatial_cue = defaultdict()

  for k in range(0,clusters):
    nk = Counter(label)[k]        # number of pixels in the kth cluster
    sum_clus = 0                  # value of spatial cue of kth cluster

    for m in range(len(image_list)):
      pixel_dict = img_dict[m]
      img = image_list[m]
    
      var = (((img.shape[0])**2 + (img.shape[1])**2) **0.5 )/2

      # normalised image center
      img_centre = np.array([(img.shape[0]/2)/img.shape[0],(img.shape[1]/2)/img.shape[1]])
      
      sum_img = 0               # sum stored at image level
      for key,val in pixel_dict.items():
        #cluster number of the pixel
        clu_id = val[1]

        # normalised pixel position
        z = np.array([key[0]/img.shape[0],key[1]/img.shape[1]])  
        
        # euclidean distance between z and img_centre
        x = np.linalg.norm(z-img_centre)

        # Gaussian pdf
        N = normpdf(x,var)

        delta = 0
        if(clu_id==k):
          delta = 1
        else:
          delta = 0
        
        sum_img+= N*delta

      sum_clus+= sum_img
    
    spatial_cue[k] = sum_clus/nk

  return spatial_cue
