"""
config parameters
"""

# subjects
frist_subject = 1               # 1 first subject to run
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

