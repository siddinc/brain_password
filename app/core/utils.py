import matplotlib.pyplot as plt
import numpy as np
# import cv2
from itertools import chain, islice
from tensorflow.keras.models import load_model
from tensorflow.keras import backend as K
from app.core.configuration import settings


SQRT2 = K.sqrt(K.constant(2.0))

def create_chunks(iterable, size):
  iterator = iter(iterable)
  for first in iterator:
    yield list(chain([first], islice(iterator, size - 1)))


def get_spectrogram(iterable, size):
  spectrogram =  np.array(list(create_chunks(iterable, size)))
  spectrogram = np.reshape(spectrogram, (spectrogram.shape[0], spectrogram.shape[1], 1))
  return spectrogram

# def preprocess_input(eeg_signal):
#   spectrogram = get_spectrogram(eeg_signal)
#   gray_spectrogram = rgb2gray(spectrogram)
#   scaled_spectrogram = min_max_scaling(gray_spectrogram, 0.0, 1.0)

#   if scaled_spectrogram.shape != (settings.figsize_height, settings.figsize_width):
#     scaled_spectrogram = cv2.resize(scaled_spectrogram, (settings.figsize_height, settings.figsize_width))

#   reshaped_spectrogram = np.reshape(
#     scaled_spectrogram, (scaled_spectrogram.shape[0], scaled_spectrogram.shape[1], 1)
#   )
#   return reshaped_spectrogram


# def get_spectrogram(
#   eeg_signal, fs=settings.fs, nfft=settings.nfft, noverlap=settings.noverlap,
#   figsize=(settings.figsize_width, settings.figsize_height), cmap=settings.cmap):
#   fig, ax = plt.subplots(1, figsize=figsize)
#   fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
#   fig.dpi = 100
#   ax.axis('off')
#   ax.grid(False)

#   pxx, freqs, bins, im = ax.specgram(x=eeg_signal, Fs=fs, noverlap=noverlap, NFFT=nfft, cmap=cmap)
#   return fig2rgb(fig)


# def fig2rgb(fig):
#   fig.canvas.draw()
#   buf = fig.canvas.tostring_rgb()
#   width, height = fig.canvas.get_width_height()
#   plt.close(fig)
#   return np.frombuffer(buf, dtype=np.uint8).reshape(height, width, 3)


# def rgb2gray(rgb_img):
#   cv_rgb_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR)
#   cv_gray = cv2.cvtColor(cv_rgb_img, cv2.COLOR_BGR2GRAY)
#   return cv_gray


# def min_max_scaling(img, f_min, f_max):
#   spec_std = (img - img.min()) / (img.max() - img.min())
#   spec_scaled = spec_std * (f_max - f_min) + f_min
#   return spec_scaled


def contrastive_loss(y_true, y_pred):
  margin = settings.margin
  return K.mean((1.0 - y_true) * K.square(y_pred) + (y_true) * K.square(K.maximum(margin - y_pred, 0.0)))


# def hellinger_distance(embeddings):
#   (p, q) = embeddings
#   return K.sqrt(K.maximum(K.square(K.sqrt(p) - K.sqrt(q)), K.epsilon())) / SQRT2


def load_network(network_path):
  return load_model(network_path, custom_objects={"contrastive_loss": contrastive_loss, "SQRT2": SQRT2})


# if __name__ == "__main__":
#   model = load_network("/home/parag/Desktop/BrainPasswordBackend/brain_password_backend/networks/model1.h5")
#   print(model.summary())