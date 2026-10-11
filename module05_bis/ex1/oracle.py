import os
import sys
from dotenv import dotenv_values, load_dotenv

# !!! 
# python3 -m venv lab_env -- creating the environment
# source lab_env/bin/activate -- switching to it
# pip install python-dotenv -- installing dependencies
# python3 ex0/construct.py -- confirming the "lab is sealed"
# cp ex1/.env.example  ex1/.env -- copy from source 
# # (example) to destination (new env file)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(BASE_DIR, ".env")
GITIGNORE_PATH = os.path.join(BASE_DIR, ".gitignore")

KEYS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]
SECRET_KEYS = ["DATABASE_URL", "API_KEY"]


DEFAULTS = {
    "development": {
        "DATABASE_URL": "sqlite:///dev.db",
        "LOG_LEVEL": "DEBUG",
        "ZION_ENDPOINT": "http://localhost:8080",
    },
    "production": {
        "LOG_LEVEL": "WARNING",
    },
}
REQUIRED_IN_PRODUCTION = ["DATABASE_URL", "API_KEY", "ZION_ENDPOINT"]


def load_config() -> tuple[dict[str, str | None], dict[str, str], list[str]]:
    from_env = {key: os.environ.get(key) for key in KEYS}
    from_file = dotenv_values(ENV_PATH)  # if the file does not exist
    load_dotenv(ENV_PATH, override = False)  # real environment wins

    warnings: list[str] = []
    if not os.path.exists(ENV_PATH):
        warnings.append("No .env file found, using environment and defaults")

    mode = os.environ.get("MATRIX_MODE", "development")
    if mode not in DEFAULTS:
        warnings.append(f"Unknown MATRIX_MODE '{mode}', using development")
        mode = "development"

    config: dict[str, str | None] = {"MATRIX_MODE": mode}
    for key in KEYS[1:]:
        config[key] = os.environ.get(key) or DEFAULTS[mode].get(key)
        if config[key] is None:
            warnings.append(f"{key} is not set")

    sources: dict[str, str] = {}
    for key in KEYS:
        if from_env[key]:
            sources[key] = "environment"
        elif from_file.get(key):
            sources[key] = ".env"
        elif config[key]:
            sources[key] = "default"
        else:
            sources[key] = "missing"
    return config, sources, warnings


def describe_database(url: str | None) -> str:
    if url is None:
        return "Not configured"
    if url.startswith("sqlite") or "localhost" in url:
        return "Connected to local instance"
    return "Connected to remote instance"


def show_config(config: dict[str, str | None]) -> None:
    api_key = config["API_KEY"]
    endpoint = config["ZION_ENDPOINT"]
    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")
    print(f"Database: {describe_database(config['DATABASE_URL'])}")
    print("API Access: " + ("Authenticated" if api_key else "Not configured"))
    print(f"Log Level: {config['LOG_LEVEL'] or 'Not configured'}")
    print("Remote Network: " + ("Online" if endpoint else "Offline"))


def show_mode_details(
    config: dict[str, str | None], sources: dict[str, str]
) -> None:
    print()
    if config["MATRIX_MODE"] == "development":  # Development is verbose!!!!
        print("Development details (never shown in production):")
        for key in KEYS:
            print(f"{key}: {sources[key]}")
        print(f"Zion endpoint: {config['ZION_ENDPOINT']}")
    else:
        print("Production mode: strict, no defaults, details hidden.")


def source_has_secret() -> bool:
    with open(os.path.abspath(__file__), "r") as source_file: 
        code = source_file.read()
    for key in SECRET_KEYS:
        value = os.environ.get(key)
        if not value:
            continue
        if value == DEFAULTS["development"].get(key):
            continue
        if value in code:
            return True
    return False


def env_is_gitignored() -> bool:
    if not os.path.exists(GITIGNORE_PATH):
        return False
    with open(GITIGNORE_PATH, "r") as ignore_file:
        lines = [line.strip() for line in ignore_file.read().splitlines()]
    return ".env" in lines or "/.env" in lines


def security_check(sources: dict[str, str]) -> bool:
    ok = True
    print()
    print("Configuration security check:")
    if source_has_secret():
        print("[FAIL] Secret value found inside the source code")
        ok = False
    else:
        print("[OK] No hardcoded secrets detected")
    if env_is_gitignored():
        print("[OK] .env file properly ignored by git")
    else:
        print("[FAIL] .env is not listed in ex1/.gitignore")
        ok = False
    if "environment" in sources.values():
        print("[OK] Production overrides active (environment beats .env)")
    else:
        print("[OK] Production overrides available")
    return ok


def main() -> None:
    print("ORACLE STATUS: Consulting the configuration...")
    print()
    config, sources, warnings = load_config()
    show_config(config)
    show_mode_details(config, sources)

    if warnings:
        print()
        for warning in warnings:
            print(f"[WARN] {warning}")

    security_ok = security_check(sources)

    missing = [key for key in REQUIRED_IN_PRODUCTION if not config[key]]
    if config["MATRIX_MODE"] == "production" and missing:
        print()
        print("[ERROR] Production needs: " + ", ".join(missing))
        sys.exit(1)

    print()
    if security_ok:
        print("The Oracle sees all configurations.")
    else:
        print("The Oracle sees problems in the configuration.")


if __name__ == "__main__":
    main()
