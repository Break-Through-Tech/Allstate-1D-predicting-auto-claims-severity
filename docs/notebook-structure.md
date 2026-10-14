# Notebook structure

Use one data-load pattern for notebooks stored in this repo, and a different pattern for notebooks that stay in Google Colab. The two patterns are not interchangeable.

## Notebooks in the repo

This block is only for a notebook that lives in the GitHub repository. The claims file is `data/allstate_claims_data.csv` inside the clone. The notebook finds it by walking up from the folder where it is running, so the same cell works on any computer.

Open the notebook from inside the cloned repository. Later cells should keep using `data_path` for the file size, the hash, and any second read.

This is the load cell from `notebooks/SeptemberMilestone/Data_Readiness_&_Source_Verification.ipynb`:

```python
from pathlib import Path
import pandas as pd

# Load the dataset from this repo, on any computer.
# Walk up from the current folder until data/allstate_claims_data.csv is found.

data_path = None
for folder in [Path.cwd(), *Path.cwd().resolve().parents]:
    candidate = folder / "data" / "allstate_claims_data.csv"
    if candidate.is_file():
        data_path = candidate
        break

if data_path is None:
    raise FileNotFoundError(
        "Could not find data/allstate_claims_data.csv. "
        "Open this notebook from inside the cloned repository."
    )

df = pd.read_csv(data_path)
```

If that error appears, the notebook was started outside the clone, or `data/allstate_claims_data.csv` is missing. Open the notebook from a folder inside the repository and run the cell again.

## Notebooks in Colab

Use this block (or a variation) only while the notebook stays in Google Colab. Colab does not have the cloned `data/` folder, so the claims file is read from that person's Google Drive after Drive is mounted.

The path after `MyDrive/` is wherever that person saved the CSV. The example below matches `notebooks/OctoberGate1.ipynb`, which expects the file at the top of My Drive.

```python
from google.colab import drive
import pandas as pd

drive.mount("/content/drive")

df = pd.read_csv("/content/drive/MyDrive/allstate_claims_data.csv")
```

A Drive path belongs in the Colab copy. When that notebook is uploaded to the repo, comment out the Drive lines and use the repo block above. `Data_Readiness_&_Source_Verification.ipynb` already does that: the `drive.mount` line and the `/content/data/...` read are comments, and the active load is the repo search.