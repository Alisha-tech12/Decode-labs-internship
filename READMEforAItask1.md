# Project 1: Rule-Based AI Chatbot

A simple rule-based chatbot that responds to predefined user inputs using if-else logic and runs in a continuous loop. This is the foundation project for the Artificial Intelligence training program at DecodeLabs.

## Overview

This chatbot demonstrates the fundamental concepts of control flow, decision-making logic, and deterministic AI systems. Unlike machine learning models that learn from data, this rule-based system uses explicit instructions to generate responses.

## Requirements Met

- Handle greetings and exit commands
- Use if-else logic for responses
- Run in a continuous loop
- 5+ conversation intents
- Fallback response for unrecognized input
- Input sanitization (lowercase conversion)

## Features

- Random response variations for natural conversation
- Keyword matching (not just exact matches)
- Multiple greeting patterns recognized
- Exit command with farewell message
- Help command listing available features

## Intents Supported

| Intent | Keywords |
|--------|----------|
| Greeting | hello, hi, hey, greetings |
| Status | how are you, how do you do, how's it going |
| AI Questions | ai, artificial intelligence, what is ai |
| Identity | your name |
| Help | help |
| Exit | bye |

## Installation

No external libraries required. Uses only Python standard library (random module).

## Usage

1. Save the code as `chatbot.py`

2. Run from terminal:
   ```bash
   python chatbot.py
