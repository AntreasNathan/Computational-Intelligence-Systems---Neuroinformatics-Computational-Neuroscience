from brian2 import *

# Define constants
tau_m = 30*ms  # Membrane time constant
EL = Vreset = -65*mV  # Resting membrane potential and reset potential
Vth = -50*mV  # Threshold potential
Rm = 90*Mohm  # Membrane resistance
Ie_values = [0.5, 1, 1.5, 2]*nA  # Constant input currents
V0 = -67*mV  # Initial membrane potential
TRefract = 2*ms  # Absolute refractory period

# Neuron model equations
eqs = '''
dV/dt = (EL - V + Rm*Ie) / tau_m : volt (unless refractory)
Ie : amp
'''

# Store firing rates for different constant input currents
firing_rates = []

for Ie_value in Ie_values:
    # Initialize neuron group
    G = NeuronGroup(1, eqs, threshold='V>Vth', reset='V=Vreset', method='exact', refractory=TRefract)
    G.V = V0  # Set initial membrane potential
    M = StateMonitor(G, 'V', record=True)  # Monitor membrane potential
    spikemon = SpikeMonitor(G)  # Monitor spikes

    G.Ie = Ie_value  # Set input current
    run(1*second, report='text')  # Simulate for 1 second

    print(f"Time of the first spike with Ie={Ie_value}:", spikemon.t[0])
    # Calculate ISIs
    isis = diff(spikemon.t)
    isi_mean = mean(isis)
    print(f"The mean isi with Ie={Ie_value}:", isi_mean)
    print(f"Number of spikes with Ie={Ie_value}:", len(spikemon.t))

    # Calculate firing rate
    firing_rate = len(spikemon.t) / 1*second
    firing_rates.append(firing_rate)


print(firing_rates)

# Plot firing rate as a function of input current
plot(Ie_values/nA, firing_rates, '-o')
xlabel('Input current (nA)')
ylabel('Firing rate (Hz)')
title('Firing rate vs Input current')
plt.grid(True)
show()