import numpy as np
import matplotlib.pyplot as plt

# Σταθερές
tau_m = 30  # ms
EL = Vreset = -65  # mV
Vth = -50  # mV
Rm = 90  # MΩ
Ie_values = [0.5, 1, 1.5,2.0] # nA
V0 = -67  # mV
TRefract = 2  # ms
mean_isi = []

def membrane_potential(t, Ie, V0):
    return EL + (Rm * Ie) + (V0 - EL - Rm * Ie) * np.exp(-t / tau_m)

def simulate_spikes(Ie, V0):
    t = 0.0
    temp=0.0
    spikes = 0
    spike_times = []
    #print(Ie)
    #print(V0)
    while t <= 1000:  # Χρονική διάρκεια 1 δευτερόλεπτο σε ms
        #print(V0)
        V = membrane_potential(temp, Ie, V0)
        if V >= Vth:
            #print(V)
            spikes += 1
            spike_times.append(t)
            if(spikes==1):
                print(f"T of First Spike:{t}")
            t += TRefract  # Προσθήκη απόλυτης περιόδου ανάκαμψης
            temp=0
            V0 = EL  # Επαναφορά του δυναμικού μετά τη σπίθα
            #t += 0.0005
            #temp += 0.0005
            #print(t)
        else:
            t += 0.0005  # Χρονικό βήμα στην προσομοίωση
            temp+=0.0005


    isi = np.diff(spike_times)
    mean_isi.append(np.mean(isi))
    return len(spike_times), mean_isi, isi

# Εκτύπωση απαντήσεων στις ερωτήσεις 1-3
k=0
for Ie in Ie_values:
    spikes, mean_isi, isi = simulate_spikes(Ie, V0)
    print(f"Ie = {Ie} nA: Spikes = {spikes}, Mean ISI = {mean_isi[k]} ms")
    k+=1

# Γραφική αναπαράσταση των interspike-interval firing rates (risi)
risi_values = [1000 / isi for isi in mean_isi]  # μετατροπή σε firing rates (Hz)

plt.figure()
plt.plot(Ie_values, risi_values, marker='o')
plt.xlabel('Σταθερό Ρεύμα (nA)')
plt.ylabel('Firing Rate (Hz)')
plt.title('Interspike-Interval Firing Rates')
plt.grid(True)
plt.show()