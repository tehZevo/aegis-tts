# Aegis TTS node

Powered by [Coqui TTS](https://github.com/coqui-ai/TTS)

## Usage
POST json `"any text here"` to `/`, get `<base64 encoded wav file>` back.

## Environment
- `PORT` - the port to listen on (defaults to 80)
- `LIST_MODELS` - if `true`, list available models on launch
- `MODEL_NAME` - TTS model to use (if empty, use Coqui default)
- `VOCODER_NAME` - VOCODER model to use (if empty, use Coqui default)

## TODO:
- make `max_decoder_steps` configurable
