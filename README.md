# Fashion Catalogue Project

This project contains tools to download, classify, and view the Fashion Product Images Dataset.

## VPS Setup

1.  **OS**: Ubuntu 22.04 LTS or 24.04 LTS is recommended.
2.  **Prerequisites**:
    *   A Kaggle account and API key (`kaggle.json`).
    *   SSH access to your VPS.

## Quick Start on VPS

1.  Clone this repository:
    ```bash
    git clone <your-repo-url>
    cd <repo-name>
    ```

2.  Run the setup script to install dependencies:
    ```bash
    bash scripts/setup_vps.sh
    ```

3.  Configure Kaggle API:
    *   Place your `kaggle.json` in `~/.kaggle/`.
    *   `chmod 600 ~/.kaggle/kaggle.json`

4.  Download the dataset:
    ```bash
    bash scripts/download_data.sh
    ```

5.  Check the CSV structure:
    ```bash
    python3 scripts/check_csv.py
    ```
