# Supplementary Materials for Periodic Distinguishers on LBlock and TWINE

This directory contains the Python implementations supporting the paper *"Improved Periodic Distinguishers for LBlock and TWINE"*.

## Directory Structure

```
.
├── Classical implementation/   # Classical distinguishing attacks (Algorithm 2)
│   ├── LBlock_9r_classical.py
│   ├── LBlock_10r_classical.py
│   ├── LBlock_11r_classical.py
│   ├── TWINE_9r_classical.py
│   ├── TWINE_10r_classical.py
│   └── TWINE_11r_classical.py
├── Probability verification/   # Empirical verification of periodic properties
│   ├── LBlock_9r_p0.py
│   ├── LBlock_10r_p8.py
│   ├── LBlock_11r_p20.py
│   ├── TWINE_9r_p0.py
│   ├── TWINE_10r_p8.py
│   └── TWINE_11r_p20.py
├── lblock10.pdf              # Route diagram of the 10-round LBlock periodic distinguisher
└── TWINE10.pdf               # Route diagram of the 10-round TWINE periodic distinguisher
```

## Requirements

- Python 3.x
- `tqdm` (for progress bars in classical implementation scripts)

Install dependencies via:
```bash
pip install tqdm
```

## Description

### Classical Implementation

The scripts in `Classical implementation/` implement **Algorithm 2** (Classical Distinguishing Attack by Detecting the Period) described in Section 3.3 of the paper. Each script executes the full attack procedure for the corresponding cipher and round number:

- **LBlock**: 9-round (polynomial-time), 10-round ($p=4$), and 11-round ($p=12$) distinguishers.
- **TWINE**: 9-round (polynomial-time), 10-round ($p=4$), and 11-round ($p=12$) distinguishers.

Each script used randomized round keys and plaintext. Upon success, it outputs the detected period and the query complexity. The reported query count is smaller than the worst-case data complexity $T$ given in the paper, because $T$ is an upper bound derived for the worst-case branch ($d=7$) while the actual execution may follow the more favorable branch.

### Probability Verification

The scripts in `Probability verification/` empirically validate the existence of the periodic function by exhaustive search over the input space. For a given randomly chosen key and controlled constants $(\alpha_0, \alpha_1)$, the scripts evaluate the output difference at the target branch position for all values of the periodic variable $x$ and check whether the predicted period $s$ is satisfied.

These scripts are used to confirm the correctness of the differential separability property and the refined propagation rules (Section 3.2) for the reported distinguishers.

## Usage

Run any script directly with Python. No command-line arguments are required; all parameters are hard-coded according to the values stated in the paper.

**Classical implementation:**
```bash
python "Classical implementation/LBlock_9r_classical.py"
python "Classical implementation/LBlock_10r_classical.py"
python "Classical implementation/LBlock_11r_classical.py"
python "Classical implementation/TWINE_9r_classical.py"
python "Classical implementation/TWINE_10r_classical.py"
python "Classical implementation/TWINE_11r_classical.py"
```

**Probability verification:**
```bash
python "Probability verification/LBlock_9r_p0.py"
python "Probability verification/LBlock_10r_p8.py"
python "Probability verification/LBlock_11r_p20.py"
python "Probability verification/TWINE_9r_p0.py"
python "Probability verification/TWINE_10r_p8.py"
python "Probability verification/TWINE_11r_p20.py"
```

## Notes

- The S-box definitions follow the original LBlock and TWINE specifications.
