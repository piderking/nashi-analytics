echo $1
#find ./src/$1 -maxdepth 1 -type f -exec echo "%s" +;
find ./src/$1 -maxdepth 1 -type f | while read -r i
do
    echo "Running... $i"
    python3 "$i"
done