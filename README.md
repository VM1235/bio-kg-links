# Bio-KG Link Prediction (In Progress): 
Knowledge graphs are incomplete by nature. Predicting missing links can help identify **potential therapeutic targets, gene functions**, and **biological pathways** especially in large-scale omics pipelines.
This project explores methods for **predicting missing links in biomedical knowledge graphs**, with a focus on datasets like **Hetionet**. The goal is to uncover potential gene–trait-pathway relationships using:
**Graph Neural Networks (e.g., R-GCN, GraphSAGE)**
**Language-based models (e.g., LLM + RAG prompts)**

## 🚧 Project Status
Currently designing baseline pipelines using knowledge embedding models (e.g., TransE), and prototyping multi-relational GNN architectures.  
Planned next steps:
Construct a minimal Hetionet subset for experiments
Train a toy R-GCN or CompGCN model
Linearize graph triples for prompt-based link prediction
Evaluate using Hits@k and MRR

## 🧪 Dataset
[Hetionet v1.0](https://het.io/): A heterogeneous biomedical knowledge graph with 47,000 nodes and 2 million edges.
Additional datasets under consideration: FB15k-237, OpenBioLink

## 🔧 Tools & Libraries
- PyTorch Geometric / DGL
- PyKEEN / OpenKE
- FAISS (for RAG-style retrieval)
- Hugging Face Transformers (for LLM prompts)

## 📈 Evaluation Metrics
- Hits@1 / Hits@10  
- Mean Reciprocal Rank (MRR)  
- Baseline: TransE, DistMult

## Baseline
A TransE baseline using PyKEEN on FB15k-237.
- Trained for 10 epochs
- Evaluated with: Hits@1, Hits@10, Mean Reciprocal Rank (MRR)
- Output: `baseline/transE_metrics.txt`
