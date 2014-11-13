from fabric.api import put, run
from fabvenv import Venv

ROOT = "/opt/lv128/AdminUI"
def deploy():
    venv = Venv(ROOT, "requirements.txt")
    if not venv.exists():
        venv.create()
    venv.install()
    put("adminUI.settings", ROOT+"/adminUI")
    put("manage.py", ROOT)
    put("lv128_adminUI.service", ROOT)
    run("sudo mv %s/lv128_adminUI.service /etc/systemd/system/" % ROOT)
    run("sudo systemctl enable lv128_adminUI")
    run("sudo systemctl restart lv128_adminUI")
