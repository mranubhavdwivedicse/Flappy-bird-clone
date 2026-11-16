# Flappy Bird Clone (Problem Statement No. 61)

**Course:** Programming Fundamentals and Logic Building Using Python (`RU-100-01-0021`)  
**Institution:** Rungta International Skills University, School of Computer Science and Engineering  
**Degree:** Bachelor of Technology (Computer Science & Engineering)  
**Academic Session:** 2026–2027  
**Class:** B.Tech / CSE / First Semester / Section – K  
**Date of Allocation:** 14th October 2026  
**Date of Submission:** 16th November 2026  

---

## 1. Problem Statement

Create a Flappy Bird style game in which a bird constantly falls due to gravity and flies upward when the player presses SPACE. The player must pass through gaps between pipes to score, and the game ends if the bird hits a pipe, the ground or leaves the top of the screen.

- **Language:** Python 3
- **Concepts:** Pygame, Gravity, Collision Detection (`Rect.colliderect`), Game Loop
- **Specifications:**
  - Window Size: `400 x 600` (Width: 400 px, Height: 600 px)
  - Bird Dimensions: `30 x 30` px, fixed at horizontal position $x = 100$, starting position $y = 300$
  - Physics Update: Each frame, $\text{velocity} += 1$, then $y += \text{velocity}$
  - Flap Impulse: Pressing `SPACE` sets $\text{velocity} = -10$ before the frame update
  - Pipe Dimensions: Width $60\text{ px}$, vertical gap $150\text{ px}$, random gap position
  - Screen Limits: Ground is at $y = 600$, top edge is at $y = 0$

---

## 2. Bare Minimum Requirements Compliance

1. **Python 3 Single File Solution:** The entire game logic and test harness are implemented in a single executable file (`main.py`).
2. **Gravity & Flap Physics:** Gravity increments velocity by 1 each frame. Pressing `SPACE` resets velocity to -10 before the position update.
3. **Pipe Generation & Movement:** Pipes spawn from the right side of the screen with a randomized 150 px gap, move leftward at constant speed, and are deleted once they exit the screen ($x + \text{width} < 0$).
4. **Scoring Mechanism:** Adds 1 point each time the bird passes a pipe ($x_{\text{bird}} > x_{\text{pipe}} + \text{width}$), displaying the current score at the top of the screen.
5. **Collision Detection & Game Over:** Detects collisions with pipes, ground ($y + 30 \ge 600$), and the ceiling ($y < 0$) using `Rect.colliderect()`. Transitions to a Game Over screen and allows restarting via `SPACE` or `R`.

---

## 3. Mathematical and Logic Formulations

### 3.1 Gravity Integration
The simulation uses semi-implicit Euler integration:
$$\text{velocity}_{t+1} = \text{velocity}_t + 1$$
$$y_{t+1} = y_t + \text{velocity}_{t+1}$$

### 3.2 Flap Impulse
When `SPACE` is pressed:
$$\text{velocity}_{\text{initial}} = -10$$
$$\text{velocity}_{t+1} = -10 + 1 = -9$$
$$y_{t+1} = y_t + (-9) = y_t - 9$$

### 3.3 Boundary Conditions
- **Ground Impact:** The bird is 30 px tall. With origin $(0,0)$ at top-left, the bottom edge is $y + 30$. Collision occurs when:
  $$y + 30 \ge 600 \iff y \ge 570$$
- **Ceiling Departure:** If $y < 0$, the bird has left the screen at the top.
- **Pipe Collision:** Evaluated using Axis-Aligned Bounding Box (AABB) intersection:
  $$\text{colliderect}(R_{\text{bird}}, R_{\text{pipe}})$$
- **Pipe Passed:** The bird is at $x = 100$. A pipe of width 60 px has its trailing edge at $x_{\text{pipe}} + 60$. The score increments when:
  $$x_{\text{bird}} > x_{\text{pipe}} + 60 \iff 100 > x_{\text{pipe}} + 60 \iff x_{\text{pipe}} < 40$$

---

## 4. Test Cases Verification Table

| Test Case | Scenario / Input | Expected Output | Actual Output | Status |
| :--- | :--- | :--- | :--- | :---: |
| **Test Case 1** | **Normal Input:**<br>Bird $y = 300$, $\text{velocity} = 0$<br>No key pressed, 2 frames | Frame 1: $\text{velocity} = 1 \mid y = 301$<br>Frame 2: $\text{velocity} = 2 \mid y = 303$ | `Frame 1: velocity = 1 \| y = 301`<br>`Frame 2: velocity = 2 \| y = 303` | Pass |
| **Test Case 2 (a)** | **Boundary Min (Ground Touch):**<br>Bird $y = 570$ (bottom touches $y=600$) | Collision with ground \| Game Over | `Collision with ground \| Game Over` | Pass |
| **Test Case 2 (b)** | **Boundary Min (Top Edge Leave):**<br>Bird $y = 5$, $\text{velocity} = 0$, `SPACE` | $\text{velocity} = -9 \mid y = -4 \mid$<br>Bird left the screen at the top \| Game Over | `velocity = -9 \| y = -4 \| Bird left the screen at the top \| Game Over` | Pass |
| **Test Case 3** | **Invalid Input:**<br>Bird $y = 300$, $\text{velocity} = 0$<br>Key pressed: `Z` (not SPACE), 1 frame | Key ignored \| $\text{velocity} = 1 \mid y = 301$ | `Key ignored \| velocity = 1 \| y = 301` | Pass |
| **Test Case 4 (a)** | **Valid Flap Velocity:**<br>Bird $y = 300$, $\text{velocity} = 5$, `SPACE`, 1 frame | $\text{velocity} = -9 \mid y = 291$ (bird moves up) | `velocity = -9 \| y = 291 (bird moves up)` | Pass |
| **Test Case 4 (b)** | **Pipe Passage & Score:**<br>Pipe at $x = 39$ ($w=60$), bird $x = 100$, score = 0 | Pipe passed \| Score: 1 | `Pipe passed \| Score: 1` | Pass |

### Visual Verification
The screenshot below shows the automated test suite executing in the terminal with all 4 test cases passing:

![Automated Acceptance Test Suite Pass](screenshots/test_case_all_pass_vscode.png)

---

## 5. Controls

- **Flap / Jump:** `SPACE`
- **Start Game:** `SPACE`
- **Restart Game:** `SPACE` or `R` (when Game Over)
- **Quit Game:** `ESCAPE` or Close Window

---

## 6. How to Run

### Interactive Graphical Game (Pygame)
```bash
python main.py
```

### Run Test Suite in Terminal
```bash
python main.py --test
```
