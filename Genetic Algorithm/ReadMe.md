# Genetic Algorithm Model – Computational Intelligence Systems  
**Topic:** Neuroinformatics / Computational Neuroscience  

This project implements a **Genetic Algorithm (GA)** in Python to optimize a function with two variables (`x1`, `x2`). Candidate solutions are encoded as binary genotypes, evaluated for fitness, and evolved using selection, crossover, and mutation.  

---

## Implementation
- **Language:** Python 3  
- **Libraries:** `numpy`, `math`, `random`  
- **Execution:**  
  ```bash
  python3 assignment4_genetic_algorithm.py

## Results from Execution

Genotype in Binary x1 x2 Fitness Normalized Fitness
Genotype (Binary)    x1     x2     Fitness    Normalized Fitness
----------------------------------------------------------------
01010010000110      -1.8   -4.5    52.13         0.04
11111010000110       4.8   -4.5    68.31         0.05
11110010001111       4.5   -3.8    60.74         0.05
00010110001111      -4.1   -3.8    40.81         0.03
00010110000110      -4.1   -4.5    60.77         0.05
11110110000110       4.7   -4.5    76.27         0.06
00000010000110      -4.9   -4.5    65.77         0.05
01110000001110      -0.6   -3.9    35.96         0.03
11010010000110       3.3   -4.5    62.14         0.05
00010010000110      -4.3   -4.5    71.33         0.06
00010010000111      -4.3   -4.4    70.26         0.06
01000010000111      -2.4   -4.4    63.19         0.05
11110010000110       4.5   -4.5    80.70         0.06
00000010000111      -4.9   -4.4    64.70         0.05
10010010010110       0.7   -3.3    32.47         0.03
00000010000110      -4.9   -4.5    65.77         0.05
00100110000110      -3.5   -4.5    72.62         0.06
11110010000110       4.5   -4.5    80.70         0.06
00010010000110      -4.3   -4.5    71.33         0.06
00100110000110      -3.5   -4.5    72.62         0.06

**Best Genotype (Binary): 11110010000110**
**Best Phenotype: x1 = 4.5, x2 = -4.5**
**Best Fitness: 80.69849126150926**