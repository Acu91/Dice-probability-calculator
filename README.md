# Dice Probability Simulator

This project simulates rolling dice to calculate the probability of obtaining specific outcomes over a number of experiments.

## Files

### `main.py`
This is the main script that takes user input and calculates the probability of rolling specific outcomes using the functions defined in `probability.py`.

### `probability.py`
This file contains helper functions to perform dice rolls, simulate experiments, and calculate probabilities.

---

## Features

- **Input Number of Dice:** Specify how many dice to roll.
- **Input Desired Outcomes:** Enter the expected outcomes for the dice rolls.
- **Run Simulations:** Specify the number of experiments to calculate the probability of achieving the desired outcomes.
- **Result Display:** Outputs the probability of obtaining the desired outcome and the first occurrence (if any).

---

## How It Works

1. The user inputs the number of dice (`n`) to roll and the desired outcomes as a list.
2. The user specifies the number of experiments (`x`) to simulate.
3. The program:
   - Rolls `n` dice for `x` experiments.
   - Checks if the rolled dice match the desired outcomes.
   - Calculates and displays the probability of obtaining the outcomes.
4. If the desired outcomes are rolled, the program also indicates the first experiment in which it occurred.

---

## Prerequisites

- Python 3.6 or higher

---

## Usage

1. Clone or download the repository.
2. Run the program:
   ```bash
   python main.py
