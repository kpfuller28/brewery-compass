# Brewery Compass
Brewery Compass is a Flask app for brewery and cidery enthusiasts. Search for breweries by city, track visited spots in the Explored list with ratings, and save future destinations in the On My Radar list. Navigate your brewing adventures with ease, whether you're discovering new places or revisiting favorites.

### Project Setup & Workflow

1. **Fork and Clone the Repository**:
   - Fork this repository to your own GitHub account.
   - Clone the repository to your local machine using:
     ```bash
     git clone <repository-url>
     ```

2. **Install Dependencies**:
   - Navigate to the project directory:
     ```bash
     cd brewery-compass
     ```
   - Install the required Python dependencies from `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

3. **Setup Environment Variables**:
   - Create a `.env` file in the root of your project directory:
     ```bash
     touch .env
     ```
   - Add the following variables to your `.env` file:
     ```env
     API_URL='https://api.openbrewerydb.org/v1/breweries'
     DB_URI='sqlite:///your-database-file.db'  # Example: for SQLite, specify your database URI
     SECRET_KEY='your-secret-key'               # A random string for secure sessions
     ```

4. **Run the Application**:
   - Run the application using:
     ```bash
     python app.py
     ```

5. **Access the App**:
   - Open your browser and go to `http://localhost:5000` to view the app.