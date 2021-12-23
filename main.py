import subprocess
import os
import uuid
import base64

from protopost import ProtoPost

PORT = int(os.getenv("PORT", 80))
MODEL_NAME = os.getenv("MODEL_NAME", None)
VOCODER_NAME = os.getenv("VOCODER_NAME", None)
LIST_MODELS = os.getenv("LIST_MODELS", "false") == "true"

if LIST_MODELS:
  os.system("tts --list_models")

def generate(text, out_path):
  command = ["tts", "--text", text]
  if MODEL_NAME is not None:
    command += ["--model_name", MODEL_NAME]
  if VOCODER_NAME is not None:
    command += ["--vocoder_name", VOCODER_NAME]
  command += ["--out_path", out_path]
  subprocess.call(command)

def handler(data):
  fn = str(uuid.uuid4()) + ".wav"

  generate(data, fn)

  with open(fn, "rb") as f:
    f = base64.b64encode(f.read())
  f = f.decode("ascii")

  os.remove(fn)

  return f

routes = {
  "": handler,
}

ProtoPost(routes).start(PORT)
