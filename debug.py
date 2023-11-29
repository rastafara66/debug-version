import os
import sys

def on_debug_start():
    current_run_path = os.path.join(os.getcwd(), "atm", "D:\\OneDrive\\Projects\\odoo-addons16\\atm\\current_run")
    manifest_path = os.path.join(os.getcwd(), "atm", "D:\\OneDrive\\Projects\\odoo-addons16\\atm\\__manifest__.py")    
    version_line = ""

    with open(current_run_path, "r") as f:
        current_run = f.read()
    new_current_run = int(current_run) + 1

    with open(current_run_path, "w") as f:
        f.write(str(new_current_run))

    with open(manifest_path, "r") as f:
        manifest = f.read()
    with open(manifest_path, "r") as f:
        for line in f:
            if line[:29] == "    'version': '16.0.1.23.11.":
                old_version_line = line
                print(old_version_line)
                version_line = line[:29]
                    
    new_version_line = str(version_line) + str(new_current_run) + "',\n"
    print(new_version_line)
    manifest = manifest.replace(
        str(old_version_line),
        str(new_version_line)
    )

    with open(manifest_path, "w") as f:
        f.write(manifest)
    return 0

if __name__ == "__main__":
    on_debug_start()
