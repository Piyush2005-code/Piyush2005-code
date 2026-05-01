<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=180&section=header&text=Piyush%20Singh%20Bhati&fontSize=42&fontColor=fff&animation=twinkling&fontAlignY=32&desc=AI%20Systems%20Engineer%20%C2%B7%20IIT%20Jodhpur&descAlignY=51&descAlign=50" />

<p>
  <a href="https://www.linkedin.com/in/piyush-singh-bhati-5a074929a">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <a href="https://github.com/Piyush2005-code">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
  </a>
  <a href="mailto:piyush.bhati680@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>
  <a href="http://piyush2005-code.github.io">
    <img src="https://img.shields.io/badge/Portfolio-00d4ff?style=for-the-badge&logo=vercel&logoColor=black" />
  </a>
</p>

<img src="https://komarev.com/ghpvc/?username=Piyush2005-code&style=for-the-badge&color=0d1c34&label=PROFILE+VIEWS" />

</div>

---

## 🧠 About Me

```python
class PiyushSinghBhati:
    affiliation  = "B.Tech CSE @ IIT Jodhpur  |  CGPA: 8.75 / 10.0"
    research     = ["AI Systems & GPU Architecture", "Physics-Informed Neural Networks (PINNs)"]
    interests    = ["ML Inference Infrastructure", "OS Design", "Embedded Systems",
                    "Computer Vision", "Autonomous Systems", "Robotics"]
    languages    = ["C", "C++", "Python", "ARM64 Assembly", "TypeScript"]
    currently    = "Deepening expertise in low-level systems & hardware-aware AI"
```

I am an undergraduate **Computer Science** student at **IIT Jodhpur** passionate about the intersection of **AI, systems engineering, and intelligent physical systems**.

My research explores **GPU architecture optimizations** (NVIDIA Hopper, kernel fusion, micro-benchmarking) and **Physics-Informed Neural Networks (PINNs)** for surrogate CFD modeling — bridging software and hardware through co-design. My project work spans a bare-metal ARM64 unikernel, real-time crop stress detection with YOLOv8, and detailed CAD modeling for STOL aircraft and precision agriculture drones.

---

## 🔬 Research Experience

<table>
<tr>
<td width="50%">

### 🖥️ AI Systems & GPU Architecture
**Prof. Sidharth Sharma · IIT Jodhpur** · *2026 – Ongoing*

- Investigating system-level optimizations for ML workloads on **NVIDIA Hopper** (Tensor Cores, DPX, async execution)
- Analyzing bottlenecks in large-model inference & training via **kernel fusion** and memory layout optimization
- Developing micro-benchmarks to characterize Hopper GPU performance, advancing hardware–software co-design

</td>
<td width="50%">

### 🌊 Physics-Informed Neural Networks (PINNs)
**Prof. Harshal D. Akolekar · IIT Jodhpur** · *2026 – Ongoing*

- Developing PINN-based **surrogate models** to accelerate CFD simulations
- Implementing neural networks in PyTorch to solve PDEs governing fluid flow
- Evaluating model accuracy & inference speed against traditional CFD solvers

</td>
</tr>
</table>

---

## 🚀 Featured Projects

<!-- ═══════════════════════════════════════════════════════════════════ -->
### 🔩 ARM64 Unikernel for ML Inference
> *C · ARM64 Assembly · QEMU · Unikraft* &nbsp;|&nbsp; **2025 – Ongoing**

<img src="https://raw.githubusercontent.com/Piyush2005-code/Piyush2005-code.github.io/dep/src/Embedded_Hardware.avif" width="100%" alt="ARM64 Embedded Hardware" />

- Implemented **ARMv8-A boot sequence**, MMU initialization, identity-mapped page tables & early UART driver on QEMU
- Built OS-agnostic UART communication protocol with **CRC validation** and bounded parsing
- Developed a **cooperative scheduler prototype**; context-switch overhead < 0.1% runtime cost
- Benchmarked **Unikraft vs. Linux VMs** across inference workloads — P50/P99 latency & scheduling variance

[![Repo](https://img.shields.io/badge/Source-MiniOS-181717?style=flat-square&logo=github)](https://github.com/Piyush2005-code/MiniOS)

---

<!-- ═══════════════════════════════════════════════════════════════════ -->
### 🌾 Crop Stress Detection — U-Net Semantic Segmentation
> *PyTorch · U-Net · OpenCV · YOLOv8n · CUDA/MPS* &nbsp;|&nbsp; **2025**

<table>
  <tr>
    <td><img src="https://raw.githubusercontent.com/Piyush2005-code/Piyush2005-code.github.io/dep/src/Farm_top_image.jpg" width="100%" alt="Aerial Farm View" /></td>
    <td><img src="https://raw.githubusercontent.com/Piyush2005-code/Piyush2005-code.github.io/dep/src/Crop_Detection_Segmentation_mask.jpg" width="100%" alt="U-Net Segmentation Mask" /></td>
  </tr>
  <tr>
    <td><img src="https://raw.githubusercontent.com/Piyush2005-code/Piyush2005-code.github.io/dep/src/Crop_Detection_YOLO_Object_Detection.png" width="100%" alt="YOLOv8 Detection" /></td>
    <td><img src="https://raw.githubusercontent.com/Piyush2005-code/Piyush2005-code.github.io/dep/src/UNet%20model.png" width="100%" alt="U-Net Architecture" /></td>
  </tr>
</table>

- Designed a **U-Net segmentation model** (~7.7M params) with skip connections for pixel-level stress detection
- Built a **synthetic dataset generation pipeline** using Gaussian blending + rotational augmentation (4× expansion)
- Full pipeline: AdamW optimizer · BCEWithLogitsLoss · Dice coefficient · 80/10/10 train–val–test split
- Real-time **video inference** with OpenCV batch processing → overlay MP4 output

[![Repo](https://img.shields.io/badge/Source-Crop_Vision-181717?style=flat-square&logo=github)](https://github.com/Piyush2005-code/Computer-Vision-for-stressed-crop-detection.git)

---

<!-- ═══════════════════════════════════════════════════════════════════ -->
### 🤖 JARVIS Voice Assistant
> *vLLM · RAG · Docker · Kubernetes · NVIDIA AudioFlamingo3* &nbsp;|&nbsp; **2025**

<img src="https://raw.githubusercontent.com/Piyush2005-code/Piyush2005-code.github.io/dep/src/jarvis-interface.png" width="100%" alt="JARVIS Interface" />

- Engineered **STT → LLM → TTS loop** with model quantization + vLLM inference on NVIDIA A5000
- Deployed containerized stack supporting **500+ concurrent users** with 98% uptime
- Integrated **RAG** for context-aware knowledge-grounded responses
- FastAPI backend with **real-time WebSocket** streaming for client UI

[![Repo](https://img.shields.io/badge/Source-Jarvis2.O-181717?style=flat-square&logo=github)](https://github.com/AISocietyIITJ/Jarvis2.O.git)

---

<!-- ═══════════════════════════════════════════════════════════════════ -->
### ⚙️ OS Scheduling Algorithm Simulator
> *React · TypeScript · Electron* &nbsp;|&nbsp; **2025**

<img src="https://raw.githubusercontent.com/Piyush2005-code/Piyush2005-code.github.io/dep/src/os-scheduler.png" width="100%" alt="OS Scheduler Gantt Chart" />

- Implemented **FCFS, Round Robin & Priority** scheduling with configurable parameters
- Real-time **Gantt chart visualization** for scheduling analysis
- Cross-platform Electron desktop app for algorithm performance comparison

[![Repo](https://img.shields.io/badge/Source-OS_Scheduler-181717?style=flat-square&logo=github)](https://github.com/Piyush2005-code/Operating-System-Scheduling-Algorithms.git)

---

<!-- ═══════════════════════════════════════════════════════════════════ -->
### ✈️ Fixed-Wing STOL Aircraft Wing Design
> *ANSYS Fluent · CAD · CFD* &nbsp;|&nbsp; **Inter IIT Tech Meet 14.0**

<table>
  <tr>
    <td><img src="https://raw.githubusercontent.com/Piyush2005-code/Piyush2005-code.github.io/dep/src/Wing_Side_view.jpeg" width="100%" alt="Wing Side View CAD" /></td>
    <td><img src="https://raw.githubusercontent.com/Piyush2005-code/Piyush2005-code.github.io/dep/src/wing-drawing.png" width="100%" alt="Wing Technical Drawing" /></td>
  </tr>
  <tr>
    <td><img src="https://raw.githubusercontent.com/Piyush2005-code/Piyush2005-code.github.io/dep/src/pressure-contours.png" width="100%" alt="Pressure Contours" /></td>
    <td><img src="https://raw.githubusercontent.com/Piyush2005-code/Piyush2005-code.github.io/dep/src/cfd-simulation.png" width="100%" alt="CFD Simulation" /></td>
  </tr>
</table>

- Surveyed high-lift wing configurations targeting **CL > 5**, benchmarking against state-of-the-art designs
- Achieved maximum **lift coefficient of 8.1258** under realistic thrust-device interaction conditions
- Complete **end-to-end CAD model** of the full wing assembly
- Validated via iterative **CFD simulations** in ANSYS Fluent

---

<!-- ═══════════════════════════════════════════════════════════════════ -->
### 🚁 Quadcopter CAD Design — Scout Drone for Precision Agriculture
> *Fusion 360 · UAV Design* &nbsp;|&nbsp; **2025**

<table>
  <tr>
    <td><img src="https://raw.githubusercontent.com/Piyush2005-code/Piyush2005-code.github.io/dep/src/quadcopter-isometric.png" width="100%" alt="Quadcopter Isometric" /></td>
    <td><img src="https://raw.githubusercontent.com/Piyush2005-code/Piyush2005-code.github.io/dep/src/quadcopter-front.png" width="100%" alt="Quadcopter Front View" /></td>
  </tr>
</table>

- Custom quadcopter frame accommodating compute, flight controller, GPS, comms modules & dual-camera config
- Hexacopter spray drone with modular tank integration and balanced payload placement

---

## 🛠️ Tech Stack

<div align="center">

**Languages**

![C](https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![ARM64](https://img.shields.io/badge/ARM64_Assembly-0091BD?style=for-the-badge&logo=arm&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)

**AI / ML**

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![CUDA](https://img.shields.io/badge/CUDA-76B900?style=for-the-badge&logo=nvidia&logoColor=white)
![vLLM](https://img.shields.io/badge/vLLM-181717?style=for-the-badge&logo=github&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)

**Systems & Infrastructure**

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![QEMU](https://img.shields.io/badge/QEMU-FF6600?style=for-the-badge&logo=qemu&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

**Design & Simulation**

![Fusion360](https://img.shields.io/badge/Fusion_360-FF6D00?style=for-the-badge&logo=autodesk&logoColor=white)
![ANSYS](https://img.shields.io/badge/ANSYS_Fluent-FFB71B?style=for-the-badge&logo=ansys&logoColor=black)

</div>

---

## 📊 GitHub Stats

<div align="center">
  <img height="160" src="https://github-readme-stats.vercel.app/api?username=Piyush2005-code&show_icons=true&theme=tokyonight&hide_border=true&bg_color=04080f&title_color=00d4ff&icon_color=00d4ff&text_color=b8d0e8&rank_icon=github" />
  <img height="160" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Piyush2005-code&layout=compact&theme=tokyonight&hide_border=true&bg_color=04080f&title_color=00d4ff&text_color=b8d0e8&langs_count=8" />
</div>

<div align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=Piyush2005-code&theme=tokyonight&hide_border=true&background=04080f&ring=00d4ff&fire=1a7fe8&currStreakLabel=00d4ff" />
</div>

---

## 🎓 Education

| Year | Degree | Institute | Score |
|------|--------|-----------|-------|
| 2024 – 2028 | B.Tech — Computer Science & Engineering | **Indian Institute of Technology, Jodhpur** | **CGPA: 8.75 / 10.0** |
| 2022 – 2024 | Senior Secondary (Class XII) | Central Academy, Ajmer | **87.4%** |

**Relevant Coursework** — Data Structures & Algorithms · Linear Algebra & O.D.E *(A-)* · Probability & Stochastic Processes *(A-)* · Introduction to Computer Science *(A)* · Introduction to Electrical Engineering *(A)*

---

## 🏆 Leadership & Activities

- **Project Mentor** — RAID AI Society, IIT Jodhpur *(2026)*  
  Mentoring first-year students building an Agentic-AI system to automate college counselling.

- **Assistant Head — Tech Exhibition, Prometeo'26** *(2025)*  
  Coordinating technical exhibits and managing logistics for IIT Jodhpur's annual technical festival.

- **Point of Contact — International Relations Conclave, IIT Jodhpur** *(2025)*  
  Managing accommodations and hospitality for delegates from all IITs during IRC 2025.

---

## 💡 Interests

`Artificial Intelligence` &nbsp;·&nbsp; `Computer Vision` &nbsp;·&nbsp; `Applied ML/DL` &nbsp;·&nbsp; `Operating Systems` &nbsp;·&nbsp; `UAVs` &nbsp;·&nbsp; `Robotics`

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer&animation=twinkling" />

*📍 IIT Jodhpur, Rajasthan, India &nbsp;·&nbsp; Last updated: May 2025*

</div>
