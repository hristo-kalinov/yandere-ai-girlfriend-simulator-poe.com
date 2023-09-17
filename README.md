# yandere-ai-girlfriend-simulator-poe.com
This repo will allow the game yandere ai girlfriend simulator to use any model on poe.com instead of OpenAI's ChatGPT

#### Prerequisites
Before getting started, ensure you have the following requirements installed on your system:

Python (compatible version, preferably the latest version)

Administrative access to the command prompt (CMD)
#### Step 1: Dependendcies
Open a CMD window with administrative privileges.

Install the required dependencies by running the following command:
```pip install -r requirements.txt```
#### Step 2: Generating Certificates
Execute the following command in the CMD window:
```python CertificateGenerator.py```
This will generate two files: **certificate.pem** and **private_key.pem**.

Next, follow these steps to add the certificate to the **Trusted Root Certification Authorities**:
1. Press Win + R, type certmgr.msc, and press Enter to open the Certificate Manager.
2. In the Certificate Manager, navigate to Trusted Root Certification Authorities.
3. Right-click on Certificates, go to All Tasks, and select Import....
4. Follow the wizard, choose any of the two options provided, and click Next.
5. Browse to the location of the certificate.pem file. If you don't see it, make sure to select All Files in the file dialog.
6. Select the option Place all certificates in the following store: Trusted Root Certification Authorities (this option should have been automatically selected).
7. Click Next, then Finish to complete the import process.

#### Step 3: Setting Up Local Hosts
Execute the following command in the CMD window:

```python hosts.py```

In the prompt, select option 1.
#### Step 4: Configuring the Web Server
Open the file webserver.py in your favorite text editor.

Navigate to the website poe.com in your web browser.

Open the Developer Tools (usually accessible through F12 or right-clicking and selecting "Inspect" or "Developer Tools").

In the Developer Tools window, go to the Application tab and click on Cookies.

Locate the **p-b** value under the poe.com cookies, and copy its content.

In the **webserver.py** file, find the variable **TOKEN** and paste the copied **p-b** value as its new value.

Also, optionally, if you want to use a different bot, find the appropriate bot value from the comment in the code and change the value accordingly (It uses ChatGPT by default).

#### Step 5: Starting the Web Server
Execute the following command in the CMD window:

```python webserver.py```

Launch the game and input a random value as the API key.

Link to the game: https://helixngc7293.itch.io/yandere-ai-girlfriend-simulator
