# Vehicle Maintenance Scheduler

## Overview
This project is a backend microservice designed to schedule vehicle maintenance tasks across multiple depots efficiently. The system assigns vehicles to depots based on available mechanic hours while attempting to maximize the overall priority of completed tasks.

## Features
- Uses a greedy scheduling algorithm based on priority to duration ratio
- Ensures that each vehicle is assigned at most once
- Respects the capacity constraints of each depot
- Includes a logging mechanism for tracking system behavior
- Handles API failures with fallback mechanisms
- Follows a modular backend structure

## Approach

### Scheduling Logic
Vehicles are sorted based on their priority to duration ratio. Depots are then processed based on their available mechanic hours. Tasks are assigned greedily such that:
- The total assigned duration does not exceed the depot capacity
- Each vehicle is assigned only once

### Optimization Goal
The objective is to maximize the total priority of all scheduled tasks across depots.

## Logging System
A logging module is implemented to track application events. It attempts to send logs to the external logging API endpoint. Each log contains the following fields:
- stack
- level
- package
- message

If the API fails due to timeout or connection issues, logs are printed to the console as a fallback.

## API Handling
The system integrates with the following endpoints:
- /auth for token generation
- /logs for sending logs

During development, the API was unstable and frequently returned timeouts or connection reset errors. To ensure continuity, a fallback token is used when the authentication request fails.

## Project Structure

vehicle-maintenance/
│
├── app.py
├── api/
│   └── client.py
├── scheduler/
│   └── scheduler.py
├── logger/
│   └── logger.py
├── utils/
│   └── config.py
├── requirements.txt
└── README.md

## How to Run

Create a virtual environment:
python3 -m venv venv

Activate it:
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Run the application:
python app.py

## Sample Output

=== FINAL SCHEDULE ===

Depot 3  
Total Priority: 22  
Vehicle 1 | Duration: 3 | Priority: 5  
Vehicle 3 | Duration: 5 | Priority: 8  

Overall Priority Achieved: 22  

## Limitations
- The greedy approach may assign all tasks to a single depot if it has sufficient capacity
- API instability required fallback handling

## Future Improvements
- Implement a dynamic programming approach for optimal scheduling
- Improve distribution of tasks across depots
- Add a REST API interface using a framework such as Flask or FastAPI
- Store logs in a persistent database

## Conclusion
This project demonstrates structured backend development, implementation of a scheduling algorithm, and handling of real-world issues such as unreliable external APIs.# RA2311028020012
