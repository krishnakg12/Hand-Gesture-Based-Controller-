# Hand-Gesture-Based-Controller-
# ✋ Advanced Hand Gesture-Based Virtual Game Controller  
> Real-Time Gesture Recognition Using OpenCV + MediaPipe + Pynput

A Python-based real-time gesture recognition system that allows you to **control in-game actions using hand gestures**. Uses **MediaPipe** for precise hand tracking and **Pynput** to simulate keyboard and mouse events — enabling movement, jumping, shooting, crouching, sprinting, and more with just your hand.

---

## 🎯 Project Objective

This project turns your hand into a virtual game controller by mapping gestures to key actions like `W`, `A`, `S`, `D`, `Jump`, `Shoot`, `Crouch`, and `Reload`. It is designed to bring **touchless interaction to gaming environments**, enhancing accessibility and immersion.

---

## 🚀 Key Features

- 👋 Real-time hand tracking via webcam
- 🖱️ Control mouse and keyboard using gestures
- 🕹️ Map intuitive actions to gestures:
  - Move Forward/Backward/Left/Right
  - Jump (Spacebar)
  - Crouch (Ctrl)
  - Shoot (Mouse Left Click)
  - Reload (R)
  - Sprint (Shift)

- 💡 Gesture logic based on landmark distances and angles
- ⚡ Fast and lightweight — minimal latency

---

## 🧠 Gesture Mappings

| Gesture | Action |
|--------|--------|
| Middle finger far above wrist | Move Forward (`W`) |
| Middle finger near wrist | Move Backward (`S`) |
| Hand moved left/right | Move Left/Right (`A` / `D`) |
| Index above middle | Jump (`Space`) |
| All fingers up, thumb across | Reload (`R`) |
| Index and thumb touch | Shoot (Mouse click) |
| Fingers down below wrist | Crouch (`Ctrl`) |
| Index bent, middle extended | Sprint (`Shift`) |


## 🧩 Tech Stack

- **Python 3.8+**
- **OpenCV** – Video and image frame processing
- **MediaPipe** – Hand landmark detection
- **Pynput** – Keyboard and mouse input simulation



