# IMVIA - Intra-Modality Multi-View Fusion and Inter-Modality Alignment for Knowledge Graph Completion

## Overview

IMVIA (Intra-Modality Multi-View Fusion and Inter-Modality Alignment) is a state-of-the-art framework for multi-modal knowledge graph completion (MMKGC). The system enhances the structural and semantic richness of knowledge graphs by integrating diverse information from different modalities, such as images and text, while ensuring both intra-modality diversity and cross-modality alignment.

The core objective of IMVIA is to improve entity and relation representation by capturing feature diversity within the same modality and ensuring effective alignment between different modalities. IMVIA uses multi-view characterization to extract distinctive features and applies contrastive learning for cross-modality consistency.

## Key Features

- **Intra-Modality Multi-View Fusion:** Efficiently integrates diverse views within each modality, such as multiple images or textual descriptions, to enhance entity representation.
- **Cross-Modality Alignment:** Ensures consistent training objectives across modalities through a novel alignment mechanism combining information disentanglement and contrastive learning.
- **Relation-Aware Gated Decision Fusion:** Dynamically integrates information from different modalities, taking into account relational context for robust decision-making.
- **Robust Entity Representations:** IMVIA captures the nuances within and across modalities, significantly improving the performance of knowledge graph completion tasks.

## Requirements

To install the dependencies required to run the project, execute:

```bash
pip install -r requirements.txt


## Requirements

To install the dependencies required to run the project, execute:

```bash
pip install -r requirements.txt




##  Train & Evaluation

python train.py --dataset <dataset_name>  --cuda 0 --lr 0.001 --mu 0.0001 --dim 256 --dataset DB15K --epochs 2000

You can refer to the training scripts in `scripts/train.sh` to reproduce our experiment results. Here is an example for DB15K dataset.


