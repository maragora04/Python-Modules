import sys
from importlib import import_module
from types import ModuleType

REQUIRED: dict[str, str] = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
    "matplotlib": "Visualization",
}


def load_package(name: str) -> ModuleType | None:
    try:
        return import_module(name)
    except ImportError:
        return None


def print_install_help(missing: list[str]) -> None:
    print(f"\nMissing dependencies: {', '.join(missing)}\n")
    print("Install with pip:")
    print("  pip install -r requirements.txt")
    print("  python3 loading.py\n")
    print("Install with Poetry:")
    print("  poetry install")
    print("  poetry run python loading.py")


def check_dependencies() -> dict[str, ModuleType] | None:
    print("Checking dependencies:")
    loaded: dict[str, ModuleType] = {}
    missing: list[str] = []
    for name, purpose in REQUIRED.items():
        module = load_package(name)
        if module is None:
            print(f"[MISSING] {name} - {purpose} unavailable")
            missing.append(name)
        else:
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {name} ({version}) - {purpose} ready")
            loaded[name] = module
    if missing:
        print_install_help(missing)
        return None
    return loaded


def compare_managers() -> None:
    poetry_env = "pypoetry" in sys.prefix
    print("\nPip vs Poetry:")
    print(f"Running from: {sys.prefix}")
    print("Manager detected:", "Poetry" if poetry_env else "pip / other")
    print("pip    -> requirements.txt, installs into the active env,")
    print("          no lock file by default")
    print("Poetry -> pyproject.toml + poetry.lock, creates and manages")
    print("          its own venv, resolves version conflicts")


def analyze(mods: dict[str, ModuleType]) -> None:
    np = mods["numpy"]
    pd = mods["pandas"]
    mods["matplotlib"].use("Agg")  # no display needed
    plt = import_module("matplotlib.pyplot")

    print("\nAnalyzing Matrix data...")
    rng = np.random.default_rng(42)
    size = 1000
    df = pd.DataFrame({"signal": rng.normal(0, 1, size).cumsum()})
    df["average"] = df["signal"].rolling(50).mean()
    print(f"Processing {len(df)} data points...")
    print(f"Mean: {df['signal'].mean():.2f}, "
          f"max: {df['signal'].max():.2f}")

    print("Generating visualization...")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df["signal"], label="Matrix signal", alpha=0.5)
    ax.plot(df["average"], label="50-tick average")
    ax.set_title("Matrix data analysis")
    ax.legend()
    fig.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    mods = check_dependencies()
    if mods is None:
        sys.exit(1)
    analyze(mods)
    compare_managers()


if __name__ == "__main__":
    main()
