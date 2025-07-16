Tags: #FalsePositives, #UnsupervisedML, #MaintenanceStrategy

A major drawback of using unsupervised models for PV fault detection is their tendency to produce a high rate of false positives. 
These models often misclassify benign anomalies, such as those caused by localized shading or soiling, as critical system faults because they lack the context to interpret them correctly (Harrou et al., 2022; Bouzidi et al., 2024).

The frequent generation of these false alarms creates a significant operational burden on maintenance personnel. 
It forces them to investigate non-existent issues, which wastes time and resources and ultimately reduces trust in the automated fault monitoring system.

## Sources

Harrou, F., Taghezouit, B., Khadraoui, S., Dairi, A., Sun, Y., & Arab, A. (2022). Ensemble learning techniques-based monitoring charts for fault detection in photovoltaic systems. Energies, 15(18), 6716. https://doi.org/10.3390/en15186716

Bouzidi, M., Rahmoune, M., & Nasri, A. (2024). Intelligent fault detection of photovoltaic panel using neural networks. Studies in Engineering and Exact Sciences, 5(1), 3161-3177. https://doi.org/10.54021/seesv5n1-157

## Connections/Related Concepts

- Connects to: [[Normal PV Operational Variations Can Mimic Faults]] (This note describes a primary cause of these false positives)
    
- Connects to: [[Poor ML Interpretability in PV Systems Leads to Inefficient Maintenance]] (False positives are a key driver of inefficient maintenance)
    
- Potential future connections: Techniques for filtering or validating anomalies to reduce false positive rates.
    

---