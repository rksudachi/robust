import streamlit.web.cli as stcli
from pathlib import Path
# import subprocess
import sys
import utilities.yamlparser as yp


# pyinstaller --onefile --copy-metadata streamlit .\run_app.py
if getattr(sys, 'frozen', False):
    current_dir = Path(sys.executable).parent
else:
    current_dir = Path(__file__).parent
src = (current_dir / "app.py").resolve()

config=yp.read_yaml()

sys.argv=['streamlit', 'run', src,f"--server.address={config.server.host}"