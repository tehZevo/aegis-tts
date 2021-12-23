import os
import uuid
import base64

from protopost import ProtoPost

PORT = int(os.getenv("PORT", 80))
MODEL_NAME = os.getenv("MODEL_NAME", None)
VOCODER_NAME = os.getenv("VOCODER_NAME", None)

def generate(text, out_path):
  command = [
    f'tts --text "{text}"',
    f'--model_name "{MODEL_NAME}"' if MODEL_NAME is not None else "",
    f'--vocoder_name "{VOCODER_NAME}"' if VOCODER_NAME is not None else "",
    f'--out_path "{out_path}"'
  ]
  os.system(" ".join(command))

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
