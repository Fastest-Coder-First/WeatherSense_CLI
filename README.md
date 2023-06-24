# WeatherSense_CLI

The WeatherSense_CLI Tool is a command line interface application that allows users to obtain the current weather forecast for any city or country of their choice. By utilizing the OpenWeatherMap API and leveraging the power of Python, this tool provides accurate and up-to-date weather information in a simple and convenient manner.

## Installation

1. Clone the repository to your local machine:
```bash
git clone https://github.com/Fastest-Coder-First/WeatherSense_CLI.git
```
2. Navigate to the project directory:
```bash
cd WeatherSense_CLI
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Obtain an API key from OpenWeatherMap by creating an account on their website.

5. Rename the `.env.example` file to `.env` and replace `YOUR_API_KEY_HERE` with your actual OpenWeatherMap API key.

## Usage

To use the WeatherSense_CLI Tool, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the project directory.

3. Run the tool with the following command:
```bash
python weatherSense.py <city_name/country_name>
```

4. Wait for the tool to fetch and display the current weather forecast for the specified location.

## Dependencies

The WeatherSense_CLI Tool relies on the following dependencies:

- requests
- argparse
- pyfiglet
- simple-chalk
- python-dotenv

These dependencies are listed in the `requirements.txt` file and will be installed during the installation process.

## GitHub Copilot

The WeatherSense_CLI Tool was developed with the assistance of GitHub Copilot, an AI-powered coding assistant. Copilot provides helpful code suggestions and autocompletion, making development faster and more efficient. It helps in generating code snippets, suggesting function signatures, and even completing entire lines of code.

While using Copilot, it's important to review and validate the suggestions provided to ensure code quality and correctness. It can be a valuable tool to enhance productivity and assist in writing code more effectively.

## Acknowledgments

The WeatherSense_CLI Tool was developed using the OpenWeatherMap API, which provides the weather data used in this application. We would like to express our gratitude to the developers and contributors of OpenWeatherMap for their valuable service.