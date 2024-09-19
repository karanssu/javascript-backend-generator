import os
import sys
import subprocess
import json


def is_valid_path(path):
    return os.path.isdir(path)


def get_current_file_path():
    if hasattr(sys, "frozen"):
        # If the application is running as an executable
        file_path = sys.executable
    else:
        # If the application is running as a Python script
        file_path = os.path.abspath(__file__)

    # Get the directory containing the file
    directory_path = os.path.dirname(file_path)
    return directory_path


def get_target_path():
    result = input(
        "Enter the full path of the folder to generate the JavaScript backend: "
    ).strip()

    if result in ["", ".", "./"]:
        return get_current_file_path()
    elif not is_valid_path(result):
        print("\nERROR: invalid path!!! try again...\n")
        return get_target_path()

    return result


def change_dir(path):
    try:
        os.chdir(path)
        print(f"Successfully changed the current directory to: {os.getcwd()}")
        return True
    except FileNotFoundError:
        print(f"The path '{path}' does not exist.")
        return False
    except NotADirectoryError:
        print(f"The path '{path}' is not a directory.")
        return False
    except PermissionError:
        print(f"Permission denied to access '{path}'.")
        return False


def create_directories(path):
    try:
        os.makedirs(path, exist_ok=True)
        return True
    except OSError as e:
        print(f"Directory creation failed with error: {e}")
        return False


def run_command(command):
    try:
        # Run the command
        result = subprocess.run(
            command, shell=True, check=True, text=True, capture_output=True
        )

        # Print the command's output
        if result.stdout:
            print(f"\n{result.stdout}\n")

        # Print any errors (if there are any)
        if result.stderr:
            print(f"\nError:\n{result.stderr}\n")
            return False

    except subprocess.CalledProcessError as e:
        print(f"\nCommand failed with error: {e}\n")
        return False

    return True


def create_git_ignore_file():
    if not run_command("echo # Logs > .gitignore"):
        return

    if not run_command("echo logs >> .gitignore"):
        return

    if not run_command("echo *.log >> .gitignore"):
        return

    if not run_command("echo npm-debug.log* >> .gitignore"):
        return

    if not run_command("echo yarn-debug.log* >> .gitignore"):
        return

    if not run_command("echo yarn-error.log* >> .gitignore"):
        return

    if not run_command("echo. >> .gitignore"):
        return

    if not run_command("echo # Dependency directories >> .gitignore"):
        return

    if not run_command("echo node_modules/ >> .gitignore"):
        return

    if not run_command("echo. >> .gitignore"):
        return

    if not run_command("echo # Environment variables >> .gitignore"):
        return

    if not run_command("echo .env >> .gitignore"):
        return

    if not run_command("echo. >> .gitignore"):
        return

    if not run_command("echo # IDE or editor specific >> .gitignore"):
        return

    if not run_command("echo .vscode/ >> .gitignore"):
        return

    if not run_command("echo .idea/ >> .gitignore"):
        return

    if not run_command("echo. >> .gitignore"):
        return

    if not run_command("echo # OS-specific files >> .gitignore"):
        return

    if not run_command("echo .DS_Store >> .gitignore"):
        return

    if not run_command("echo Thumbs.db >> .gitignore"):
        return

    if not run_command("echo. >> .gitignore"):
        return

    if not run_command("echo # Debugging >> .gitignore"):
        return

    if not run_command("echo *.swp >> .gitignore"):
        return


def create_server_file():
    if not run_command('echo const express = require("express"); > server.js'):
        return

    if not run_command("echo const app = express(); >> server.js"):
        return

    if not run_command('echo const cors = require("cors"); >> server.js'):
        return

    if not run_command("echo. >> server.js"):
        return

    if not run_command('echo require("dotenv").config(); >> server.js'):
        return

    if not run_command(
        "echo const SERVER_PORT = process.env.SERVER_PORT ^|^| 8000; >> server.js"
    ):
        return

    if not run_command("echo. >> server.js"):
        return

    if not run_command('echo app.use(cors({ origin: "*" })); >> server.js'):
        return

    if not run_command("echo app.use(express.json()); >> server.js"):
        return

    if not run_command("echo. >> server.js"):
        return

    if not run_command("echo // user >> server.js"):
        return

    if not run_command(
        'echo app.use("/user", require("./routes/user/users")); >> server.js'
    ):
        return

    if not run_command("echo. >> server.js"):
        return

    if not run_command("echo app.listen(SERVER_PORT, (req, res) =^> ^{ >> server.js"):
        return

    if not run_command("echo     console.log( >> server.js"):
        return

    if not run_command(
        "echo         `Backend Server is running on port ${SERVER_PORT}...` >> server.js"
    ):
        return

    if not run_command("echo     ); >> server.js"):
        return

    if not run_command("echo }); >> server.js"):
        return


def create_dot_env_file():
    if not run_command("echo SERVER_PORT=4000 > .env"):
        return


def create_route_dir():
    return create_directories("routes/user")


def create_user_file():
    if not run_command(
        'echo const express = require("express"); > routes/user/users.js'
    ):
        return

    if not run_command("echo const router = express.Router(); >> routes/user/users.js"):
        return

    if not run_command("echo. >> routes/user/users.js"):
        return

    if not run_command(
        'echo router.get("/", async (req, res) =^> { >> routes/user/users.js'
    ):
        return

    if not run_command("echo     const users = { >> routes/user/users.js"):
        return

    if not run_command('echo         "testuser": { >> routes/user/users.js'):
        return

    if not run_command('echo             "name": "test", >> routes/user/users.js'):
        return

    if not run_command('echo             "age": "-1", >> routes/user/users.js'):
        return

    if not run_command('echo             "gender": "unknown" >> routes/user/users.js'):
        return

    if not run_command("echo         } >> routes/user/users.js"):
        return

    if not run_command("echo     }; >> routes/user/users.js"):
        return

    if not run_command("echo. >> routes/user/users.js"):
        return

    if not run_command("echo     return res.json(users); >> routes/user/users.js"):
        return

    if not run_command("echo }); >> routes/user/users.js"):
        return

    if not run_command("echo. >> routes/user/users.js"):
        return

    if not run_command("echo module.exports = router; >> routes/user/users.js"):
        return


def add_start_script_to_package_json():
    file_path = "package.json"

    if not os.path.isfile(file_path):
        print(f"File {file_path} does not exist.")
        return

    # Read the existing package.json file
    with open(file_path, "r") as file:
        data = json.load(file)

    # Check if the 'scripts' section exists and add the new line
    if "scripts" in data:
        if "start" not in data["scripts"]:
            data["scripts"]["start"] = "node server.js"
        else:
            print("The 'start' script already exists.")
            return
    else:
        print("The 'scripts' section does not exist.")
        return

    # Write the updated content back to package.json
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Updated {file_path} with 'start' script.")


def run():
    target_path = get_target_path()

    if change_dir(target_path):
        if not run_command("npm init -y"):
            return

        if not run_command("npm install express dotenv cors"):
            return

        create_git_ignore_file()
        create_server_file()
        create_dot_env_file()
        create_route_dir()
        create_user_file()
        add_start_script_to_package_json()

        print(
            "\n\nInstallation complete.\n"
            "To start the server, use the command: `npm start`\n"
            "Then, open your browser and navigate to: http://localhost:4000/user"
        )

    input("\n\nPress any key to exit...")


run()
