[![Parallelize Jobs](https://github.com/Wvrmhat/Finance-Automation-Tool/actions/workflows/docker-build.yml/badge.svg)](https://github.com/Wvrmhat/Finance-Automation-Tool/actions/workflows/docker-build.yml)

# Finance-Automation-Tool
Finance Dashboard that takes in a CSV of a banking statement, and displays it in a more clean and readable format. Supports custom expense categories and automatic tagging based off keywords. Also includes a graphical summary of expenses to display how money was being used.

## Features

- Upload and parsing CSV files
- Categorize transactions using keyword-based logic
- Visual summary of expenses in a pie chart 
- Tab for tracking debit/credit transactions 

## Notable Libraries 
- Streamlit library used to build the webapp and main GUI as well as saving session   
state
- Plotly used for a visual representation of expenses 
- JSON used to save category data and track keywords

![Main page](https://github.com/Wvrmhat/Finance-Automation-Tool/screenshots/image1.png)

![Categories](https://github.com/Wvrmhat/Finance-Automation-Tool/screenshots/image2.png)

![Expense Summary](https://github.com/Wvrmhat/Finance-Automation-Tool/screenshots/image3.png)

![Payment Summary](https://github.com/Wvrmhat/Finance-Automation-Tool/screenshots/image4.png)

---
> [!NOTE]
> Images that have been tagged and pushed to Docker hub can be found here https://hub.docker.com/repositories/wvrmhat. 
