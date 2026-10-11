# TankWise AI — Heat and Water Safety Assistant

## 🌍 About the Project

TankWise AI is a Python-based application built for **WeMakeDevs AWS Environmental Hacks — Heat and Water track**. It helps users estimate household water tank availability and understand basic safety precautions during extreme heat.

## 🚨 Problem Statement

Water shortages and extreme heat can affect household safety and daily life. People need a simple way to estimate how long their available tank water may last and receive basic heat-safety guidance.

## 💡 Our Solution

TankWise AI provides a simple web application where users can enter water tank details, daily water usage, temperature, and humidity to get useful estimates and safety recommendations.

## ✨ Features

- 💧 Calculates estimated water remaining in a tank.
- 📊 Estimates how many days the available water may last.
- 🌡️ Provides basic heat-safety guidance using temperature and humidity inputs.
- 📁 Allows users to download recorded calculations as a CSV file.
- ☁️ Includes a Python serverless safety function tested locally using AWS SAM CLI and Docker.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- AWS SAM CLI
- AWS Lambda-compatible Python function
- Docker
- Git and GitHub

## ▶️ How to Run the Web Application

1. Install Python on your computer.
2. Open a terminal in the project folder.
3. Install the required packages:

   ```bash
   pip install streamlit pandas
   ```

4. Start the application:

   ```bash
   streamlit run app.py
   ```

5. Open the local URL shown in the terminal.

## ☁️ Test the Serverless Function Locally

Make sure Docker and AWS SAM CLI are installed.

Open a terminal in the project folder and run:

```bash
cd tankwise-safety-function
sam build
sam local invoke HelloWorldFunction --event event.json
```

The function processes water and heat-related input values and returns safety recommendations. It has been tested locally; **it has not been deployed to AWS Cloud**.

## ⚠️ Limitations

- Results depend on the values entered by the user.
- Heat recommendations are general guidance, not official weather alerts or medical advice.
- Water estimates depend on the user's tank capacity and daily usage.
- The serverless function has been tested locally and is not yet connected to the Streamlit interface.

## 🤖 AI Assistance

AI tools, including ChatGPT, were used to support project planning, code development, debugging, and documentation. The project was tested locally.

## 🎯 Hackathon Track

**WeMakeDevs AWS Environmental Hacks — Heat and Water**

TankWise AI aims to promote awareness of household water availability and basic heat safety through a beginner-friendly Python application.
