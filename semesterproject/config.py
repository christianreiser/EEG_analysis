"""
config parameters
"""

#modes
closeInteractiveCleaningPlot = True  # hide interactive plots how manual cleaning was done

# subjects
first_subject = 1               # 1 first subject to run
last_subject = 1                # 40 last subject to run

# downsample
sfreq = 256                     # Hz

# band-filter
l_freq = 0.4                    # Hz
h_freq = 54			 # Hz
fir_design = 'firwin'           # filter design

# ICA
l_freq_ica = 1.5                # Hz, high-filter for ICA
h_freq_ica = 54               # Hz, high-filter for ICA
fir_design_ica = 'firwin'           # filter design
ica_method = 'fastica'

# epochs
epoch_tmin = -0.2               # epoch start
epoch_tmax = 0.8                # epoch end
baseline = (-0.2,0)


picked_channel = 'Pz'
picked_channel_num = 13

ref_channels = ['P9', 'P10']    # channels for rereferencing

# rejection_threshold
rejection_threshold = 125e-6


# ICA Artefacts
# subject 1
heart_sub1 = []
blink_sub1 = [0] #3
eye_sub1 = [13,17,25] # 0,1,2,6,24,29
muscle_sub1 = [2,20,24] # 5,7,10,13,16,18,21,23,28,29
noisy_electrode_sub1 = []
other_sub1 = [26,27]
unsure_sub1 = [7,9,14,15,23]

# subject 2
heart_sub2 = []
blink_sub2 = [0]
eye_sub2 = []
muscle_sub2 = [12,19,25]
noisy_electrode_sub2 = [29]
other_sub2 = [3, 7, 8, 22, 23]

# subject 3
heart_sub3 = []
blink_sub3 = []
eye_sub3 = []
muscle_sub3 = []
noisy_electrode_sub3 = []
other_sub3 = []
