import numpy as np
import matplotlib.pyplot as plt

# 1. Generate Simulated Noisy Sensor Signal
def generate_signal():
    np.random.seed(42)
    time = np.linspace(0, 10, 500)
    # Pure sine wave representing a clean sensor reading (e.g., vibration or AC voltage)
    clean_signal = np.sin(2 * np.pi * 0.5 * time) 
    # Adding random Gaussian noise to simulate real-world environment
    noise = np.random.normal(0, 0.4, size=len(time))
    noisy_signal = clean_signal + noise
    return time, clean_signal, noisy_signal

# 2. Apply Moving Average Filter for Noise Reduction
def moving_average_filter(signal, window_size=15):
    window = np.ones(window_size) / window_size
    # Convolve the signal to smooth out high-frequency noise
    filtered_signal = np.convolve(signal, window, mode='same')
    return filtered_signal

# 3. Analyze Data and Extract Features
def analyze_data(time, clean, noisy, filtered):
    # Calculate basic statistical metrics
    mae_noisy = np.mean(np.abs(clean - noisy))
    mae_filtered = np.mean(np.abs(clean - filtered))
    
    print("--- Signal Analysis Report ---")
    print(f"Mean Absolute Error (Before Filter): {mae_noisy:.4f}")
    print(f"Mean Absolute Error (After Filter):  {mae_filtered:.4f}")
    print(f"Noise Reduction Efficiency: {((mae_noisy - mae_filtered) / mae_noisy) * 100:.2f}%")

# 4. Main Execution
if __name__ == "__main__":
    time, clean_signal, noisy_signal = generate_signal()
    filtered_signal = moving_average_filter(noisy_signal)
    
    # Run analytics
    analyze_data(time, clean_signal, noisy_signal, filtered_signal)
    
