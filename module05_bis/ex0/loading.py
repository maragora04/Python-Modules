import importlib
import importlib.metadata


REAGENTS = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation" } # name, purpose


def get_version(name: str) -> str:
    try:
        version = module.__version__
    except AttributeError:
        version = "unknown"


def check_reagents() -> list[str]:
    missing: list[str] = []
    print("Checking dependencies:")
    for name, purpose in REAGENTS.items():
        try:
            importlib.import_module(name)
            version = importlib.metadata.version(name)
        except (ImportError, importlib.metadata.PackageNotFoundError):
            print(f"[MISSING] {name} - {purpose} unavailable")
            missing.append(name)
            continue
        print(f"[OK] {name} ({version}) - {purpose} ready")
    return missing


def print_install_help(missing: list[str]) -> None:
    print()
    print("Missing reagents: " + ", ".join(missing))
    print("Install them with one of:")
    print("pip: pip install -r ex0/requirements.txt")
    print("Poetry: poetry install")


def print_comparison() -> None:
    print()
    print("pip vs Poetry:")
    print("requirements.txt declares what to install; "
          "pip resolves it at install time.")
    print("pyproject.toml declares the same constraints, and Poetry pins the \
    resolved versions in poetry.lock so every install is identical.")


def main() -> None:
    print("REAGENT STATUS: Loading reagents...")
    print()
    missing = check_reagents()
    print_comparison()
    if missing:
        print_install_help(missing)
    else:
        print()
        print("All reagents present and accounted for.")


if __name__ == "__main__":
    main()