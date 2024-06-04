import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

seed_value = 42  # fix the random numbers
np.random.seed(seed_value)

# Parameters for the peaks
def chromatogram(
    peak_means=[1, 1.5, 2.6, 5, 6.3, 9.5],
    peak_stddevs=[0.1, 0.2, 0.3, 0.3, 0.3, 0.3],
    end_x=10,
    data_points=1000,
    noise_stddev=0.05,
):
  """

  :param peak_means:
  :param peak_stddevs:
  :param end_x:
  :param data_points:
  :param noise_stddev:
  :return:
  """
  # fix random values for same result
  np.random.seed(seed_value)

  # Adjust these values for peak positions
  # Adjust these values for peak widths
  num_peaks = len(peak_means)

  # Generate x-axis (retention time)
  x = np.linspace(0, end_x, data_points)

  # Initialize an empty signal
  signal = np.zeros_like(x)

  # Create the peaks
  for i in range(num_peaks):
    peak = np.exp(-(x - peak_means[i]) ** 2 / (2 * peak_stddevs[i] ** 2))
    signal += peak

  # Add noise (optional)
  signal += np.random.normal(0, noise_stddev, len(x))

  return x, signal


def noisy_sin():
  # fix random values for same result
  np.random.seed(seed_value)

  # Generate a sample signal (you can replace this with your own data)
  x = np.linspace(0, 10, 1000)
  signal = np.sin(2 * np.pi * x) + np.random.normal(0, 0.1, 1000)
  return x, signal


# demo data
def sin_peaks(data_points=100):
  # fix random values for same result
  np.random.seed(seed_value)

  # Example 1d-vector
  y = np.linspace(0, 3.7 * np.pi, data_points)
  return range(len(y)), (0.3 * np.sin(y) + np.sin(1.3 * y) + 0.9 * np.sin(
      4.2 * y) + 0.06 * np.random.randn(data_points))


def coelute():
  # fix random values for same result
  np.random.seed(seed_value)

  # Data
  y = [9, 60, 377, 985, 1153, 672, 501, 1068, 1110, 574, 135, 23, 3, 47, 252,
       812, 1182, 741, 263, 33]
  return range(len(y)), y
