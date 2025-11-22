📅 Capstone Project Execution Plan: 1-Click CAD-to-Simulation
This file serves as a high-level timeline and a live task board template for the capstone project. Checkboxes should be marked with [x] when completed.
🎯 Semester-Based Project Timeline (Milestone Tracking)
The project is structured across the remaining three semesters, focusing on a clear progression from data setup to final integration and delivery.
Semester
Phase Goal
Key Tasks & Milestones
Deliverables
Status
6th Semester: Data Foundation & CAD Automation
Focus: Establish the automated pipeline for data generation (CAD to FEA results).
- [ ] A. Add-in Setup: Basic Fusion 360 Add-in structure and initial Python environment setup.
Initial Add-in folder and manifest.
TODO




- [ ] B. Parametric CAD Scripting: Develop scripts to automatically generate the design space (e.g., L-brackets) based on input parameters.
Parameterized geometry generation script.
TODO




- [ ] C. Automated FEA: Script Fusion API to apply boundary conditions, run cloud simulation, and export results (VTU files) for each generated geometry.
FEA automation script (BCs and Solve).
TODO




- [ ] D. Data Factory: Develop VTU parsing and tensor conversion scripts to create the labeled training dataset.
Minimum Viable Dataset (MVD) - 500+ labeled pairs.
TODO
7th Semester: Deep Learning Model Development
Focus: Train, validate, and host the surrogate model for fast inference.
- [ ] A. Model Architecture: Finalize the DLSM architecture (e.g., U-Net or PINN) for stress field prediction.
Model definition and architecture documentation.
TODO




- [ ] B. Model Training: Train the DLSM using the Data Factory dataset, focusing on achieving high validation accuracy (>90%).
Trained model checkpoint (.pth or .h5).
TODO




- [ ] C. Inference Backend: Set up a lightweight, local Python service (e.g., FastAPI) to host the model for sub-second inference.
Local inference API endpoint operational.
TODO




- [ ] D. Integration Mockup: Test the communication link: Add-in sends parameters, Backend returns a mock stress tensor.
Successful communication handshake proof-of-concept.
TODO
8th Semester: Integration, Refinement & Delivery (Final)
Focus: Seamless integration, robust testing, documentation, and final presentation.
- [ ] A. Full Integration: Connect the Fusion 360 Add-in UI/geometry input to the live DL Inference Backend.
Functional "1-Click" stress prediction.
TODO




- [ ] B. Visualization: Implement custom visualization logic within Fusion 360 to display the predicted stress field (color mapping) accurately and quickly.
Accurate 3D visualization of predicted stress.
TODO




- [ ] C. Comprehensive Testing: Run performance tests comparing DL inference time to traditional FEA time; test prediction accuracy across diverse geometries.
Final Performance Report and Accuracy Benchmarks.
TODO




- [ ] D. Documentation: Complete the final capstone report, presentation, and clean up the code/repository.
Final Capstone Submission.
TODO

⚙️ Task Tracking Board Template (Detailed Tasks)
This template is designed to be used with GitHub Issues or a dedicated GitHub Project Board. Use the checklist format to mark progress on individual tasks.
Example Tasks
Status
Task Description
Assignee
Priority
Related Phase
TODO
- [ ] Complete VTU file parsing script to extract nodal stress values.
[Your Name]
p1-high
phase-1-data
IN PROGRESS
- [ ] Design the data loading and augmentation pipeline for the U-Net input tensors.
[Your Name]
p1-high
phase-2-model
BLOCKED
- [ ] Set up the Fusion 360 Add-in manifest file. Blocked by: Need to finalize script naming conventions.
[Your Name]
p2-medium
phase-3-integration
DONE
- [x] Researched and selected PyTorch as the primary Deep Learning framework.
[Your Name]
p2-medium
phase-2-model
TODO
- [ ] Design the user interface (UI) elements for inputting load values in the Add-in.
[Your Name]
p1-high
phase-3-integration


