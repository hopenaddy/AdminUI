from fabric.api import put, run
from fabvenv import Venv

ROOT = "/opt/lv128/AdminUI"
def deploy():
    venv = Venv(ROOT, "requirements.txt")
    if not venv.exists():
        venv.create()
    venv.install()
    put("requirements.txt")
    put("loginsys", ROOT)
    put("adminUI", ROOT)
    put("my_app", ROOT)
    put("manage.py", ROOT)
    put("db.sqlite3", ROOT)
    put("lv128_adminUI.service", ROOT)
    run("sudo mv %s/lv128_adminUI.service /etc/systemd/system/" % ROOT)
    run("sudo systemctl enable lv128_adminUI")
    run("sudo systemctl restart lv128_adminUI")
