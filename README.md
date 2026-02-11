# Multi-Agent Stock Trading Decision System

An AI-powered multi-agent trading system built using CrewAI and Python that analyzes live stock market data and generates strategic Buy/Sell/Hold recommendations.

## Overview

This project implements a multi-agent architecture where autonomous AI agents collaborate to retrieve, analyze, and interpret live stock market data. The system fetches real-time financial metrics using the yFinance API and applies LLM-based reasoning to generate structured trading decisions.

## Features

- Multi-agent system built using CrewAI
- Live stock data retrieval using yFinance API
- Real-time analysis of:
  - Current market price
  - Daily price change
  - Percentage change
- Automated Buy/Sell/Hold recommendation generation
- Modular and extensible architecture

## Tech Stack

- Python
- CrewAI
- yFinance API
- Large Language Models (LLMs)

## System Architecture

1. Data Retrieval Agent  
   - Fetches real-time stock information using yFinance.

2. Analysis Agent  
   - Evaluates stock performance indicators such as price trends and daily momentum.

3. Decision Agent  
   - Generates structured Buy/Sell/Hold recommendation based on analyzed data.

## Example Output

Stock: TSLA  
Price: 245.30 USD  
Change: +3.12 (1.29%)  
Recommendation: HOLD  

## Installation

1. Clone the repository:

   git clone https://github.com/your-username/multi-agent-stock-trading-system.git

2. Navigate to the project directory:

   cd multi-agent-stock-trading-system

3. Create a virtual environment:

   python -m venv venv

4. Activate the environment:

   Windows:
   venv\Scripts\activate

   Mac/Linux:
   source venv/bin/activate

5. Install dependencies:

   pip install -r requirements.txt

## Usage

Run the main script:

   python main.py

Modify the stock ticker symbol inside the script to analyze different stocks.

## Future Enhancements

- Integration of technical indicators (RSI, MACD, Moving Averages)
- Backtesting trading strategies
- Portfolio-level analysis
- Streamlit-based web dashboard
- API deployment for real-time access

## Disclaimer

This project is for educational and research purposes only. It does not provide financial advice.
