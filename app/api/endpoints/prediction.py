from fastapi import APIRouter, status, Query, Path, Request, Body, File, UploadFile, HTTPException, Response
from typing import Optional, List, Dict
from pydantic import Field
import numpy as np
from app.models.prediction import Prediction
from app.crud.eeg_recordings import retrieve_all_eeg_recordings_data
from app.core.utils import (get_spectrogram, load_network)
from app.models.response import CustomResponse
from time import time
router = APIRouter()

model = load_network("/home/siddharth/Desktop/brain_password_backend/networks/model1.h5")
print("Model loaded")  

@router.post("/", status_code=status.HTTP_200_OK)
async def get_user_prediction(
  request: Request,
  response: Response,
  eeg_file: UploadFile = File(...),
):
  start = time()
  all_eeg_recordings = await retrieve_all_eeg_recordings_data(request)
  end = time()
  
  query_file = await eeg_file.read()
  decoded_file = list(map(lambda e: float(e), query_file.decode("utf-8").split(",")))
  query_recording = get_spectrogram(decoded_file, 54)
  datasets = [ np.zeros((len(all_eeg_recordings), 2, 36, 54, 1)) for i in range(6) ]
  subjects = []
  results = []

  count = 0
  for eeg_recordings in all_eeg_recordings:
    subjects.append(eeg_recordings["user_id"])
    for i in range(6):
      dataset = datasets[i]    
      dataset[count,0,:,:,:] = get_spectrogram(eeg_recordings["eeg_recording_"+str(i+1)], 54)
      dataset[count,1,:,:,:] = query_recording
    count += 1
  
  first = True
  for dataset in datasets:
      if first:
        result = np.squeeze(model.predict([dataset[:,0], dataset[:,1]]), axis = -1)
        first = False
        
      else:
         pred = np.squeeze(model.predict([dataset[:,0], dataset[:,1]]), axis = -1) 
         result = np.vstack((result, pred))   
  result = np.argmin(np.mean(result, axis=0))
  
  
  return CustomResponse(
      status_code=status.HTTP_201_CREATED,
      message=str(end-start),
    )
    

        

  
    
