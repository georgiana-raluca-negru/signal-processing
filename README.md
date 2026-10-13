# Signal Processing Laboratories

This repository contains the laboratory exercises, assignments, and projects for the Signal Processing course. 

## Setup Instructions

To run the code in this repository locally, we must create a virtual environment first.

### 1. Create the Virtual Environment
Open a terminal, navigate to the root folder of this repository, and run the following command to create a virtual environment named `.venv`:
```bash
python3 -m venv .venv
```

### 2. Activate the Environment
Before installing dependencies, activate the environment. 

* **On Linux/macOS:**
  ```bash
  source .venv/bin/activate
  ```
* **On Windows:**
  ```bash
  .venv\Scripts\activate
  ```

### 3. Install Dependencies
With the environment activated, install all the required packages from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```