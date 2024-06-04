import numpy as np
from scipy.signal import find_peaks, savgol_filter
import matplotlib.pyplot as plt

def scipy_plotting_smoothed(xy_data, height=0.5, distance=50, smooth_window_length=50, smooth_polyorder=3):
  x, y = xy_data
  # Apply Savitzky-Golay smoothing
  smoothed_y = savgol_filter(y, window_length=smooth_window_length, polyorder=smooth_polyorder)

  # Find peaks
  peaks, properties = find_peaks(y, height=height, distance=distance)
  smooth_peaks, _ = find_peaks(smoothed_y, height=height, distance=distance)

  # Plot the chromatography data
  plt.figure(figsize=(10, 6))

  # Original signal (without smoothing)
  plt.subplot(2, 1, 1)
  scipy_plotting(x, y, peaks, False)

  # Smoothed signal
  plt.subplot(2, 1, 2)
  scipy_plotting(x, smoothed_y, smooth_peaks, False, "After smoothing")

  plt.tight_layout()
  plt.show()

def scipy_plotting(x, y, peaks, show=True,
    title='Peak Detection using scipy.signal.find_peaks()'):
  # Plot the signal and peaks
  plt.plot(x, y, label='Signal')
  plt.plot(x[peaks], y[peaks], 'ro', label='Peaks')
  # plt.legend()
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.title(title)
  if show:
    plt.show()
