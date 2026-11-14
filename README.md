# Bitcoin Private Key Predictor

A historical TensorFlow experiment exploring neural networks and Bitcoin-related key data.

> [!WARNING]
> **This project does not demonstrate recovery or prediction of Bitcoin private keys from public keys.** Standard Bitcoin private keys cannot be practically recovered this way. The repository name reflects the original experiment, not a proven capability. Do not use it for wallet recovery, security decisions, or funds.

## What the current code actually does

- `data_generator.py` samples integer secrets using Python's seeded `random` module, derives public keys, and returns the secrets and three 160-bit hash representations as arrays. These generated secrets are **not secure wallet keys**.
- `train.py` takes the first two arrays returned by the generator: it feeds 256-bit secret representations as inputs and trains a 160-output model against uncompressed public-key hashes. This is the **opposite direction** from public-key-to-private-key prediction.
- `predict.py` passes a truncated historical public-key hex string as a 256-bit input to that model, then writes formatted model output to `predictions.txt`. This input does not match the secret-key inputs used for training, and the model's 160 outputs are not established private-key predictions.
- The code does not provide evidence that it can recover unseen private keys. Merely increasing the training data, changing layers, or running for more epochs does not establish such a capability.

## Installation

Requires Python 3, TensorFlow, and the other packages listed in `requirements.txt`.

```bash
git clone https://github.com/ufodia/Bitcoin-Private-Key-Predictor.git
cd Bitcoin-Private-Key-Predictor
python -m venv env
```

Activate the environment with `source env/bin/activate` on macOS/Linux or `env\Scripts\activate` on Windows, then:

```bash
pip install -r requirements.txt
```

## Running the experiment

`data_generator.py` exposes a data-generation function; running the file directly is not a documented standalone data-export step. `train.py` generates data in memory, trains the model, and attempts to save `prediction_model.keras`:

```bash
python train.py
```

The historical settings specify 10,000 training samples and 5,000 epochs. Training can take substantial time and resources; compatibility and completion depend on your environment.

After a compatible model file exists, the historical inference script can be run with:

```bash
python predict.py
```

It writes `predictions.txt`. Treat its contents as experimental numeric model output, **not a recovered private key**. The hard-coded input is truncated by the script; changing it does not correct the training/inference mismatch.

## Files

- `data_generator.py`: seeded experimental data generation.
- `train.py`: training configuration and model fitting.
- `predict.py`: historical inference example.
- `model_utils.py` and `data_processing.py`: model and data helpers.

## Contributing

Questions, issue reports, and contributions that improve the experiment's clarity are welcome.

## Support this project

**BTC**: `1GZdNtQYa2DN4b3hLekrYErv9c8WLqbBTm`

<p align="center">
  <a href="https://buymeacoffee.com/ufodia">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" height="60">
  </a>
</p>
