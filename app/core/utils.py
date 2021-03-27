import matplotlib.pyplot as plt
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras import backend as K
from app.core.configuration import (
  figsize_height, figsize_width,
  fs, nfft, noverlap, cmap,
  margin,
)


SQRT2 = K.sqrt(K.constant(2.0))


def preprocess_input(eeg_signal):
  spectrogram = get_spectrogram(eeg_signal)
  gray_spectrogram = rgb2gray(spectrogram)
  scaled_spectrogram = min_max_scaling(gray_spectrogram, 0.0, 1.0)

  if scaled_spectrogram.shape != (figsize_height, figsize_width):
    scaled_spec = cv2.resize(scaled_spectrogram, (figsize_height, figsize_width))

  reshaped_spectrogram = np.reshape(
    scaled_spectrogram, (scaled_spectrogram.shape[0], scaled_spectrogram.shape[1], 1)
  )


def get_spectrogram(
  eeg_signal, fs=fs, nfft=nfft, noverlap=noverlap,
  figsize=(figsize_width, figsize_height), cmap=cmap):
  fig, ax = plt.subplots(1, figsize=figsize)
  fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
  fig.dpi = 100
  ax.axis('off')
  ax.grid(False)

  pxx, freqs, bins, im = ax.specgram(x=eeg_signal, Fs=fs, noverlap=noverlap, NFFT=nfft, cmap=cmap)
  return fig2rgb(fig)


def fig2rgb(fig):
  fig.canvas.draw()
  buf = fig.canvas.tostring_rgb()
  width, height = fig.canvas.get_width_height()
  plt.close(fig)
  return np.frombuffer(buf, dtype=np.uint8).reshape(height, width, 3)


def rgb2gray(rgb_img):
  cv_rgb_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR)
  cv_gray = cv2.cvtColor(cv_rgb_img, cv2.COLOR_BGR2GRAY)
  return cv_gray


def min_max_scaling(img, f_min, f_max):
  spec_std = (img - img.min()) / (img.max() - img.min())
  spec_scaled = spec_std * (f_max - f_min) + f_min
  return spec_scaled


def load_network(network_path):
  return load_model(network_path, custom_objects={"contrastive_loss": contrastive_loss})


def contrastive_loss(y_true, y_pred):
  margin = margin
  return K.mean((1.0 - y_true) * K.square(y_pred) + (y_true) * K.square(K.maximum(margin - y_pred, 0.0)))


def custom_acc(y_true, y_pred):
  return K.mean(K.equal(y_true, K.cast(y_pred > 0.5, y_true.dtype)))


def hellinger_distance(embeddings):
  (p, q) = embeddings
  return K.sqrt(K.maximum(K.square(K.sqrt(p) - K.sqrt(q)), K.epsilon())) / SQRT2