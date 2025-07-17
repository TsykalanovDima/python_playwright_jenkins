# Playwright Python CI/CD Jenkins

## 🚀 What it does

- Logs in to Saucedemo with test credentials.
- Checks that the products inventory page loads and all items are visible.
- Adds one or all products to the cart and verifies the cart.
- Runs a negative login test with wrong credentials.
- Generates a clear **HTML test report** (`pytest-html`).
- The Jenkins pipeline:
  - Creates a Python virtual environment.
  - Installs dependencies and Playwright browsers.
  - Runs the tests in **headless mode**.
  - Publishes the test report in Jenkins.
- For now, the Jenkins build is triggered **manually** from the Jenkins UI.

---
## Setup

Jenkins

[//]: # (Jenkins)

docker-compose up --build

[//]: # (open in browser)
open in browser http://localhost:8080

[//]: # (password)
docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
playwright install --with-deps
pytest --html=reports/report.html
