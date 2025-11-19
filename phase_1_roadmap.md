# 📘 Phase 1: Setup & Research Roadmap (Months 1–3)

**Goal:** Lay the technical and research foundation for the AI-powered CAD assembly and simulation system.  
**Timeframe:** 12 weeks (Weeks 1–12)  
**Effort:** ~9 hours/week (total ≈ 100 hours)

---

## 📅 Month 1 (Weeks 1–4): Research & Environment Setup

### ✅ Week 1–2: Literature & Toolchain Setup
- **[docs] Literature Review**
  - Study academic papers on:
    - CAD assembly automation (e.g. AutoMate, Fusion Gallery)
    - ML-based FEA surrogates
    - 3D CNNs and geometry-based AI
  - Summarize insights in `research_notes.md`
- **[setup] Install and Test Environment**
  - Install Fusion 360 and activate API access
  - Install Python 3.10+, PyTorch/TensorFlow, NumPy, Matplotlib
  - Clone starter scripts from Autodesk Fusion 360 API GitHub
- **[repo] Create GitHub Repository**
  - Initialize: `ai-cad-assembly-sim`
  - Add:
    - `README.md`
    - `.gitignore` (Python, CAD formats)
    - MIT or Apache-2.0 license
    - Devlog file: `log.md`

---

### ✅ Week 3–4: Data Strategy & Plugin Scaffolding
- **[data] Plan Data Schema**
  - Define structure for CAD part metadata:
    - Face normals, edge loops, bounding box, hole locations
  - Define schema for stress prediction data:
    - Input (voxelized geometry), Output (stress map or label)
- **[data] Source Data & Tools**
  - List open CAD repositories (Onshape, GrabCAD, Fusion Gallery)
  - Identify FEA tools: CalculiX, FEniCS, PyCalculix
  - List formats to support: `.STEP`, `.IGES`
- **[plugin] Scaffold Fusion 360 Plugin**
  - Create minimal plugin:
    - UI button in toolbar
    - Click handler that logs “Plugin Initialized”
  - Directory structure:
    ```
    fusion_plugin/
      ├─ scripts/
      ├─ resources/
      ├─ ai_module/
      └─ README.md
    ```

---

## 📅 Month 2 (Weeks 5–8): CAD Geometry I/O & Basic Feature Extraction

### ✅ Week 5–6: STEP/IGES File Processing
- **[plugin] Parse Geometry**
  - Write Python script to:
    - Load `.STEP` files
    - Extract faces, edges, and loops
    - Print face areas, edge lengths, centroid
  - Use Fusion 360 API (`BRepBody`, `BRepFace`, `BRepEdge`)
- **[plugin] Log Features to Console**
  - Debug output:
    ```
    Part: gear_20t.step  
    Faces: 17  
    Cylindrical holes: 2  
    Bounding box: 45x45x10 mm
    ```

### ✅ Week 7–8: Visual Debugging & Test Parts
- **[plugin] Add Face/Edge Visualization**
  - Mark circular holes with colors or callouts
  - Optional: Render face normals in 3D canvas (arrows)
- **[data] Collect Sample Assemblies**
  - Download or create 3–5 simple assemblies:
    - Bracket + Bolt
    - Shaft + Gear
    - Block + Housing
  - Manually document intended joint types (rigid/revolute)

---

## 📅 Month 3 (Weeks 9–12): Constraint Data Collection & Readiness for ML

### ✅ Week 9–10: Constraint Annotation Prep
- Prepare spreadsheet format for joint annotations:
  ```
  part1_id, part2_id, face1_id, face2_id, joint_type
  bracket, bolt, face#12, face#7, rigid
  ```
- Extract face IDs via Fusion API and export to CSV

### ✅ Week 11–12: Final Review & Checkpoint
- Review:
  - Code organization
  - Plugin UI and geometry pipeline
  - Face/edge detection reliability
- Push stable plugin + data tools to GitHub
- Snapshot project state:
  - Plugin = parses and logs geometry
  - 3 assemblies labeled for joint prediction
  - Data schemas and API scripts in place

---

## 🧾 Summary of Deliverables (End of Phase 1)

| Output | Description |
|--------|-------------|
| 🧠 `research_notes.md` | Summary of key methods & papers |
| 🗂 `fusion_plugin/` | Initialized Fusion 360 plugin scaffold |
| 📄 `step_parser.py` | STEP/IGES geometry feature extractor |
| 🧪 `assembly_samples/` | 3–5 part files + annotated joints |
| 📑 `data_schema.md` | Formats for geometry + stress ML input |
| 🔁 GitHub repo | Live with README, license, logs, and commits |

---

## 🟢 Ready for Phase 2:
- Implement **AI Assembly Generator** (joint prediction + assembly automation)
