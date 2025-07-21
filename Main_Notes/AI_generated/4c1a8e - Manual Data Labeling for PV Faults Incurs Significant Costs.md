Tags: #PVsystems, #datalabeling, #economics

A substantial portion of the cost associated with supervised learning for PV fault detection comes from the manual labeling of data. 
This is not a simple task; it requires significant time and the involvement of technical experts who can accurately identify and annotate each specific fault type.

This meticulous process must be performed for every distinct fault, from string disconnections to module degradation. 
The high cost of this human-in-the-loop requirement makes it a significant financial barrier, especially when considering the need for ongoing updates to the dataset.

## Sources

- Lu, S., Wang, M., Wei, S., Liu, H., & Wu, C. (2021). Photovoltaic module fault detection based on a convolutional neural network. _Processes, 9_(9), 1635. [https://doi.org/10.3390/pr9091635](https://doi.org/10.3390/pr9091635)
    

## Connections/Related Concepts

- Connects to: [[Data Acquisition and Labeling Costs Challenge Supervised ML in PV Fault Detection]] (This note isolates and details the "labeling" aspect of the overall cost).
    
- Connects to: [[Dynamic Nature of PV Systems Necessitates Costly Model Retraining]] (The cost of labeling is a recurring one because of the need for retraining).
    
- Potential future connections: [[Active Learning for PV Fault Detection]] could be a strategy to minimize the amount of data that needs to be manually labeled.
- Can our approach make the process of labeling exponentially more useful, because more labeling makes the future labeling better by providing more fitting candidates?

---