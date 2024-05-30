# OWASP Top Ten Web Scraper

This project is a web scraper that extracts the OWASP Top Ten security risks from the [OWASP website](https://owasp.org/www-project-top-ten/) and displays them in a Streamlit web application. The application allows users to view the top ten security risks, download the data as a CSV file, and visualize the risks using metric cards.

## Features

- Web scraping of the OWASP Top Ten security risks
- Display of the risks using Streamlit metric cards
- DataFrame view of the risks
- Download the risks data as a CSV file

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Zyquier/owasp.git
   cd owasp
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


pip install -r requirements.txt



streamlit run app.py



Project Structure
app.py: The main Streamlit application script.
requirements.txt: The list of required Python packages.
README.md: This README file.
Dependencies
The project uses the following Python packages:

requests: To make HTTP requests to the OWASP website.
beautifulsoup4: To parse HTML content.
pandas: To handle data in DataFrame format.
streamlit: To create the web application.
streamlit-extras: For additional Streamlit components (metric cards).
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
The OWASP Foundation for providing the OWASP Top Ten data.
The developers of the open-source libraries used in this project.
Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

Contact
If you have any questions or suggestions, please open an issue or contact the repository owner.













### Explanation:

- **Title and Description**: Provide a brief overview of the project.
- **Features**: List the main features of the project.
- **Installation**: Step-by-step instructions to set up the project locally.
- **Usage**: Instructions on how to run the application.
- **Project Structure**: Describe the main files and directories in the project.
- **Dependencies**: List the main dependencies used in the project.
- **License**: Mention the license under which the project is distributed.
- **Acknowledgements**: Give credit to any resources or tools you used.
- **Contributing**: Provide guidelines for contributing to the project.
- **Contact**: Information on how to contact the project owner.

You can customize this `README.md` as per your project requirements. Save this content in a file named `README.md` in your project directory.
