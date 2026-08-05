# ML Defect Detection Roadmap

> Goal: Build a clean, production-style binary image classification
> pipeline for surface crack detection.

## Phase 0 --- Project Setup

-   [x] Create Git repository
-   [x] Docker development environment
-   [x] Project structure
-   [x] Download Kaggle dataset
-   [x] Basic EDA notebook

> struggles: docker dependencies, notebook conventions
------------------------------------------------------------------------

## Phase 1 --- Data Pipeline

### Dataset organization

-   [x] Split train / validation / test
-   [x] Reproducible split (fixed seed)
-   [x] Preserve class folders
-   [x] Prevent duplicate copies

### Image loading

-   [x] `dataset.py`
-   [x] Implement custom `torch.utils.data.Dataset`

> learned: dataset returns a single sample.
### Preprocessing

-   [x] `transforms.py`
-   [x] Read image
-   [x] BGR → RGB
-   [x] Resize
-   [x] Normalize

> learned: compute dataset mean/std from the training set for normalization.
### Data augmentation

-   [x] Train transforms
-   [x] Validation transforms
-   [x] Test transforms

### DataLoader

-   [x] Batch loading
-   [x] Shuffle
-   [x] Multiple workers
-   [x] Pin memory

> learned:
> dataloader batches multiple samples.
> multiple workers use multipler cpu processes to prepare batches, keeping GPU is busy.
> pin memory speeds up data transfer from CPU RAM to GPU VRAM.
------------------------------------------------------------------------

## Phase 2 --- Baseline Model

### Model
- [ ] Build Simple CNN
- [ ] Forward pass
- [ ] Verify output shape

### Training
- [ ] Loss function
- [ ] Optimizer
- [ ] Training loop
- [ ] Validation loop

### Checkpoint
- [ ] Save best model
- [ ] Load checkpoint

------------------------------------------------------------------------

## Phase 3 --- Evaluation

-   [ ] Accuracy
-   [ ] Precision
-   [ ] Recall
-   [ ] Validation loss curve
-   [ ] F1 Score
-   [ ] Confusion Matrix
-   [ ] Misclassified image visualization

------------------------------------------------------------------------

## Phase 4 --- Improve Model

-   [ ] Data augmentation experiments
-   [ ] Learning-rate scheduling
-   [ ] Early stopping
-   [ ] Transfer learning (ResNet)

------------------------------------------------------------------------

## Phase 5 --- Inference

-   [ ] Predict single image
-   [ ] Batch prediction
-   [ ] Visualization

------------------------------------------------------------------------

## Phase 6 --- Deployment

-   [ ] Export model
-   [ ] Inference script
-   [ ] Docker inference image

------------------------------------------------------------------------

## Git Branch Plan

-   [x] feature/docker-setup
-   [x] feature/data-pipeline
-   [x] feature/dataset
-   [ ] feature/model
-   [ ] feature/training
-   [ ] feature/evaluation
-   [ ] feature/inference

------------------------------------------------------------------------

## Current Progress

**Completed:** Phase 0 + Phase 1

**Current focus:** Build the first CNN baseline model.

**Next milestone:** Train the first CNN and verify the training pipeline.
