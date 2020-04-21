#@markdown <h3>⬅️ Run This Cell to Install lynda_DL_Mine Requirements</h3>
import random, string, urllib.request, json, getpass, os, IPython, uuid
import ipywidgets as widgets

from IPython.display import HTML, clear_output

loadingBtn = widgets.Button(description = "Installing",
                          disabled = True,
                          button_style = 'warning', # 'success', 'info', 'warning', 'danger' or '' 
                          tooltip = "Installing",
                          icon = 'check')
display(loadingBtn)

if not os.path.exists("/opt/python3.8"):
  get_ipython().system_raw("rm -rf /content/sample_data/ && sudo apt update && sudo apt install software-properties-common")
  get_ipython().system_raw("sudo add-apt-repository ppa:deadsnakes/ppa")
  get_ipython().system_raw("sudo apt install python3.8")
  get_ipython().system_raw("sudo apt install python3-pip")
  get_ipython().system_raw("python3.8 -m pip install --upgrade pip setuptools wheel")
  get_ipython().system_raw("git clone https://github.com/r0oth3x49/lynda-dl.git /root/.lynda_DL_Mine")
  clear_output()

try:
  get_ipython().system_raw("python3.8 -m pip -q install -r /root/.skillshare_DL_Mine/requirements.txt")
  display(HTML("<center><h2 style=\"font-family:Trebuchet MS;color:#4f8bd6;\">Successfully Configured!</h2><br></center>"))
  
except:
  display(HTML("<center><h2 style=\"font-family:Trebuchet MS;color:#ff0000;\">Error Occured, Rerun the Cell!!</h2><br></center>")) 