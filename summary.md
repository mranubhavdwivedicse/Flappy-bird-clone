# Project Submission Summary: Flappy Bird Clone (Problem Statement No. 61)

**Course:** Programming Fundamentals and Logic Building Using Python (`RU-100-01-0021`)  
**Institution:** Rungta International Skills University, School of Computer Science & Engineering  
**Degree:** Bachelor of Technology (Computer Science & Engineering)  
**Academic Session:** 2026–2027  
**Class:** B.Tech / CSE / First Semester / Section – K  
**Student Name:** Anubhav Dwivedi  
**Problem Statement No.:** 61  
**Project Title:** Flappy Bird Clone  

---

## 1. Project Summary

This project implements a 2D arcade Flappy Bird game in Python using Pygame, designed and developed as part of the B.Tech First Semester curriculum.

The game implements all functional requirements outlined in Problem Statement No. 61:
1. **Discrete Gravity & Flap Mechanics:** The bird experiences downward gravity of $+1$ pixel/frame each frame. Pressing the SPACE key provides an upward flap impulse of $-10$ pixels/frame.
2. **Obstacle Pipes:** Pairs of upper and lower vertical pipes (width 60 px, vertical gap 150 px) move from right to left at 3 pixels/frame.
3. **Collision Detection:** Bounding box collisions check whether the bird touches the upper pipe, lower pipe, ground ($y \ge 560$ px), or ceiling ($y < 0$ px). Any collision triggers the Game Over state.
4. **Scoring System:** Exactly $+1$ point is awarded when the bird successfully clears a pipe pair ($x_{\text{bird}} > x_{\text{pipe}} + \text{width}$).
5. **Acceptance Testing:** All 4 required test cases have been implemented and verified to pass with 100% accuracy.

---

## 2. In-Game Visual Documentation

| Start Screen | Active Flight | Game Over Screen |
| :---: | :---: | :---: |
| ![Start Screen](screenshots/flappy_bird_title.png) | ![Active Gameplay](screenshots/flappy_bird_gameplay.png) | ![Game Over](screenshots/flappy_bird_game_over.png) |

---

## 3. Test Cases Verification & Results

The test suite validates all four mandatory problem statement test cases. Running `python main.py --test` gives the following output:

```text
=================================================================
FLAPPY BIRD CLONE - PROBLEM STATEMENT NO. 61 TEST SUITE
=================================================================
[Test 1: Normal Input]
  Frame 1: velocity = 1 | y = 301
  Frame 2: velocity = 2 | y = 303
  Result : PASS

[Test 2: Boundary Collision]
  (a) y = 570 + 30 >= 600 -> Collision with ground: True
  (b) y = 5, SPACE -> v = -9, y = -4 (Top leave): True
  Result : PASS

[Test 3: Invalid Input]
  Key 'Z' ignored -> velocity = 1 | y = 301
  Result : PASS

[Test 4: Flap & Scoring]
  (a) y=300, v=5, SPACE -> v = -9 | y = 291 (bird moves up)
  (b) Pipe x=39, bird x=100 -> Pipe passed | Score: 1
  Result : PASS

=================================================================
SUMMARY: 4/4 TEST CASES PASSED (100% SUCCESS)
=================================================================
```

### In-Engine Test Case Frame Verification

| Test Case 1: Gravity | Test Case 2: Boundary Collision |
| :---: | :---: |
| ![Test Case 1](screenshots/test_case_1_normal.png) | ![Test Case 2](screenshots/test_case_2_boundary.png) |

| Test Case 3: Invalid Input | Test Case 4: Pipe Scoring |
| :---: | :---: |
| ![Test Case 3](screenshots/test_case_3_invalid.png) | ![Test Case 4](screenshots/test_case_4_valid.png) |

---

## 4. Key Classes & Code Architecture

The source code in `main.py` is organized into clean, modular classes:

1. **`Bird` Class:**
   - Tracks horizontal and vertical position ($x=100, y=300$) and velocity.
   - `flap()`: Applies the upward force (`velocity = -10`).
   - `update()`: Applies downward acceleration (`velocity += 1, y += velocity`).
   - `draw()`: Renders the retro bird sprite with body, wings, eyes, and beak.

2. **`Pipe` Class:**
   - Generates matching top and bottom pipes with a 150 px gap.
   - `update()`: Moves pipes to the left by 3 pixels per frame.
   - `is_colliding(bird_rect)`: Uses `pygame.Rect.colliderect` for bounding box collision checks.

3. **`main()` Function:**
   - Manages game states (`READY`, `PLAYING`, `GAME_OVER`).
   - Dispatches user input (SPACE, UP, R, T, ESC).
   - Manages scoring and screen refresh at 60 FPS.

---

## 5. Conclusion

The Flappy Bird clone satisfies 100% of the requirements set out in Problem Statement No. 61. The code is clean, fully readable, verified by automated test cases, and runs directly with standard Python and Pygame.
