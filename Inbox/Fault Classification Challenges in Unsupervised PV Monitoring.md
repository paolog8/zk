Tags: #FaultClassification, #UnsupervisedML, #PVSystems

Unsupervised models are inherently limited in their ability to classify the specific type of fault occurring in a PV system. 
Since they do not train on labeled historical data, they cannot distinguish between faults like short-circuits, open-circuits, or arc faults (Rao et al., 2021; Suliman et al., 2024).

These models may successfully group anomalous data points into clusters, but these clusters lack inherent meaning. 
This leaves technicians with the knowledge that _something_ is wrong, but without the crucial information needed to take the correct remedial action (Liu et al., 2024).

## Sources

Rao, S., Muniraju, G., Tepedelenlioğlu, C., Srinivasan, D., TamizhMani, G., & Spanias, A. (2021). Dropout and pruned neural networks for fault classification in photovoltaic arrays. Ieee Access, 9, 120034-120042. https://doi.org/10.1109/access.2021.3108684

Suliman, F., Anayi, F., & Packianather, M. (2024). Electrical faults analysis and detection in photovoltaic arrays based on machine learning classifiers. Sustainability, 16(3), 1102. https://doi.org/10.3390/su16031102

Liu, S., Qi, Y., Ma, R., Liu, L., & Li, Y. (2024). Intelligent fault diagnosis of photovoltaic systems based on deep digital twin. Measurement Science and Technology, 35(7), 076207. https://doi.org/10.1088/1361-6501/ad3bdf

## Connections/Related Concepts

- Connects to: [[Unsupervised ML for PV Fault Detection Lacks Interpretability and Classification]] (This note expands on the classification aspect of the core problem)
    
- Connects to: [[Overlapping Fault Signatures Complicate PV Anomaly Classification]] (Explains a key reason why this challenge exists)
    
- Potential future connections: Semi-supervised learning approaches for fault classification.
    

---