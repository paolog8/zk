Tags: #HybridModel, #PVFaultDetection, #MachineLearning

A promising strategy for improving the accuracy and reliability of PV fault detection is to create hybrid models that integrate both unsupervised and supervised machine learning techniques. 
This approach leverages the distinct strengths of each methodology.

In a typical hybrid system, an unsupervised model is first used to perform broad anomaly detection, flagging any data that deviates from the norm. 
These potential faults are then passed to a supervised model, which classifies the specific type of fault, thereby reducing false positives and providing more detailed diagnostics (Voutsinas et al., 2023; Lin et al., 2025).

## Sources

- Voutsinas, S., Karolidis, D., Voyiatzis, I., & Σαμαράκου, Μ. (2023). Development of a machine-learning-based method for early fault detection in photovoltaic systems. _Journal of Engineering and Applied Science_, 70(1). [https://doi.org/10.1186/s44147-023-00200-0](https://doi.org/10.1186/s44147-023-00200-0)
    
- Lin, B., Zheng, M., Shao, J., & Hu, K. (2025). Automatic intelligent operation and maintenance system for photovoltaic panel failure of photovoltaic power stations. _Journal of Physics Conference Series_, 2993(1), 012005. [https://doi.org/10.1088/1742-6596/2993/1/012005](https://doi.org/10.1088/1742-6596/2993/1/012005)
    

## Connections/Related Concepts

- Connects to: [[High False Positive Rate is a Key Limitation of Unsupervised PV Fault Detection]] (This note presents a solution to that problem)
    
- Connects to: [[Unsupervised ML for PV Fault Detection Overcomes Labeled Data Scarcity]] (This approach still minimizes the need for comprehensive labeled data by using it only in the second stage)
    
- Potential future connections: Investigating the architecture of effective hybrid fault detection systems.