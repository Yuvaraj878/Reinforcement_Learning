p = {
    0: {  # Red Light (Stopped)
        1: [(0.6, 1, 0.0, False), (0.4, 0, 0.0, False)],  # Proceed → Yellow Light
        0: [(0.6, 0, 0.0, False), (0.4, 1, 0.0, False)]   # Stay → Remain at Red
    },
    1: {  # Yellow Light (Ready)
        1: [(0.6, 2, 0.0, False), (0.4, 0, 0.0, False)],  # Proceed → Green Light
        0: [(0.6, 0, 0.0, False), (0.4, 2, 0.0, False)]   # Stay → Might go back or proceed
    },
    2: {  # Green Light (Walking)
        2: [(0.6, 1, 0.0, False), (0.4, 2, 0.0, False)],  # Left → Go back to Yellow Light
        1: [(0.6, 4, 1, True), (0.4, 2, 0.0, False)],  # Right → Reach Flashing Green (Success)
        0: [(0.6, 3, 0.0, True), (0.4, 2, 0.0, False)]  # Up → Blinking Red (Failure)
    },
    3: {  # Blinking Red Light (Collapsed)
        1: [(0.6, 2, 0.0, False), (0.4, 3, 0.0, False)],  # Try to recover → Green
        0: [(0.6, 3, 0.0, True), (0.4, 2, 0.0, False)]   # Stay stuck
    },
    4: {  # Flashing Green Light (Running - Goal)
        1: [(0.6, 4, 1, True), (0.4, 2, 0.0, False)],  # Stay at Flashing Green (Success)
        0: [(0.6, 2, 0.0, False), (0.4, 4, 1, True)]   # Move back to Green Light
    }
}
print("Yuvaraj S\n212222240119")
print(p)

