# Contributing to Gemini PDF Chatbot

First off, thank you for considering contributing to Gemini PDF Chatbot! It's people like you that make this project better for everyone.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)
- [Community](#community)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## Getting Started

- Make sure you have a [GitHub account](https://github.com/signup)
- Submit an issue for your proposed change if one doesn't already exist
- Fork the repository on GitHub

## How Can I Contribute?

### Reporting Bugs

This section guides you through submitting a bug report. Following these guidelines helps maintainers understand your report and reproduce the behavior.

**Before Submitting A Bug Report**

- Check the existing issues to avoid duplicates
- Determine which part of the application the problem relates to

**How Do I Submit A (Good) Bug Report?**

Bugs are tracked as [GitHub issues](https://github.com/kaifcoder/gemini_multipdf_chat/issues). Create an issue and provide the following information:

- Use a clear and descriptive title
- Describe the exact steps to reproduce the problem
- Provide specific examples and screenshots if applicable
- Describe the behavior you observed and what behavior you expected
- Include your environment details (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are also tracked as GitHub issues. When creating an enhancement suggestion, please provide:

- A clear and descriptive title
- A detailed description of the proposed enhancement
- Explain why this enhancement would be useful
- Include mockups or examples if applicable

### Your First Code Contribution

Unsure where to begin contributing? You can start by looking through these beginner-friendly issues:

- Issues labeled `good first issue` - these should only require a few lines of code
- Issues labeled `help wanted` - these are more involved but still accessible

### Pull Requests

- Fill in the required template
- Do not include issue numbers in the PR title
- Include screenshots and animated GIFs in your pull request whenever possible
- Follow the Python style guidelines
- Include tests if applicable
- Document new code

## Development Setup

1. **Fork and Clone the Repository**
   ```bash
   git clone https://github.com/your-username/gemini_multipdf_chat.git
   cd gemini_multipdf_chat
   ```

2. **Set up Python Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up Environment Variables**
   ```bash
   cp .env.example .env
   # Add your GOOGLE_API_KEY to the .env file
   ```

4. **Run the Application**
   ```bash
   streamlit run app.py
   ```

5. **Using Docker (Alternative)**
   ```bash
   docker compose up --build
   ```

## Pull Request Process

1. Ensure any install or build dependencies are documented
2. Update the README.md if needed with details of changes to the interface
3. Test your changes thoroughly
4. Make sure your code follows the existing style and conventions
5. Write clear commit messages
6. Submit your pull request with a clear description of what you've changed and why

## Style Guidelines

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

### Python Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Keep lines under 80-100 characters when possible
- Use type hints where appropriate

### Documentation Style Guide

- Use [Markdown](https://guides.github.com/features/mastering-markdown/)
- Reference functions and classes using backticks
- Include code examples where helpful

## Community

- Join our discussions in the [Issues](https://github.com/kaifcoder/gemini_multipdf_chat/issues) section
- Follow the project on GitHub for updates
- Star the repository if you find it useful!

## Questions?

If you have questions about contributing, feel free to:
- Open an issue with the `question` label
- Reach out to the maintainers directly

Thank you for your interest in contributing to Gemini PDF Chatbot! 🚀