<!-- Beautiful README for Azure AI project -->
# Azure AI — Lightweight Skill + Static App

Welcome to the Azure AI example project — a compact demonstration that pairs a static front-end with a Python-based Azure Functions skill.

**What this project contains**
- **Purpose:** A minimal, extensible pattern for hosting a small static site and a serverless skill that can be used as a starting point for Azure Function-based AI integrations.
- **Stack:** Static HTML (client), Python Azure Function (skill), and an opinionated structure suitable for local dev and Azure deployment.

**Quick Links**
- **App (static):** [app/index.html](app/index.html)
- **Function (skill):** [skill/function_app.py](skill/function_app.py)
- **Function host config:** [skill/host.json](skill/host.json)
- **Python deps:** [skill/requirements.txt](skill/requirements.txt)
- **Docs:** [docs/Test_Documentation.md](docs/Test_Documentation.md)

**Project Structure**

- Root
  - app/: Static front-end files (open in a browser for a quick preview)
  - docs/: Project documentation and notes
  - skill/: Azure Function implementation (Python)

Why this layout? It keeps the front-end separate from serverless logic so you can develop, test, and deploy each part independently.

**Prerequisites**
- Python 3.10+ (or your target runtime)
- (Optional) Azure CLI and Azure Functions Core Tools for local function debugging and deployment
- Git (recommended)

**Local Setup**

1. Clone the repo:

```bash
git clone <your-repo-url>
cd <repo-folder>
```

2. Static app preview
- Open [app/index.html](app/index.html) in your browser for an instant preview — no server required.

3. Prepare the function environment

```bash
cd skill
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Windows CMD:
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

4. Run the Azure Function locally (requires Azure Functions Core Tools):

```bash
# from the skill/ folder
func start
```

The function will bind to a localhost port (usually 7071). Check the console for the exact endpoint.

**Deployment to Azure (brief)**

1. Log in to Azure and select subscription:

```bash
az login
az account set --subscription "<subscription-name-or-id>"
```

2. Create a Function App (example, Linux consumption plan):

```bash
az functionapp create --resource-group <rg> --consumption-plan-location <region> \
  --runtime python --functions-version 4 --name <app-name> --storage-account <storage-name>
```

3. Deploy code (using ZIP deploy or `func azure functionapp publish`):

```bash
# from the skill/ folder
func azure functionapp publish <app-name>
```

4. Serve the static `app/` directory using Azure Static Web Apps, Azure Blob Static Website, or any static hosting provider.

**Configuration & Environment**
- Add any settings or secrets to the Function App configuration in Azure (Portal or `az functionapp config appsettings set`).
- Example local settings can go into `local.settings.json` when using Functions Core Tools (do not commit secrets).

**Testing & Extending**
- The `skill/function_app.py` is a natural place to plug in AI/ML logic, third-party SDKs, or to forward requests to other services.
- Add unit tests alongside the function code and run them with `pytest`.

**Contribution**
- Improvements, bug fixes, or feature requests are welcome. Open an issue or submit a pull request.

**License & Contact**
- Add your project license file or choose an open-source license.
- For questions, include a contact or maintainer section here.

------
*This README is a friendly guide to get you up and running quickly.* If you’d like, I can also:

- Scaffold `local.settings.json` for local debugging
- Add a GitHub Actions workflow to build and deploy the function
- Add a tiny test harness for `skill/function_app.py`

Tell me which of the above you want next and I’ll implement it.
