# EEG Preprocessing and analysis [WS2020]
Welcome to the practical part of the EEG course.
- You can find information on the semesterproject in `./semesterproject`
- You can find the exercises in `./exercises`
- Data and results will be saved to `./local` by default, but can be changed

## Filtering
The raw data we get has a has all frequencies below 128 Hz:

![](./local/bids/sub-002/ses-P3/results/01freq_before_filtering.png)

One the one hand, we are less interested in very low frequncies, as they are often due to the drying of the EEG gel which increases resistance between the scull and electrodes. Low frequencies can be observed as a slow drift.
On the other hand, relatively low frequencies might also result form brain activity. If cut it might impact the onset latencies. A sweetspot seems to be a mild high-pass filter, which blocks frequencies  below 0.1, only.

Furthermore, the signal to noise ratio decreases at high frequencies. Reasons for this are, that noise due to the power line are at 60 Hz (in the US) and alpha, beta, delta and theta frequencies are below 30 Hz. 
However, gamma frequencies are higher. In a compromise to keep low gamma frequencies but block noise from the powerline and noisy frequencies above that, a low-pass filter of 54 Hz is applied.

The frequency spectrum after band-pass filtering can be seen in the figure below.

![](./local/bids/sub-002/ses-P3/results/02freq_after_filtering.png)

It can be seen how high frequencies are cut off. 
However, in this figure the filter does not seem to cut exactly at 0.1 and 54 Hz. Therefore, I investigate further and plot the timeline of a channel:

![](./local/bids/sub-002/ses-P3/results/03whole_overlay/channel17png)

As intended, the slow drift, as well as the offset is gone.

To investigate, if the figh pass filter has the expected effect, let's zoom in.
Raw:

![](./local/bids/sub-002/ses-P3/results/04zoom_raw.png)

Filtered:

![](./local/bids/sub-002/ses-P3/results/05zoom_filtered.png)

It looks good, as high frequcies seem to be supessed.

## ICA
![](./local/bids/sub-002/ses-P3/results/06ICA_components.png)
![](./local/bids/sub-002/ses-P3/results/07ICA_properties/component0.png)
![](./local/bids/sub-002/ses-P3/results/08Pz_before_ICA.png)
![](./local/bids/sub-002/ses-P3/results/09Pz_after_ICA.png)
![](./local/bids/sub-002/ses-P3/results/10before_after_overlay.png)
![](./local/bids/sub-002/ses-P3/results/11Pz.png)
## Event-related potential (ERP)
![](./local/bids/sub-002/ses-P3/results/12trials.png)
![](./local/bids/sub-002/ses-P3/results/13epochs_average.png)
