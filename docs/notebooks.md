# Notebooks

**Naming**: 

Name every notebook for the work it does. The filename and the title at the top should say what the notebook checks or produces. 

**Universal data paths:** 

Every notebook uploaded to GitHub needs a data path that works for every person who clones this repo. Load `data/allstate_claims_data.csv` by searching upward from the folder where the notebook is running. A path that exists only on one computer, or only inside one Google Drive, will fail for everyone else.

The load block below is from `notebooks/SeptemberMilestone/Gate_2.ipynb`. Use the same search in every notebook. The notebook has to be opened from inside the cloned repository.

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

