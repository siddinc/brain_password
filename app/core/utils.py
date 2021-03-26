def success_response(data=None, code=None, message=None):
  return {
    "code": code,
    "message": message,
    "data": data,
  }


def error_response(error=None, code=None, message=None):
  return {
    "code": code,
    "message": message,
    "error": error,
  }


def preprocess_input(inp):
  pass


def get_spectrogram(eeg_signal):
  pass


def normalize_spectrogram(spectrogram):
  pass


def rgb2gray(spectrogram):
  pass


def load_network(network_path):
  pass


def contrastive_loss(y_pred, y_true):
  pass