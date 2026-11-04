# heart-murmur-classification

## Dataset

Extract the [CirCor DigiScope Phonocardiogram dataset v2](https://www.kaggle.com/datasets/bjoernjostein/the-circor-digiscope-phonocardiogram-dataset-v2) into `data/`.

## Setup

1. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

2. Activate it using the command for your terminal:

   ```
   source .venv/bin/activate      # Linux/macOS
   .\.venv\Scripts\Activate.ps1   # Windows PowerShell
   .\.venv\Scripts\activate.bat   # Windows CMD
   ```

3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

Or, using uv:

```bash
uv venv
uv pip install -r requirements.txt
```