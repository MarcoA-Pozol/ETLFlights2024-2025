import pandas as pd
import random
from datetime import datetime, timedelta
import os

# Sample values for each column from the provided JSON-like input
sample_values = {
    "Airline": [
        "Delta Air Lines", "Emirates", "Southwest Airlines", "Lufthansa", "Volaris",
        "Qantas", "American Airlines", "AirAsia", "United Airlines", "Singapore Airlines",
        "Alaska Airlines", "Japan Airlines", "Spirit Airlines", "Turkish Airlines", "Air France",
        "JetBlue", "Cathay Pacific", "Frontier Airlines", "Qatar Airways", "Avianca",
        "Air Canada", "Ryanair", "ANA", "Hawaiian Airlines", "KLM",
        "Azul Brazilian Airlines", "Etihad Airways", "Allegiant Air", "Virgin Atlantic", "IndiGo"
    ],
    "Airplane Model": [
        "Boeing 737-800", "Airbus A380-800", "Boeing 737-700", "Boeing 747-8", "Airbus A320neo",
        "Boeing 787-9", "Boeing 777-300ER", "Airbus A320-200", "Airbus A350-900", "Boeing 787-8",
        "Airbus A321-200", "Airbus A220-300", "Airbus A350-1000", "Airbus A319-100", "Airbus A330-300",
        "Airbus A330-200", "Boeing 787-10", "Embraer E195", "Boeing 737-900", "Boeing 737 MAX 8",
        "Boeing 777-300", "Boeing 767-400", "Boeing 777-200LR", "Boeing 777-200", "Boeing 757-200"
    ],
    "Origin": ["ATL", "DXB", "DAL", "FRA", "MEX", "SYD", "DFW", "KUL", "ORD", "LAX"],
    "Destination": ["JFK", "LHR", "SIN", "HOU", "CUN", "AKL", "HNL", "CDG", "NRT", "SFO"],
    "Flight Type": ["Domestic", "International"],
    "Pilot Name": [
        "Capt. Jessica Lee", "Capt. Ahmed Al-Farsi", "Capt. Sophia Müller", "Capt. Hiro Tanaka",
        "Capt. Luis Hernández", "Capt. Emily Clark", "Capt. Jean Dupont", "Capt. Ravi Patel"
    ],
    "Flight Status": ["Completed", "Delayed", "Cancelled"],
    "Fuel Type": ["Jet A", "Jet A-1"],
    "Service Class": ["Economy", "First Class", "Business", "Premium Economy"],
    "Delay Reason": ["-", "Weather", "Technical Issues", "Air Traffic Control", "Crew Availability"]
}

paths = ["./DataSets/flights_2024A.csv", "./DataSets/flights_2024B.csv", "./DataSets/flights_2024C.csv", "./DataSets/flights_2024D.csv", "./DataSets/flights_2024E.csv", "./DataSets/flights_2024F.csv", "./DataSets/flights_2024G.csv", "./DataSets/flights_2024H.csv", "./DataSets/flights_2024I.csv", "./DataSets/flights_2024J.csv", "./DataSets/flights_2024K.csv", "./DataSets/flights_2024L.csv"]
for path in paths:
    # Generate the dataset
    num_flights = 1500
    flights_data = []

    start_date = datetime(2024, 1, 1)
    for _ in range(num_flights):
        flight = {
            "Airline": random.choice(sample_values["Airline"]),
            "Airplane Model": random.choice(sample_values["Airplane Model"]),
            "Origin": random.choice(sample_values["Origin"]),
            "Destination": random.choice(sample_values["Destination"]),
            "Date": (start_date + timedelta(days=random.randint(0, 364))).strftime("%Y-%m-%d"),
            "Flight Type": random.choice(sample_values["Flight Type"]),
            "Pilot Name": random.choice(sample_values["Pilot Name"]),
            "Departure Time": f"{random.randint(0, 23):02}:{random.choice([0, 15, 30, 45]):02}:00",
            "Flight Status": random.choice(sample_values["Flight Status"]),
            "Delay Minutes": random.choice([0, 5, 10, 15, 20, 25, 30, "-", 45, 60]),
            "Fuel Type": random.choice(sample_values["Fuel Type"]),
            "Service Class": random.choice(sample_values["Service Class"]),
            "Delay Reason": random.choice(sample_values["Delay Reason"])
        }
        flights_data.append(flight)

    # Create a DataFrame
    flights_df = pd.DataFrame(flights_data)

    # Save to CSV
    os.makedirs(os.path.dirname(path), exist_ok=True)
    flights_df.to_csv(path, index=False)

    path
