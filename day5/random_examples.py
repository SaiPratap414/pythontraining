#!/usr/bin/env python3
"""
Random Module Examples - Comprehensive Guide
This file demonstrates all major functions in Python's random module
"""

import random
import string

def basic_number_generation():
    """Basic random number generation functions"""
    print("=== BASIC NUMBER GENERATION ===")
    
    # Generate random float between 0.0 and 1.0
    print(f"random.random(): {random.random()}")
    
    # Generate random integer between a and b (inclusive)
    print(f"random.randint(1, 10): {random.randint(1, 10)}")
    
    # Generate random number from range (like range() function)
    print(f"random.randrange(0, 100, 5): {random.randrange(0, 100, 5)}")
    
    # Generate random float between a and b
    print(f"random.uniform(1.5, 9.5): {random.uniform(1.5, 9.5):.2f}")
    
    # Generate random bits
    print(f"random.getrandbits(8): {random.getrandbits(8)}")
    
    # Generate random bytes
    print(f"random.randbytes(4): {random.randbytes(4)}")
    print()

def sequence_operations():
    """Working with sequences (lists, tuples, strings)"""
    print("=== SEQUENCE OPERATIONS ===")
    
    fruits = ['apple', 'banana', 'orange', 'grape', 'kiwi']
    numbers = list(range(1, 11))
    
    # Choose one random element
    print(f"random.choice(fruits): {random.choice(fruits)}")
    
    # Choose multiple elements with replacement (can repeat)
    print(f"random.choices(fruits, k=3): {random.choices(fruits, k=3)}")
    
    # Choose multiple elements without replacement (unique)
    print(f"random.sample(fruits, 3): {random.sample(fruits, 3)}")
    
    # Shuffle list in place
    numbers_copy = numbers.copy()
    random.shuffle(numbers_copy)
    print(f"Original: {numbers}")
    print(f"Shuffled: {numbers_copy}")
    
    # Weighted choices
    weights = [1, 1, 1, 3, 1]  # grape is 3x more likely
    print(f"Weighted choice: {random.choices(fruits, weights=weights, k=5)}")
    print()

def statistical_distributions():
    """Statistical distribution functions"""
    print("=== STATISTICAL DISTRIBUTIONS ===")
    
    # Normal (Gaussian) distribution
    print(f"Normal distribution (μ=0, σ=1): {random.gauss(0, 1):.4f}")
    print(f"Normal distribution (μ=100, σ=15): {random.normalvariate(100, 15):.2f}")
    
    # Uniform distribution
    print(f"Uniform distribution (1-10): {random.uniform(1, 10):.2f}")
    
    # Triangular distribution
    print(f"Triangular (low=0, high=10, mode=2): {random.triangular(0, 10, 2):.2f}")
    
    # Exponential distribution
    print(f"Exponential (λ=1.5): {random.expovariate(1.5):.4f}")
    
    # Beta distribution
    print(f"Beta (α=2, β=5): {random.betavariate(2, 5):.4f}")
    
    # Gamma distribution
    print(f"Gamma (α=2, β=1): {random.gammavariate(2, 1):.4f}")
    print()

def practical_examples():
    """Practical real-world examples"""
    print("=== PRACTICAL EXAMPLES ===")
    
    # Simulate dice roll
    def roll_dice(sides=6, count=1):
        return [random.randint(1, sides) for _ in range(count)]
    
    print(f"Roll 2 six-sided dice: {roll_dice(6, 2)}")
    print(f"Roll 1 twenty-sided die: {roll_dice(20, 1)}")
    
    # Generate random password
    def generate_password(length=8):
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(random.choices(chars, k=length))
    
    print(f"Random password: {generate_password(12)}")
    
    # Simulate coin flips
    def flip_coins(count=10):
        return [random.choice(['Heads', 'Tails']) for _ in range(count)]
    
    print(f"10 coin flips: {flip_coins(10)}")
    
    # Random color generator
    def random_color():
        return f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"
    
    print(f"Random hex color: {random_color()}")
    
    # Pick random items from different categories
    adjectives = ['amazing', 'brilliant', 'creative', 'dynamic', 'elegant']
    nouns = ['programmer', 'artist', 'scientist', 'explorer', 'inventor']
    print(f"Random description: {random.choice(adjectives)} {random.choice(nouns)}")
    print()

def seed_and_state():
    """Working with seeds and state for reproducibility"""
    print("=== SEEDS AND STATE ===")
    
    # Set seed for reproducible results
    random.seed(42)
    print("After setting seed(42):")
    print(f"  First random(): {random.random()}")
    print(f"  Second random(): {random.random()}")
    
    # Reset to same seed
    random.seed(42)
    print("After resetting seed(42):")
    print(f"  First random(): {random.random()}")
    print(f"  Second random(): {random.random()}")
    
    # Save and restore state
    random.seed(123)
    state = random.getstate()
    print(f"Random number: {random.random()}")
    
    random.setstate(state)  # Restore saved state
    print(f"Same random number: {random.random()}")
    print()

def security_note():
    """Note about security and SystemRandom"""
    print("=== SECURITY NOTE ===")
    print("For cryptographic purposes, use random.SystemRandom():")
    
    secure_random = random.SystemRandom()
    print(f"Secure random int: {secure_random.randint(1, 1000)}")
    print(f"Secure random choice: {secure_random.choice(['A', 'B', 'C', 'D'])}")
    print("SystemRandom uses os.urandom() and is suitable for passwords, tokens, etc.")
    print()

if __name__ == "__main__":
    # Run all examples
    basic_number_generation()
    sequence_operations()
    statistical_distributions()
    practical_examples()
    seed_and_state()
    security_note()
    
    print("=== SUMMARY ===")
    print("The random module provides:")
    print("• Basic random number generation (int, float, bytes)")
    print("• Sequence operations (choice, sample, shuffle)")
    print("• Statistical distributions (normal, exponential, etc.)")
    print("• State management (seed, getstate, setstate)")
    print("• Secure random numbers (SystemRandom)")