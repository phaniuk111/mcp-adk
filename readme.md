# Testing ADK Integration with gcloud CLI MCP Server

Follow these steps to test ADK integration with the gcloud CLI MCP server:

## Steps

1. **Create a Virtual Environment**  
   Run the following command to create a virtual environment named `venv`:

   ```bash
   python3 -m venv venv
   ```

2. **Activate the Virtual Environment**  
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

3. **Install Dependencies**  
   Use `pip` to install the dependencies listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Authenticate with gcloud**  
   Run the following command to log in:

   ```bash
   gcloud auth application-default login
   ```

5. **Initiate ADK Web Locally**  
   Start the ADK web interface:

   ```bash
   adk web
   ```
