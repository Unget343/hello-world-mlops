from sagemaker.sklearn.model import SKLearnModel

model = SKLearnModel(
  model_data = "s3://example-sagemaker-bucket/model-artifacts/model.tar.gz",
  role = 'arn:aws:iam:ID:role/SageMakerRole'
  entry_point = 'inference.py'
  framework_v = '1.2-1
)

predictor = model.deploy(
  instance_type = 'ml.t2.medium',
  initial_instance_count = 1
)
