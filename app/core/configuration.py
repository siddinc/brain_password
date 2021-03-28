from decouple import config


debug_mode = config("DEBUG_MODE", cast=bool)
host = config("HOST", cast=str)
db_url = config("DB_URL", cast=str)
db_name = config("DB_NAME", cast=str)
host = config("HOST", cast=str)
port = config("PORT", cast=int)
user_collection = config("USER_COLLECTION_NAME", cast=str)
eeg_recordings_collection = config("EEG_RECORDINGS_COLLECTION_NAME", cast=str)

nfft = config("NFFT", cast=int)
noverlap = config("NOVERLAP", cast=int)
fs = config("FS", cast=int)
cmap = config("CMAP", cast=str)
figsize_height = config("FIGSIZE_HEIGHT", cast=float)
figsize_width = config("FIGSIZE_WIDTH", cast=float)

margin = config("MARGIN", cast=float)