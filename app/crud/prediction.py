# from fastapi import APIRouter, status, Query, Path, Request, Body, HTTPException, UploadFile, File
# from typing import Optional, List, Dict
# from pydantic import Field
# from uuid import UUID, uuid4
# from app.models.prediction import Prediction
# from app.core.configuration import settings
# from app.core.utils import unflatten_spectrogram
# from app.crud.eeg_recordings import retrieve_all_eeg_recordings_data
# import numpy as np
# import csv

  # paired_dataset = np.zeros(len(all_eeg_recordings, 6, 2, 36, 54, 1))

  # for eeg_recording in all_eeg_recordings:
  #   db_spectrogram = [unflatten_spectrogram(i) for i in eeg_recording]

  # query_file = await eeg_file.read()
  # decoded_query_file = list(map(float, query_file.decode("utf-8").split(",")))
  # query_spectrogram = unflatten_spectrogram(decoded_query_file)