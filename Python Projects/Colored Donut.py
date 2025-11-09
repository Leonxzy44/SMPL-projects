import sys
import time
import math

A = 0
B = 0

width = 120
height = 40

# Shading levels and corresponding ANSI foreground colors
shading_chars = ".,-~:;=!*#$@"
shading_colors = [
    "\033[90m",  # Dark gray
    "\033[91m",  # Red
    "\033[91m",  # Red
    "\033[93m",  # Yellow
    "\033[93m",  # Yellow
    "\033[92m",  # Green
    "\033[96m",  # Cyan
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[97m",  # White
    "\033[97;1m",  # Bright white
    "\033[97;1m",  # Bright white
]

RESET = "\033[0m"
BACKGROUND = "\033[40m"  # Black background

print("\x1b[2J", end="")  # Clear screen once

while True:
    z = [0] * (width * height)
    b = [' '] * (width * height)

    for j in range(0, 628, 2):
        for i in range(0, 628, 1):
            c = math.sin(i / 100)
            d = math.cos(j / 100)
            e = math.sin(A)
            f = math.sin(j / 100)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i / 100)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e

            x = int(width / 2 + width * 0.25 * D * (l * h * m - t * n))
            y = int(height / 2 + height * 0.5 * D * (l * h * n + t * m))
            o = x + width * y
            N = int(12 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if 0 <= o < width * height and D > z[o]:
                z[o] = D
                idx = max(0, min(N, len(shading_chars) - 1))
                b[o] = f"{shading_colors[idx]}{shading_chars[idx]}{RESET}"

    sys.stdout.write('\x1b[H')  # Move cursor to top-left
    for k in range(width * height):
        sys.stdout.write(BACKGROUND + b[k])
        if (k + 1) % width == 0:
            sys.stdout.write(RESET + '\n')
    sys.stdout.flush()

    A += 0.07
    B += 0.03
    time.sleep(0.01)

