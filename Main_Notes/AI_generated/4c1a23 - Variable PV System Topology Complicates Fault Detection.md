Tags: #SystemTopology, #FaultPropagation, #PVFaultDetection

The variable and interconnected topology of photovoltaic (PV) systems adds a layer of complexity to fault detection. 
A fault in a single module can propagate through the circuit, altering the electrical characteristics of the entire system in ways that are difficult to predict (Dhimish & Chen, 2019).

Traditional ML methods that rely on monitoring individual, isolated data points often fail to capture this systemic perspective. 
They may overlook simultaneous fault scenarios or misinterpret the system's true condition because they do not account for how faults can dynamically interact and spread across the interconnected array.

## Sources

Dhimish, M. and Chen, Z. (2019). Novel open-circuit photovoltaic bypass diode fault detection algorithm. _Ieee Journal of Photovoltaics, 9_(6), 1819-1827. [https://doi.org/10.1109/jphotov.2019.2940892](https://doi.org/10.1109/jphotov.2019.2940892)

## Connections/Related Concepts

- Connects to: [[Complex Interdependencies in PV Sensor Data Require Non-Linear Models]] (The topological effects are a physical manifestation of data interdependencies)
    
- Connects to: [[Unsupervised Models Struggle to Distinguish Critical PV Faults from Normal Variations]]
    
- Potential future connections: Exploring graph neural networks (GNNs) to model the PV system's topology and fault propagation paths.
    

---