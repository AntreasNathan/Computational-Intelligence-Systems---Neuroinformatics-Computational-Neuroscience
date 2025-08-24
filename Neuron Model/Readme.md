# Spiking Neuron Models – Computational Intelligence Systems  
**Topic:** Neuroinformatics / Computational Neuroscience  

This project explores spiking neuron models, focusing on the simulation of action potentials, spike timing, and firing frequency under different input currents. The work was implemented both in **pure Python** and using the **Brian2 simulator**, with results compared for consistency.  

---

## Part A – Python Implementation
The neuron model was implemented in Python and executed on Google Colaboratory.  

### Results
1. **First spike time:** 6.1295 ms  
2. **Mean inter-spike interval (ISI):** 7.4695 ms  
   - Computed by summing all ISIs and dividing by the number of spikes.  
   - Verified using the theoretical equation.  
   (imgs/equation.png)
3. **Number of spikes (0–1 s):** 134  
4. **Observation:** The firing frequency **increases drastically** when the input current is raised.  

(imgs/interspike-interval Firing Rate.png)

---

## Part B – Brian2 Implementation
The same experiment was reimplemented using the [Brian2](https://brian2.readthedocs.io/en/stable/) simulator for spiking neural networks.  

### Results
- **First spike time:** ≈ 6.1 ms  
- **Mean ISI:** ≈ 7.4 ms  
- **Number of spikes (0–1 s):** 134

We observe that the frequency increases drastically when we increase the input current.

(imgs/interspike-interval Firing Rate Brian2.png)

---

## Comparative Analysis
Below are the program responses using brian2. As can be seen from the graph, the results of the two programs are in agreement. For questions 1, 2 and 3, it is clear from the responses that the two programs are in agreement since for Ie=1 the time to the first spike is 6.1, the average isi is 7.4 and the number of spikes for sec 0-1 is 135. The small differences that exist may be due to decimal operations or to the fact that Brian2 may have a different implementation for the membrane potential.

---

## Files
- `neuron_model.py` – Python implementation.  
- `neuron_model_brian2.py` – Brian2 implementation. 

---

## Requirements
- Python 3.x  
- NumPy, Matplotlib  
- Brian2  

### Run
```bash
# Python model
python neuron_model.py

# Brian2 simulation
python neuron_model_brian2.py
