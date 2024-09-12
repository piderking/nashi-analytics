create:
    python3 -m venv .env
install:
    pip3 install -r requirements.txt
run $script:
    python src/$script