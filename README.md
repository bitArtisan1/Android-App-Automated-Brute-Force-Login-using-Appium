# Android-App-Automated-Brute-Force-Login-using-Appium

This repository contains an example implementation of mobile automation using Appium, focusing on interacting with Android applications. The project covers setting up Appium, writing automation scripts in Python, handling UI elements, and integrating with a continuous integration (CI) pipeline.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Setting Up Appium](#setting-up-appium)
- [Project Structure](#project-structure)
- [Usage](#usage)
  - [Running Tests](#running-tests)
  - [CI/CD Integration](#cicd-integration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Appium is an open-source automation framework for automating native, mobile web, and hybrid applications on iOS and Android platforms. Appium operates on a client-server architecture. The Appium server is responsible for receiving commands from the client (such as a test script written in Python or Java), executing those commands on the mobile device or emulator, and sending back the results.

The automation script demonstrates:
- Launching the Android application using Appium
- Identifying & interacting with UI elements such as EditText (username and password fields) and TextView (login button)
- Using dynamic data (date formatting) as input (password attempts)
- Integrating with a continuous integration (CI) pipeline for automated testing

# Appium Automation Setup

## Prerequisites

Before running the automation scripts, ensure you have the following installed and configured:

- Python (3.x recommended)
- Appium Server
- Android SDK tools
- Appium Python client (`appium-python-client`)
- Java Development Kit (JDK)
- UIAutomator2 Driver
- Developer options enabled on your Android device with USB debugging

### Installing Python

1. **Download Python:** Go to the [official Python website](https://www.python.org/downloads/) and download the latest version of Python.
2. **Install Python:** Run the installer and ensure that you select the option to add Python to your system PATH during installation.

### Installing Java Development Kit (JDK)

1. **Download JDK:** Go to the [Oracle JDK download page](https://www.oracle.com/java/technologies/javase-downloads.html) and download the latest JDK.
2. **Install JDK:** Run the installer and follow the prompts.
3. **Set JAVA_HOME Environment Variable:**
   - Open the Start Menu, search for "Environment Variables," and select "Edit the system environment variables."
   - In the System Properties window, click "Environment Variables."
   - Under "System variables," click "New" and set the `JAVA_HOME` variable to the path of your JDK installation (e.g., `C:\Program Files\Java\jdk-13`).
   - Find the `Path` variable in the list, select it, and click "Edit." Add a new entry with the path to the JDK's `bin` directory (e.g., `C:\Program Files\Java\jdk-13\bin`).

### Installing Android SDK Tools

1. **Download Android SDK Command-line Tools:** Go to the [Android developer site](https://developer.android.com/studio#command-tools) and download the SDK command-line tools.
2. **Extract and Install SDK Tools:**
   - Extract the downloaded tools to a directory of your choice.
   - Open a command prompt and navigate to the extracted directory.
   - Run the following commands to install the SDK and platform tools:

     ```bash
     sdkmanager --install "platform-tools" "platforms;android-30" "build-tools;30.0.3" tools
     ```

3. **Add SDK Tools to PATH:**
   - Open the Start Menu, search for "Environment Variables," and select "Edit the system environment variables."
   - In the System Properties window, click "Environment Variables."
   - Find the `Path` variable in the list, select it, and click "Edit." Add a new entry with the path to the `platform-tools` directory within the SDK installation (e.g., `C:\Users\YourUsername\Android\Sdk\platform-tools`).

### Installing Appium Server

1. **Install Node.js and npm:** Appium is built on Node.js, so you need to install Node.js first.
   - Download and install Node.js from the [official website](https://nodejs.org/).
2. **Install Appium:** Once Node.js and npm are installed, you can install Appium globally using npm.
   - Open a command prompt and run the following command:

     ```bash
     npm install -g appium
     ```

3. **Install Appium Doctor:** Appium Doctor helps verify that your system is properly configured.
   - Run the following command to install Appium Doctor:

     ```bash
     npm install -g appium-doctor
     ```

4. **Verify Appium Installation:**
   - Run the following command to check that Appium is installed correctly:

     ```bash
     appium-doctor
     ```

### Installing UIAutomator2 Driver

1. **Install UIAutomator2 Driver:**
   - Open a command prompt and run the following command:

     ```bash
     npm install -g appium-uiautomator2-driver
     ```

### Setting Up Developer Options on Android Device

1. **Enable Developer Options:**
   - Open the Settings app on your Android device.
   - Scroll down and select "About phone."
   - Find the "Build number" entry and tap it seven times. You should see a message indicating that Developer options are now enabled.
2. **Enable USB Debugging:**
   - Go back to the main Settings menu and select "System."
   - Select "Developer options."
   - Find and enable the "USB debugging" option.

3. **Connect Your Android Device:**
   - Connect your device to your computer using a USB cable.
   - You may need to allow USB debugging permissions on your device when prompted.

### Installing Android SDK Tools (Command Line) and UIAutomatorViewer

1. **Install SDK Tools:**
   - Open a command prompt and navigate to your SDK tools directory.
   - Run the following command to install additional tools:

     ```bash
     sdkmanager --install "tools"
     ```

2. **Launch UIAutomatorViewer:**
   - Navigate to the `tools/bin` directory within your Android SDK installation.
   - Run the following command to launch UIAutomatorViewer:

     ```bash
     uiautomatorviewer.bat
     ```

UIAutomatorViewer is a GUI tool to inspect the UI components of your Android application. It helps you understand the structure of the UI elements, which is essential for writing reliable Appium tests.

### Installing Appium Python Client

1. **Install Appium Python Client:**
   - Open a command prompt and run the following command:

     ```bash
     pip install Appium-Python-Client
     ```

---

Following these detailed steps will ensure that your environment is correctly set up for running Appium automation scripts. You are now ready to start writing and executing your Appium tests!

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/appium-mobile-automation.git
   cd appium-mobile-automation

