#!/usr/bin/env python3
"""
Hello World Script for Data Analysis Environment
This script demonstrates that your Python environment is working correctly.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def main():
    print("🐍 Hello, World! Welcome to your Data Analysis Environment!")
    print("=" * 60)
    
    # Show Python version and current time
    import sys
    print(f"Python version: {sys.version}")
    print(f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Test pandas
    print("📊 Testing pandas...")
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'London', 'Tokyo', 'Paris']
    })
    print("Sample DataFrame:")
    print(df)
    print()
    
    # Test numpy
    print("🔢 Testing numpy...")
    array = np.array([1, 2, 3, 4, 5])
    print(f"NumPy array: {array}")
    print(f"Mean: {np.mean(array)}")
    print(f"Standard deviation: {np.std(array):.2f}")
    print()
    
    # Test matplotlib (create a simple plot)
    print("📈 Testing matplotlib...")
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, 'b-', linewidth=2, label='sin(x)')
    plt.title('Hello World - Sine Wave')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('hello_world_plot.png', dpi=150, bbox_inches='tight')
    print("✅ Plot saved as 'hello_world_plot.png'")
    plt.show()
    
    print("\n🎉 All packages are working correctly!")
    print("Your Python environment is ready for data analysis and visualization!")

if __name__ == "__main__":
    main() 