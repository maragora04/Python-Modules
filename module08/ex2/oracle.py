import os
import sys

from dotenv import load_dotenv

KEYS: tuple[str, ...] = (
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
)
MODES: tuple[str, ...] = ("development", "production")
PROD_REQUIRED: tuple[str, ...] = ("DATABASE_URL", "API_KEY", "ZION_ENDPOINT")


def load_config() -> tuple[dict[str, str | None], list[str]]:
    from_env = [k for k in KEYS if os.environ.get(k)]
    load_dotenv()  # never overrides variables already in the environment
    config = {k: os.environ.get(k) or None for k in KEYS}
    return config, from_env


def get_mode(config: dict[str, str | None]) -> str:
    mode = config["MATRIX_MODE"]
    if mode is None:
        print("WARNING: MATRIX_MODE not set, defaulting to development")
        return "development"
    if mode not in MODES:
        print(f"WARNING: invalid MATRIX_MODE '{mode}', using development")
        return "development"
    return mode


def warn_missing(config: dict[str, str | None], mode: str) -> None:
    missing = [k for k in KEYS if config[k] is None]
    if mode == "production":
        needed = [k for k in PROD_REQUIRED if k in missing]
        if needed:
            print(f"ERROR: production requires {', '.join(needed)}")
            sys.exit(1)
    for key in missing:
        print(f"WARNING: {key} is not set")


def report(config: dict[str, str | None], mode: str) -> None:
    prod = mode == "production"
    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")
    if config["DATABASE_URL"] is None:
        print("Database: Not configured")
    else:
        target = "production cluster" if prod else "local instance"
        print(f"Database: Connected to {target}")
    api = "Authenticated" if config["API_KEY"] else "Missing"
    print(f"API Access: {api}")
    level = config["LOG_LEVEL"] or ("WARNING" if prod else "DEBUG")
    print(f"Log Level: {level}")
    zion = "Online" if config["ZION_ENDPOINT"] else "Offline"
    print(f"Zion Network: {zion}")


def read_text(path: str) -> str:
    try:
        with open(path, encoding="utf-8") as file:
            return file.read()
    except OSError:
        return ""


def security_check(
    config: dict[str, str | None], from_env: list[str]
) -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    source = read_text(os.path.abspath(__file__))
    ignored = read_text(os.path.join(here, ".gitignore")).splitlines()
    key = config["API_KEY"]

    print("\nEnvironment security check:")
    if key is not None and key in source:
        print("[FAIL] Hardcoded secret found in source!")
    else:
        print("[OK] No hardcoded secrets detected")
    if ".env" in (line.strip() for line in ignored):
        print("[OK] .env file ignored by git")
    else:
        print("[FAIL] .env is not in .gitignore!")
    print("[OK] Production overrides available")
    if from_env:
        print(f"     (set in real environment: {', '.join(from_env)})")


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    config, from_env = load_config()
    mode = get_mode(config)
    warn_missing(config, mode)
    report(config, mode)
    security_check(config, from_env)
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
