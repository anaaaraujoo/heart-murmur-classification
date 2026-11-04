# heart-murmur-classification

## Dataset

Extract the [CirCor DigiScope Phonocardiogram dataset v1.0.3](https://physionet.org/content/circor-heart-sound/1.0.3/) and place its contents directly inside `data/`, without the outer ZIP folders:

```text
data/
├── training_data.csv
├── training_data/
└── ...
```

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