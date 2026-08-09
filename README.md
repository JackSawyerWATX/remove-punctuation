# Punctuation Remover (Python)

## Introduction

This simple Python program demonstrates how to remove punctuation from a string by iterating through each character and filtering out unwanted symbols. It’s a great beginner-friendly example for learning loops, conditionals, and string manipulation in Python.

---

## Table of Contents

* [About](#about)
* [Features](#features)
* [Tech Stack](#tech-stack)
* [Architecture](#architecture)
* [Project Structure](#project-structure)
* [Getting Started](#getting-started)
* [Configuration](#configuration)
* [Security](#security)
* [How to Contribute](#how-to-contribute)
* [What's Next?](#whats-next)
* [License](#license)
* [Acknowledgements](#acknowledgements)
* [Author](#author)

---

## About

This project removes punctuation characters from a predefined string. It loops through each character and builds a new string containing only non-punctuation characters.

---

## Features

* Removes common punctuation symbols from text
* Demonstrates character-by-character iteration
* Simple and easy-to-understand logic
* Beginner-friendly Python example
* Prints intermediate results during processing

---

## Tech Stack

* **Language:** Python 3
* **Concepts Used:**

  * Strings
  * Loops (`for`)
  * Conditional statements (`if`)

---

## Architecture

The program follows a straightforward procedural flow:

1. Define a string of punctuation characters
2. Define the input string
3. Loop through each character in the string
4. Check if the character is NOT punctuation
5. Append valid characters to a new string
6. Print the result progressively

---

## Project Structure

```
punctuation-remover/
│── main.py
│── README.md
```

### Example Code (`main.py`)

```python
punctuations = '"!@#$%^&*()_+=-:{}|[];<>?,./"'
my_string = "Hello!!, he said -- and went."
no_punctuation = ""

for char in my_string:
    if char not in punctuations:
        no_punctuation = no_punctuation + char
        print(no_punctuation)
```

---

## Getting Started

### Prerequisites

* Python 3 installed

### Run the Program

```bash
python main.py
```

---

## Configuration

You can modify:

* `my_string` → to process different text
* `punctuations` → to customize which characters are removed

---

## Security

* This is a local script with no external inputs or dependencies
* No known security risks
* Safe for educational and demonstration purposes

---

## How to Contribute?

1. Fork the repository
2. Create a new branch (`feature/your-feature`)
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## What's Next?

* Convert this into a reusable function
* Accept user input dynamically
* Use Python’s `string.punctuation` instead of a custom list
* Improve performance using list comprehensions
* Add unit tests

---

## License

This project is open-source and available under the MIT License.

---

## Acknowledgements

* Python documentation
* Beginner programming tutorials and exercises

---

## Author

**Jonathan Fausset**

* GitHub: https://github.com/jacksawyerwatx
* Portfolio: https://jonathanfausset.com
