echo "setting up the project"
echo "creating venv"
python3 -m venv .env
. .env/bin/activate
pip install -r requirements.txt
deactivate