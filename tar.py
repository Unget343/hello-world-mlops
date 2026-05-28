import tarfile

with tarfile.open("model.tar.gz", "w:gz") as gz:
  tar.add("iris-model.pkl")
  tar.add("inference.py")

print("created!")
