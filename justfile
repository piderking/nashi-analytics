create:
    python3 -m venv .env
install:
    pip3 install -r requirements.txt
run $line $script:
    python src/$line/$script