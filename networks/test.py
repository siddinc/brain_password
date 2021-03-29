import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import (
  Input, Dense, Multiply, Activation, Lambda, Reshape, BatchNormalization,
  LeakyReLU, Flatten, Dropout, Concatenate, Add,
  Conv2D, MaxPooling2D, GlobalAveragePooling2D, AveragePooling2D,
)
from tensorflow.keras.models import Model, load_model
from tensorflow.keras import backend as K

def build_sequential(cnn_input=None):
  x = Conv2D(filters=64, kernel_size=(3,3), padding="same", activation="relu")(cnn_input)
  x = BatchNormalization()(x)

  x = MaxPooling2D(pool_size=(2,2), strides=(2,2))(x)

  x = Conv2D(filters=128, kernel_size=(3,3), padding="same", activation="relu")(x)
  x = BatchNormalization()(x)

  x = MaxPooling2D(pool_size=(2,2), strides=(2,2))(x)

  x = Conv2D(filters=256, kernel_size=(3,3), padding="same", activation="relu")(x)
  x = BatchNormalization()(x)

  x = GlobalAveragePooling2D()(x)

  x = Activation("sigmoid")(x)
  return x

def build_model(height, width, channels, model_type, distance_metric):
  model_types = {
    "sequential": build_sequential,
  }

  distance_metrics = {
    "hellinger": hellinger_distance,
  }

  input_shape=(height, width, channels)
  
  # Siamese Input ----------------------------------------------------------------------------
  siamese_left_input = Input(shape=input_shape)
  siamese_right_input = Input(shape=input_shape)
  # ------------------------------------------------------------------------------------------

  # CNN --------------------------------------------------------------------------------------
  cnn_input = Input(shape=input_shape)
  cnn_output = model_types[model_type](cnn_input)
  cnn_model = Model(inputs=cnn_input, outputs=cnn_output)
  # -------------------------------------------------------------------------------------------

  # Siamese Output-----------------------------------------------------------------------------
  encoded_l = cnn_model(siamese_left_input)
  encoded_r = cnn_model(siamese_right_input)

  distance = Lambda(distance_metrics[distance_metric])([encoded_l, encoded_r])

  drop = Dropout(0.4)(distance)

  dense = Dense(64)(drop)

  siamese_output = Dense(1, activation="sigmoid")(dense)
  siamese_net = Model(inputs=[siamese_left_input, siamese_right_input], outputs=siamese_output)
  # -------------------------------------------------------------------------------------------

  return siamese_net, cnn_model

from tensorflow.keras.models import load_model
from tensorflow.keras import backend as K
SQRT2 = K.sqrt(K.constant(2))

def contrastive_loss(y_true, y_pred):
  margin = 1.0
  return K.mean(y_true * K.square(y_pred) + (1.0 - y_true) * K.square(K.maximum(margin - y_pred, 0.0)))

def custom_acc(y_true, y_pred):
  return K.mean(K.equal(y_true, K.cast(y_pred > 0.5, y_true.dtype)))

def hellinger_distance(embeddings):
  (p, q) = embeddings
  return K.sqrt(K.maximum(K.square(K.sqrt(p) - K.sqrt(q)), K.epsilon())) / SQRT2

def get_model():
  loaded_model = load_model("./networks/model1.h5",
  custom_objects={
      "contrastive_loss": contrastive_loss,
      "custom_acc": custom_acc,
      "SQRT2": SQRT2
    }
  )
  return loaded_model

if __name__ == "__main__":
  # print(os.getcwd())
  pair_test = np.load(os.path.abspath("./networks/my_file.npy"))
  model, cnn_model = build_model(36, 54, 1, "sequential", "hellinger")
  model.load_weights(os.path.abspath("./networks/model1_weights.h5"))

  # model = get_model()
  print(model.summary())

  preds = np.squeeze(model.predict([pair_test[:, 0], pair_test[:, 1]]), axis=-1)
  print(preds)