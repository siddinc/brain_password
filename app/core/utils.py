import matplotlib.pyplot as plt
import numpy as np
# import cv2
from itertools import chain, islice
from tensorflow.keras.models import load_model
from tensorflow.keras import backend as K
from fastapi import APIRouter, status, Query, Path, Request, Body, HTTPException, UploadFile, File
from uuid import UUID, uuid4
from app.core.configuration import settings


SQRT2 = K.sqrt(K.constant(2.0))


def create_chunks(iterable, size=int(settings.figsize_width*100)):
  iterator = iter(iterable)
  for first in iterator:
    yield list(chain([first], islice(iterator, size - 1)))


def unflatten_spectrogram(spectrogram_1d):
  spectrogram_2d =  np.array(list(create_chunks(spectrogram_1d)))
  spectrogram_2d = np.reshape(spectrogram_2d, (spectrogram_2d.shape[0], spectrogram_2d.shape[1], 1))
  return spectrogram_2d


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
#   model = load_network("/home/siddharth/Desktop/brain_password_backend/networks/model1.h5")
#   model.summary()
