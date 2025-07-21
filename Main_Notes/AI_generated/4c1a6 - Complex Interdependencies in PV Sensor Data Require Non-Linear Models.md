Tags: #DataComplexity, #NonLinearModels, #PVSystems

Sensor data from PV systems exhibits complex, non-linear interdependencies between its various parameters. 
For instance, the impact of shading on a module's current output is not constant but varies with the module's temperature, creating an intricate relationship that is difficult to model (Hojabri et al., 2022).

Simple linear algorithms are often insufficient to capture these nuances. 
This necessitates the use of more sophisticated and computationally intensive models, such as deep neural networks or advanced ensemble methods, which are capable of deciphering these non-linear patterns (Aziz et al., 2020). ^9a66e3

## Sources

Hojabri, M., Kellerhals, S., Upadhyay, G., & Bowler, B. (2022). Iot-based pv array fault detection and classification using embedded supervised learning methods. Energies, 15(6), 2097. https://doi.org/10.3390/en15062097

Aziz, F., Ul-Haq, A., Ahmad, S., Mahmoud, Y., Jalal, M., & Ali, U. (2020). A novel convolutional neural network-based approach for fault classification in photovoltaic arrays. Ieee Access, 8, 41889-41904. https://doi.org/10.1109/access.2020.2977116

## Connections/Related Concepts

- Connects to: [[High Data Dimensionality and Complexity Challenge ML in PV Fault Detection]] (This note details the "complexity" aspect of the main challenge)
    
- Connects to: [[Ensemble Learning Improves Robustness in PV Fault Detection]] (Ensemble methods are a key solution for this problem)
    
- Potential future connections: Investigating specific non-linear relationships in PV systems.
- [[#^9a66e3]] can outlier scoring function help in extracting relevant representation of the data?
---