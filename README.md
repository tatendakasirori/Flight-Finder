✈️ Flight Finder

A Python-based flight monitoring system that automates the search for
cheap flight deals using the Amadeus API and sends real-time WhatsApp
notifications via Twilio.
It integrates with a Google Sheet (through the Sheety API) that stores
destinations, IATA codes, and target prices — effectively creating an
automated personal flight deals assistant.

------------------------------------------------------------------------

🚀 Project Overview

The system connects multiple APIs and services to perform the following
workflow:

1.  DataManager: Reads and updates Google Sheets via the Sheety API.
    -   Retrieves cities and target prices.
    -   Checks if IATA codes are missing and updates them automatically.
2.  FlightSearch: Queries the Amadeus Flight Offers API for available
    flights.
    -   Authenticates using OAuth2.
    -   Searches for business-class flights from a default origin (LON)
        to all listed destinations over a 3-week window.
3.  FlightData: Filters and structures the raw flight data.
    -   Filters out flights that exceed the target price.
    -   Summarizes results into a concise structure.
4.  NotificationManager: Sends WhatsApp alerts using Twilio when cheap
    flights are found.

------------------------------------------------------------------------

🧩 Project Architecture

    ├── data_manager.py           # Handles Google Sheets data (read/write IATA codes)
    ├── flight_search.py          # Communicates with Amadeus API to find flights
    ├── flight_data.py            # Filters and summarizes flight data
    ├── notification_manager.py   # Sends WhatsApp notifications via Twilio
    ├── main.py                   # Main orchestrator script
    ├── .env                      # Environment variables (API keys and URLs)
    └── requirements.txt          # Python dependencies

------------------------------------------------------------------------

🧠 How It Works

1.  Initialization
    -   Load environment variables using dotenv.
    -   Initialize all service classes with API credentials.
2.  Google Sheet Check
    -   If any IATA codes are missing, they are fetched from Amadeus and
        written back.
3.  Flight Search
    -   Fetches flight offers for all destinations.
    -   Filters deals below a predefined target price.
4.  Notification Dispatch
    -   Sends a WhatsApp message for every flight deal that meets the
        criteria.

------------------------------------------------------------------------

⚙️ Setup Instructions

1. Clone the repository

    git clone https://github.com/tatendakasirori/Flight-Finder
    cd flight-Finder

2. Create and activate a virtual environment

    python -m venv venv
    source venv/bin/activate   # On macOS/Linux
    venv\Scripts\activate      # On Windows

3. Install dependencies

    pip install -r requirements.txt

4. Create a .env file

    touch .env

Populate it with your credentials:

    # Sheety API
    SH_URL=<your_google_sheet_endpoint>
    SH_AUTH=Bearer <your_sheety_token>

    # Amadeus API
    AMAD_API=<your_amadeus_api_key>
    AMAD_API_SECRET=<your_amadeus_api_secret>

    # Twilio API
    TWILIO_ACC_SID=<your_twilio_account_sid>
    TWILIO_KEY_SID=<your_twilio_key_sid>
    TWILIO_KEY_SECRET=<your_twilio_key_secret>
    WHATS_APP_FROM_NUM=whatsapp:+14155238886
    WHATS_APP_TO_NUM=whatsapp:+<your_verified_number>

5. Run the application

    python main.py

------------------------------------------------------------------------

🧾 Example Workflow

1.  The system checks if your Google Sheet has missing IATA codes.
2.  Missing codes are fetched automatically and updated.
3.  The program retrieves flight data for all destinations.
4.  If a flight is cheaper than the defined price in your Sheet, you get
    a WhatsApp message like:

  “Low price alert! Only £420 to fly from LON to DXB on 2025-11-03 until
  2025-11-09.”

------------------------------------------------------------------------

🔍 Dependencies

-   requests – API communication
-   python-dotenv – Environment variable management
-   twilio – WhatsApp notifications
-   datetime – Flight date computation

Install all dependencies with:

    pip install requests python-dotenv twilio

------------------------------------------------------------------------

🧱 Google Sheet Structure

Your Google Sheet (connected via Sheety API) should have the following
columns:

  | City      | IATA Code  | Lowest Price |
  |----------|-----------|--------------|
  | Paris    |   PAR     |     500      |
  | Dubai    |   DXB     |     450      |
  | New York |   JFK     |     400      |

------------------------------------------------------------------------

🧰 API References

-   Amadeus for Developers
-   Twilio WhatsApp API
-   Sheety API

------------------------------------------------------------------------

🧭 Future Improvements

-   Add support for multiple origin airports.
-   Integrate email notifications alongside WhatsApp.
-   Include machine learning for price trend prediction.
-   Store flight history for analytics.

------------------------------------------------------------------------


