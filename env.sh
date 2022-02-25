
HERE="."
CONT="y" # empty means to not continue

[ -n "${CONT}" ] && [ ! -d venv ] && python3 -m venv ${HERE}/venv && echo "+++ python env created" 
IN_ENV=$(pip -V | awk '{print $4}' | grep venv)
[ -n "${CONT}" ] && [ -n "${IN_ENV}" ] && echo "+++ already in venv" && CONT=""
[ -n "${CONT}" ] && [ -z "${IN_ENV}" ] && source ${HERE}/venv/bin/activate && echo "+++ python env activated"