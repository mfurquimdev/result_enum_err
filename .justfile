default: hot_reload

alias h := hot_reload

set dotenv-load := true

run:
    @echo -e "\n\033[1;7;37mExecuting main\033[0;1;0m"
    @python src/main.py

hot_reload:
    @echo "Hot reloading 'run' recipe with *.py"
    @fd --glob '*.py' . | entr just run
