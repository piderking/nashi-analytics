create:
    python3 -m venv .env
install:
    pip3 install -r requirements.txt
run $line $script:
    python src/$line/$script

encrypt $version $password:
    zip --password $password -r data-encrypted/data-$version.zip data

open $version $password:
    unzip -P $password -u data-encrypted/data-$version.zip 