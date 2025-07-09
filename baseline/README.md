# Baseline: TransE Knowledge Graph Embedding

This folder contains the implementation and evaluation of the **TransE** model on the biomedical knowledge graph dataset using PyKEEN.

---

## 📁 Files

- `train_transE.py`  
  Trains the TransE model and evaluates it on the dataset.
  
- `transE_metrics.txt`  
  Raw output printed after training and evaluation — saved directly from terminal.

- `extract_metrics.py`  
  Script to convert `transE_metrics.txt` into a clean CSV and generate a performance chart.

- `transE_metrics.csv`  
  Tabular version of the evaluation metrics — easy to compare values like Hits@10.

- `transE_metrics.png`  
  Visual bar chart showing `Hits@K` performance (K = 1, 3, 5, 10) for `head`, `tail`, and `both`.

---

## 🧠 What Is Happening?

- The `train_transE.py` script:
  - Loads the dataset.
  - Trains a TransE model using PyKEEN.
  - Evaluates on head, tail, and both predictions.
  - Saves the printed results to `transE_metrics.txt`.

- The `extract_metrics.py` script:
  - Reads that raw text file.
  - Parses the metrics and saves to a `.csv`.
  - Also creates a `.png` chart for quick comparison.

---

## 📊 How to Read the Results

- Open `transE_metrics.csv` in Excel or Google Sheets.
- Each row is a metric (e.g., `hits_at_10`), and columns include:
  - head / tail / both
  - optimistic / realistic / pessimistic scores

- Open `transE_metrics.png` to visually compare how the model performed in ranking the correct triples:
  - Higher bars = better Hits@K

---

## ✅ Want to Add More Baselines?

Just copy `train_transE.py`, replace `TransE` with another model (like `DistMult` or `ComplEx`), and re-run.

Then reuse `extract_metrics.py` to convert and plot.
