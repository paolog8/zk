## 1. Broad Context & Problem Statement

- **The Big Picture:**
    - Increasing reliance on complex industrial systems and critical infrastructure.
    - Growth of renewable energy sources, specifically Photovoltaic (PV) Power Plants.
    - ### 4 - Solar PV Dominates Global Renewable Capacity Growth (IEA 2024)
    -
      New solar capacity is projected to account for 80% of the growth in global renewable power between 2024 and 2030.
      This rapid growth is attributed to declining costs, shorter permitting timelines, and widespread social acceptance.
    - ### 4a - China dominates solar and wind deployment (IEA 2024)

      China has been the primary driver of global renewable additions, accounting for two-thirds of the total in 2023.
      The country has already surpassed its 2030 target for solar PV and wind capacity six years early.
    - ### 4b - Grid Infrastructure Bottlenecks Impede Renewable Energy Deployment (IEA)

      Inadequate investment in grid infrastructure is a critical bottleneck for accelerating renewable energy deployment.
      This challenge is widespread across all country clusters and leads to long connection queues.
      Greater system flexibility is needed to integrate variable renewable energy sources cost-effectively.
      Governments must prioritize modernizing regulatory frameworks and aligning transmission and distribution grid planning to address these issues.
- **Importance of System Health & Reliability:**
    - Consequences of undetected faults: Economic Losses, Safety Hazards, Reduced Efficiency, Environmental Impact.
    - ### 4d1a - Undetected Faults Degrade PV System Health and Reliability (Nieto-Vallejo et al. 2019, Al-Katheri et al. 2022)

      Undetected faults in photovoltaic systems fundamentally undermine their primary function of efficient energy conversion.
      These issues, which range from component degradation to electrical imbalances, directly compromise system health and operational reliability.

      When faults are not identified and rectified, they can lead to significant power losses and shorten the lifespan of the installation.
      Therefore, effective fault detection is not just for maintenance but is essential for ensuring the system's overall efficiency and longevity.
    - ### 4d1a1 - Undetected PV Faults Can Create Significant Safety Hazards (Appiah et al. 2019, Abubakar et al. 2021)

      Beyond power loss and economic impact, undetected faults in PV systems pose serious safety risks.
      If not addressed, minor issues can escalate into catastrophic failures with dangerous consequences.

      Specific hazards include the formation of "hot spots" on modules, often due to cell mismatches, which can become a fire risk.
      Furthermore, deteriorating wiring or faulty connections can lead to electrical shock hazards, endangering maintenance personnel and property.
    - ### 4d1a2 - Undetected PV Faults Cause Economic Losses by Reducing Energy Yield (Davarifar et al. 2013, Bosman et al. 2020)

      The consequences of undetected faults in a PV system extend directly to its economic viability.
      As faults cause the system to degrade and underperform, the resulting energy yield diminishes, which negatively impacts the return on investment (ROI).

      These economic losses are not limited to large-scale installations.
      Smaller PV systems can be especially vulnerable if they are not regularly monitored, as performance decline may be overlooked.
      This can also affect warranty claims and reduce energy credits, adding further financial strain.
    - Crucial role of Effective Fault Detection for operational efficiency and failure prevention.
    - ### 4c1a7 - Continuous PV Monitoring Swiftly Identifies and Corrects Inefficiencies (Bosman et al. 2020)

      Proactive monitoring is essential for maintaining high energy production efficiency in photovoltaic systems. Through the constant assessment of system performance and output, operators can quickly detect anomalies that indicate a loss in efficiency.

      Common causes for such losses include environmental factors like panel soiling or shading, as well as internal operational faults. Early detection enables prompt corrective actions, which restores the system to its optimal performance level and maximizes financial returns, a crucial factor in large-scale solar farms.
    - ### 4c1a7a - Proactive Monitoring Data Informs Strategic PV Investment Decisions (Bosman et al. 2020)

      The real-time performance data gathered from proactive monitoring systems provides a robust basis for strategic planning and investment. This data empowers operators and owners to make more informed, evidence-based decisions regarding their PV assets.

      For example, detailed performance analytics can clarify the need for system upgrades, justify plans for expansion, or help evaluate the potential return on investment for adopting newer, more efficient technologies. Such strategic oversight is critical for navigating the competitive and rapidly evolving renewable energy market.
    - ### 4c1a7b - Proactive Monitoring Enables Predictive Maintenance for PV Systems (Bosman et al. 2020)

      A primary advantage of proactive monitoring is its ability to facilitate predictive maintenance for photovoltaic systems. By continuously analyzing operational data, it becomes possible to anticipate equipment malfunctions and component failures before they happen.

      This foresight allows maintenance to be scheduled at the most opportune times, minimizing system downtime and preventing significant losses in energy production. Adopting a predictive strategy not only reduces operational costs but can also substantially extend the lifespan of PV system components.
    - ### 4c1a7c - Proactive Monitoring Optimizes Photovoltaic System Performance (Bosman et al. 2020)

      Proactive monitoring of photovoltaic systems is a foundational strategy for maximizing their performance, longevity, and energy output. It involves using advanced technologies to collect and analyze system data in real-time.

      This approach enables operators to identify and address potential issues before they escalate into significant failures. By catching problems early, operators can ensure the system functions optimally, enhancing overall energy yield and ensuring its long-term health and reliability.
    - ### 4c1a7d - PV System Monitoring Ensures Compliance with Warranty Conditions (Bosman et al. 2020)

      Effective monitoring of a photovoltaic system is a critical tool for managing and enforcing warranty agreements. Equipment warranties are often contingent on the system meeting specific performance benchmarks and operational standards.

      Proactive monitoring creates a continuous and detailed log of the system's performance, providing clear evidence that these contractual benchmarks are being met. This documentation is invaluable for substantiating warranty claims if a component fails or underperforms, thereby protecting the owner's financial investment.
## 2. Specific Challenges in Fault Detection
- **Data Characteristics Challenges:**
    - Scarcity of Labeled Fault Data (rare events).
        - ### 4c1a8 - Data Acquisition and Labeling Costs Challenge Supervised ML in PV Fault Detection (Gaaloul et al. 2025, Behrends et al. 2022)

          Traditional supervised machine learning approaches for photovoltaic fault detection are significantly challenged by the high costs and logistical hurdles associated with data.
          The necessity for extensive, accurately labeled datasets creates a primary barrier to entry and effective deployment.

          Acquiring and labeling data for the wide array of potential faults is a resource-intensive process.
          This fundamental difficulty complicates the development of robust models and underscores the need for methods that less dependent on perfectly curated datasets.
        - ### 4c1a8a - Data Acquisition for PV Faults is Complex and Resource-Intensive (Gaaloul et al. 2025)

          The process of acquiring high-quality data for PV fault detection is inherently complex and requires significant resources.
          Faults are often identified through indirect indicators like power loss or voltage errors, which necessitates the use of precisely calibrated sensors and robust data collection protocols.

          This complexity is magnified by the potential for sensor error, such as a misaligned pyranometer providing inaccurate solar irradiation data.
          Correcting for such issues adds another layer of difficulty and cost to the data acquisition process, making it a major operational challenge for large-scale PV systems.
        - ### 4c1a8e - Manual Data Labeling for PV Faults Incurs Significant Costs (Lu et al. 2021)

          A substantial portion of the cost associated with supervised learning for PV fault detection comes from the manual labeling of data.
          This is not a simple task; it requires significant time and the involvement of technical experts who can accurately identify and annotate each specific fault type.

          This meticulous process must be performed for every distinct fault, from string disconnections to module degradation.
          The high cost of this human-in-the-loop requirement makes it a significant financial barrier, especially when considering the need for ongoing updates to the dataset.
        - ### 4c1a8h - Scarcity of Labeled Data Hinders Advanced ML Adoption in PV Systems (Garoudja et al. 2017, Al-Obaidi & Derbel 2023)

          A major barrier to implementing more advanced machine learning (ML) fault detection systems in PV applications is the scarcity of extensive, high-quality labeled datasets.
          While techniques like Convolutional Neural Networks (CNNs) show promise, their effectiveness is contingent upon large volumes of labeled data for training (Garoudja et al., 2017; Al-Obaidi & Derbel, 2023).

          Obtaining comprehensive, real-time data that covers a wide array of fault types and environmental conditions is difficult and costly.
          This data scarcity limits the ability of traditional and even some advanced models to adapt to new or previously unencountered fault scenarios, creating a bottleneck for the development of truly robust and intelligent detection systems.
        - ### 4c1a8i - Scarcity of Labeled Data Impedes PV Fault Detection Model Development (Jaskie et al. 2021, Wu et al. 2023)

          A significant barrier to improving fault detection in photovoltaic systems is the scarcity of comprehensive, labeled fault data.
          As PV installations become more common, the need for effective fault management grows, yet collecting diverse and accurately labeled datasets that capture the full range of real-world fault scenarios remains a major challenge.

          This lack of sufficient labeled data directly hampers the development and training of effective machine learning (ML) models.
          Without robust datasets, creating reliable and accurate automated fault detection and diagnosis systems is difficult.
    - High Dimensionality and Complexity of Sensor Data.
        - ### 4c1a10 - High Data Dimensionality and Complexity Challenge ML in PV Fault Detection (Badr et al. 2021, Et-taleby et al. 2023)

          Machine learning (ML) for fault detection in photovoltaic systems is challenged by high-dimensional and complex sensor data.
          The multitude of interacting environmental and electrical parameters generates convoluted datasets that complicate accurate modeling.

          These characteristics increase computational demands and elevate the risk of model overfitting, where the model learns noise instead of true patterns (Badr et al., 2021; Et-taleby et al., 2023).
          Effectively managing these data challenges is crucial for developing reliable ML-based fault detection systems.
        - ### 4c1a1a - Curse of Dimensionality in PV System Data (Thakfan & Salamah 2024, Quiles et al. 2025)

          Photovoltaic systems utilize numerous sensors, resulting in high-dimensional datasets with many features (Thakfan & Salamah, 2024).
          This volume of data can lead to the "curse of dimensionality," a state where the feature space becomes so vast and sparse that ML models struggle to find meaningful patterns.

          This sparsity increases the likelihood of overfitting, where the model learns noise instead of true patterns (Quiles et al., 2025).
          Consequently, the model's ability to generalize and make accurate predictions on new, unseen data is significantly diminished.
        - ### 4c1a6 - Complex Interdependencies in PV Sensor Data Require Non-Linear Models (Hojabri et al. 2022, Aziz et al. 2020)

          Sensor data from PV systems exhibits complex, non-linear interdependencies between its various parameters.
          For instance, the impact of shading on a module's current output is not constant but varies with the module's temperature, creating an intricate relationship that is difficult to model (Hojabri et al., 2022).

          Simple linear algorithms are often insufficient to capture these nuances.
          This necessitates the use of more sophisticated and computationally intensive models, such as deep neural networks or advanced ensemble methods, which are capable of deciphering these non-linear patterns (Aziz et al., 2020).
        - ### 4c1a9 - Heterogeneous Data from PV Systems Challenges Traditional ML Models (Hojabri et al. 2022, Dhimish et al. 2017, Al-Obaidi & Derbel 2023)

          Traditional machine learning (ML) models face significant challenges when applied to fault detection in photovoltaic (PV) systems due to the heterogeneous nature of the data.
          This data is a complex mix of signals influenced by fluctuating irradiance, temperature, and shading, alongside inherent noise and inconsistencies from various sensors (Hojabri et al., 2022).

          This variability makes it difficult for fixed algorithms to perform reliably, as different faults can manifest uniquely under different operational states (Dhimish et al., 2017).
          Even advanced deep learning techniques require extensive preprocessing to extract relevant features from this complex data, highlighting a fundamental hurdle in creating robust detection systems (Al-Obaidi & Derbel, 2023).
    - Dynamic Operating Conditions and their impact on data.
        - ### 4c1b - Dynamic Operating Conditions in PV Systems Cause False Positives (Jaskie et al. 2021)

      The dynamic operating conditions of photovoltaic (PV) systems, particularly fluctuating sunlight and shading, are a primary source of false positives in fault detection algorithms.
      These environmental changes can cause significant variations in power output that traditional ML models mistake for actual system faults (Jaskie et al., 2021).

      Many conventional algorithms fail because they treat each data point in isolation, without considering the system's historical performance or the broader environmental context.
      This lack of temporal and contextual awareness makes it difficult to distinguish between a genuine fault and a normal response to a change in conditions, such as a passing cloud.
        - ### 4c1b1 - Environmental Factors Complicate PV Fault Classification (Zhang et al. 2021)

      The challenge of classifying PV faults with unsupervised models is made even more difficult by environmental factors.
      Conditions such as partial shading from clouds or physical soiling of panels create fault signatures that are highly variable and dependent on local conditions (Zhang et al., 2021).

      An unsupervised model that is not designed to explicitly account for these complex and dynamic environmental inputs will have limited success in accurately classifying the anomalies it detects.
      What might be classified as a component failure could simply be the effect of a passing cloud, leading to inaccurate diagnoses.
        - ### 4c3 - Variable Environmental Conditions Can Mask PV System Faults (Basnet et al. 2020, Li et al. 2021)

          The accurate detection of faults in a PV system can be complicated by environmental factors.
          In particular, inconsistent solar irradiation can obscure the performance data that would typically indicate a fault.

          For example, a drop in power output caused by a hardware fault might be mistaken for a cloudy day.
          This masking effect makes it harder to diagnose underlying issues, allowing them to persist and worsen without intervention, especially in systems without advanced monitoring.
- **Limitations of Traditional Approaches:**
    - **Supervised Methods:**
        - Requirement for Extensive Labeled Data.
            - ### 4c1a8l - Supervised Learning for PV Fault Detection is Limited by Labeled Data Dependency (Islam et al. 2023, Zgraggen et al. 2022)

              While supervised machine learning is a powerful approach for fault detection in photovoltaic systems, its effectiveness is fundamentally constrained by its dependence on large, well-labeled datasets.
              The process of collecting and accurately labeling data for the myriad of potential faults is both costly and labor-intensive.

              This dependency creates a significant practical bottleneck.
              The difficulty in obtaining comprehensive labeled datasets that cover all operational and environmental conditions limits the real-world efficacy and reliability of purely supervised fault detection models.
        - Challenges in Data Acquisition and Labeling Cost.
            - ### 4c1a8c - Dynamic Nature of PV Systems Necessitates Costly Model Retraining (Lu et al. 2021)

              The operational environment of a photovoltaic (PV) system is not static.
              System configurations can change, and new, previously unseen fault types can emerge over time.
              This dynamic nature poses a challenge for supervised learning models, which may experience performance degradation as the real-world conditions diverge from their original training data.

              To maintain accuracy and reliability, these models require constant retraining with newly collected and labeled data.
              This creates a continuous cycle of resource expenditure, as the costs associated with data acquisition and labeling are not a one-time investment but an ongoing operational necessity.
            - ### 4c1a8d - Inadequate Training Data Limits ML Model Effectiveness in PV Fault Detection (Elkalashy & Taha 2022)

              The effectiveness of machine learning (ML) models in PV fault detection is critically dependent on the quality and comprehensiveness of the training data.
              A significant challenge is that models trained on a limited set of fault types become specialized and may fail to recognize new or uncommon faults accurately (Elkalashy & Taha, 2022).

              If the training dataset does not include examples of certain faults or neglects the impact of various component failures, the resulting model will have blind spots.
              This vulnerability means the model may perform well in test scenarios but fail when deployed in a real-world environment where unexpected fault conditions can and do occur.
            - ### 4c1a8f - Poor Generalization in PV Fault Models is a Consequence of Labeled Data Scarcity (Voutsinas et al. 2023, Liu et al. 2024)

              Machine learning models trained on inadequate labeled data for photovoltaic fault detection often exhibit poor generalization.
              This means they perform poorly when encountering fault conditions that were not well-represented in their limited training data.

              This issue stems from datasets that are either too small or lack examples of all potential fault types, leading to inherent biases in the model.
              As a result, these models are prone to high rates of false positives and false negatives in real-world applications, making their diagnostic output unreliable.
            - ### 4c1a8m - Supervised PV Fault Detection Models Suffer from Overfitting Due to Incomplete Datasets (Eldeghady et al. 2024, Aziz et al. 2020)

              A primary drawback of using supervised learning for PV fault detection is the high risk of model overfitting.
              This occurs when the model learns the training data too well, including its noise and biases, because the dataset is not diverse enough to represent all possible real-world scenarios.

              This overfitting leads to poor generalization, meaning the model fails to accurately identify faults it has not explicitly seen during training.
              As a result, the system's reliability is compromised, often producing high rates of false positives or negatives when deployed in a live operational environment.
    - **Purely Unsupervised Methods:**
        - Strengths in Anomaly Detection.
            - Strengths in Anomaly Detection.
            - ### 4c1a20 - Unsupervised Learning Enables Comprehensive PV Fault Detection

              Unsupervised algorithms are essential for effective fault detection systems.
              Unlike supervised methods that rely on pre-labeled data, unsupervised approaches can identify any relevant deviation from normal operating conditions.
              This capability is crucial for real-world applications, where it's impossible to train a system on every conceivable fault.
              By detecting novel anomalies, unsupervised learning ensures a robust and adaptable fault detection system that remains relevant over time.
            - ### 4c1a21 - Unsupervised Learning Excels at Identifying Novel or Undocumented PV Faults (Zhang et al. 2021)

              A significant advantage of unsupervised fault detection methods is their ability to identify fault types that are novel, poorly understood, or not previously documented.
              This capability stems from their fundamental approach of detecting anomalies rather than searching for specific, pre-defined fault signatures.

              Because these models define a baseline of normal operation, any significant deviation is flagged as a potential issue.
              This allows operators to discover emerging or unexpected failure modes without the need for prior data collection and labeling specific to that fault (Zhang et al., 2021).
            - [[4c1a22 - Unsupervised ML in PV Systems Detects Faults by Identifying Anomalies from a Normal Baseline]]
        - Limitations in Fault Interpretability and Fault Type Classification.
            - Limitations in Fault Interpretability and Fault Type Classification.
            - ### 4c1a5b - Fault Classification Challenges in Unsupervised PV Monitoring (Rao et al. 2021, Suliman et al. 2024, Liu et al. 2024)

              Unsupervised models are inherently limited in their ability to classify the specific type of fault occurring in a PV system.
              Since they do not train on labeled historical data, they cannot distinguish between faults like short-circuits, open-circuits, or arc faults (Rao et al., 2021; Suliman et al., 2024).

              These models may successfully group anomalous data points into clusters, but these clusters lack inherent meaning.
              This leaves technicians with the knowledge that _something_ is wrong, but without the crucial information needed to take the correct remedial action (Liu et al., 2024).
            - ### 4c1a5b1 - Overlapping Fault Signatures Complicate PV Anomaly Classification (Suliman et al. 2024)

              A primary reason unsupervised models struggle to classify PV faults is that different fault types often exhibit similar electrical signatures, especially in their early stages.
              Conditions like short-circuits, open-circuits, and degradation can produce overlapping patterns in operational data, such as current-voltage (I-V) characteristics (Suliman et al., 2024).

              Because these models rely solely on analyzing the data's features to find deviations, they cannot easily distinguish between two different problems that look alike from a data perspective.
              This inherent ambiguity leads to misclassifications and undermines the reliability of the fault detection system.
            - ### 4c1a5b2 - Poor ML Interpretability in PV Systems Leads to Inefficient Maintenance (Rao et al. 2021, Liu et al. 2024)

              The lack of clear interpretation from unsupervised fault detection models has direct negative consequences for PV system maintenance.
              The inability to understand the physical cause behind a flagged anomaly can lead to a high rate of false positives, where harmless operational deviations are mistaken for faults (Rao et al., 2021).

              This ambiguity forces operators into a difficult position.
              They may perform unnecessary maintenance, wasting resources, or delay action due to uncertainty, which can lead to extended system downtime (Liu et al., 2024).
              Ultimately, this fosters a reactive, rather than proactive, maintenance strategy.
            - ### 4c1a5b3 - Unsupervised ML for PV Fault Detection Lacks Interpretability and Classification (Voutsinas et al. 2023)

              Unsupervised machine learning models are effective for identifying anomalies in photovoltaic system data without needing pre-labeled examples.
              However, their primary weakness lies in their inability to explain _why_ an anomaly was flagged or to classify the specific _type_ of fault.

              This limitation hinders effective decision-making and operational management of PV systems (Voutsinas et al., 2023).
              While they can detect deviations, they cannot inherently provide the actionable insights needed for targeted maintenance.
            - ### 4c1a5c - Interpretability Gap in Unsupervised Models for PV Faults (Voutsinas et al. 2023)

              A significant challenge with using unsupervised learning for PV fault detection is the difficulty in interpreting the results.
              Models like one-class SVM or clustering can flag data that deviates from a normal operational baseline but do not intrinsically explain the physical cause of the anomaly (Voutsinas et al., 2023).

              This "interpretability gap" means operators receive an alert without understanding the underlying issue.
              To make the model's findings actionable, the system often requires additional interpretative frameworks or the integration of human expert knowledge to translate the abstract anomaly signal into a concrete maintenance task.
        - Problem of distinguishing Critical Faults vs. Normal Variations.
            - ### 4c1b2 - High False Positive Rate is a Key Limitation of Unsupervised PV Fault Detection (Basnet et al. 2020)

              A primary challenge in using unsupervised models for photovoltaic fault detection is their potential for a high rate of false positives.
              The anomalies identified by the model do not always correspond to actual system faults.

              These false alarms can be triggered by benign operational variances or sensor noise that the model misinterprets as a fault.
              This can lead to unnecessary and costly maintenance actions, reducing the overall efficiency and practicality of the system (Basnet et al., 2020).
              Careful model tuning and feature selection are required to mitigate this issue.
            - ### 4c1b2a - High Rate of False Positives in Unsupervised PV Fault Detection (Harrou et al. 2022, Bouzidi et al. 2024)

              A major drawback of using unsupervised models for PV fault detection is their tendency to produce a high rate of false positives.
              These models often misclassify benign anomalies, such as those caused by localized shading or soiling, as critical system faults because they lack the context to interpret them correctly (Harrou et al., 2022; Bouzidi et al., 2024).

              The frequent generation of these false alarms creates a significant operational burden on maintenance personnel.
              It forces them to investigate non-existent issues, which wastes time and resources and ultimately reduces trust in the automated fault monitoring system.
            - ### 4c1b2b - Normal PV Operational Variations Can Mimic Faults (Rao et al. 2021, García et al. 2022, Raslan & Çam 2020)

              The performance of photovoltaic systems naturally fluctuates due to changing environmental conditions, such as solar irradiance and ambient temperature.
              These normal operational variances can produce data signatures that closely resemble those of actual faults, confusing unsupervised anomaly detection algorithms (Rao et al., 2021; García et al., 2022).

              This mimicry makes it difficult for a purely data-driven model to delineate between a critical failure and a normal response to the environment (Raslan & Çam, 2020).
              Without the ability to account for these benign fluctuations, models can inaccurately flag normal conditions as faults, undermining their reliability.
            - ### 4c1b2c - Sensor Noise in PV Systems Can Mimic Fault Signatures (Punitha et al. 2024, Syed et al. 2024)

              Noise within sensor data is a significant obstacle for machine learning algorithms in PV systems.
              Transient environmental factors, such as a cloud momentarily passing over a panel, can cause fluctuations in the data that closely mimic the signature of a genuine equipment fault (Punitha et al., 2024; Syed et al., 2024).

              This similarity can easily mislead a fault detection model into making an incorrect classification.
              As a result, the system may generate a false alarm, flagging a benign event as a critical failure and prompting unnecessary investigation or maintenance actions.
            - ### 4c1b2d - Unsupervised Models Struggle to Distinguish Critical PV Faults from Normal Variations (Raslan & Çam 2020)

              A core challenge for unsupervised machine learning models in photovoltaic fault detection is their inability to reliably distinguish between critical system faults and benign, normal variations in operational performance.
              These models can flag anomalies but often lack the necessary context to determine if a deviation is a genuine threat or a harmless fluctuation (Raslan & Çam, 2020).

              This fundamental difficulty can lead to misinterpretation of alerts.
              It underscores the limitation of relying purely on statistical methods without incorporating more nuanced domain knowledge about the system's operational environment and fault characteristics.
            - ### 4c1b3 - High Rate of False Negatives in Unsupervised PV Fault Detection (Han et al. 2025, Han et al. 2024)

              In addition to false positives, unsupervised models for PV fault detection are also prone to false negatives, where a genuine fault goes undetected.
              This is particularly dangerous with incipient faults, as their subtle early signals can be lost within the patterns of normal operational data, causing the model to overlook them (Han et al., 2025).

              The failure to consistently identify these nuanced deviations that signal a developing problem is a critical weakness (Han et al., 2024).
              A single false negative can allow a serious fault to develop unnoticed, increasing the risk of major system failure, safety hazards, and compromised energy production.
            - ### 4c1b3a - Unsupervised Models May Miss Subtle Incipient Faults in PV Systems (Han et al. 2024)

              Incipient faults—those in their earliest stages—are particularly challenging for unsupervised models to detect in PV systems.
              The initial symptoms often manifest as very small deviations from normal operational data, making them easily confusable with standard system noise (Han et al., 2024).

              Because unsupervised models lack historical, labeled examples of how faults develop, they may fail to capture these subtle but critical precursor patterns.
              This can lead to a failure to provide early warnings, allowing a minor issue to escalate into a significant failure before it is identified.