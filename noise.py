import numpy as np

def add_gaussian_noise(data, mean=0.0, std=0.05): 
    # Returns data with added Gaussian noise
    rng = np.random.default_rng()
    noise = rng.normal(mean, std, data.shape)
    return data.astype(np.float32) + noise.astype(np.float32)

def frequency_masking(data, max_mask_width=20, num_masks=1):
    # Applies frequency masking to a spectrogram.
    masked_data = data.copy()
    num_freq_bins = data.shape[0]

    for _ in range(num_masks):
        mask_width = np.random.randint(0, max_mask_width + 1)
        start = np.random.randint(0, num_freq_bins - mask_width + 1)
        masked_data[start:start + mask_width, :] = 0
    return masked_data

def temporal_masking(data, max_mask_width=20, num_masks=1):
    # Applies temporal masking to a spectrogram.
    masked_data = data.copy()
    num_time_frames = data.shape[1]

    for _ in range(num_masks):
        mask_width = np.random.randint(0, max_mask_width + 1)
        start = np.random.randint(0, num_time_frames - mask_width + 1)
        masked_data[:, start:start + mask_width] = 0
    return masked_data