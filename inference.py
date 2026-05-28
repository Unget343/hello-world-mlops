import joblib
import json
import os

def model_fn(model_dir):
  model_path = os.path.join(model_dir, "iris-model.pkl")
  model = joblib.load(model_path)
  return model

def input_fn(request_body, request_content_type):
  if request_content_type != "application/json":
    raise ValueError("Only application/json supported")

def predict_fn(input_data, model):
  predictions = model.predict(input_data)
  return predictions

def output_fn(prediction, content_type):
  return json.dumps({"predictions": prediction.tolist()})
