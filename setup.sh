virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
cat creds_template.json > creds.json