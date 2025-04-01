import numpy as np
from scipy.optimize import newton


def mean_return():
    """Arithmetic mean of periodic returns."""
    try:
        returns = list(map(float, input("Enter periodic returns (comma-separated): ").split(',')))
        mean = np.mean(returns)
        print(f"Arithmetic Mean Return: {mean:.4f} or {mean*100:.2f}%\n")
    except ValueError:
        print("Invalid input.\n")


def geometric_mean_return():
    """Geometric mean (compounded) return."""
    try:
        returns = list(map(float, input("Enter periodic returns (comma-separated): ").split(',')))
        product = np.prod([1 + r for r in returns])
        geometric_mean = product ** (1/len(returns)) - 1
        if geometric_mean < -1:
            print("Error: Negative value due to invalid returns (e.g., <-100%).\n")
        else:
            print(f"Geometric Mean Return: {geometric_mean:.4f} or {geometric_mean*100:.2f}%\n")
    except ValueError:
        print("Invalid input. Use numbers separated by commas.\n")


def irr_calculator():
    """Internal Rate of Return (IRR)."""
    try:
        cash_flows = list(map(float, input("Enter cash flows (comma-separated): ").split(',')))
        irr = newton(lambda r: sum(cf / (1 + r)**i for i, cf in enumerate(cash_flows)), x0=0.1)
        print(f"IRR: {irr:.4f} or {irr*100:.2f}%\n")
    except RuntimeError as e:  # Catch specific solver error
        print(f"IRR could not be calculated: {e}\n")
    except ValueError:
        print("Invalid cash flows.\n")


def annualized_return():
    """Annualized a return over a period."""
    try:
        total_return = float(input("Total return (decimal, e.g., 0.5 for 50%): "))
        years = float(input("Time period (years): "))
        annualized = (1 + total_return) ** (1/years) - 1
        print(f"Annualized Return: {annualized:.4f} or {annualized*100:.2f}%\n")
    except ValueError:
        print("Invalid input. Use numbers.\n")


def continuously_compounded_return():
    """Continuously compounded return (ln)."""
    try:
        start = float(input("Initial investment (e.g., 1000): "))
        end = float(input("Ending value: "))
        cc_return = np.log(end / start)
        print(f"Continuously Compounded Return: {cc_return:.4f} or {cc_return*100:.2f}%\n")
    except ValueError:
        print("Invalid input. Use numbers.\n")


# Submenu for Quantitative Methods
def quantitative_method_submenu():
    while True:
        print("\n=== Quantitative Methods ===")
        tools = {
            "1": ("Arithmetic Mean Return", mean_return),
            "2": ("Geometric Mean Return", geometric_mean_return),
            "3": ("IRR Calculator", irr_calculator),
            "4": ("Annualized Return", annualized_return),
            "5": ("Continuously Compounded Return", continuously_compounded_return),
            "0": ("Back to Main Menu", None)
        }
        for k, (name, _) in tools.items():
            print(f"{k}. {name}")

        sub_choice = input("\nSelect a tool (1-5) or 0 to return: ")
        if sub_choice == "0":
            break
        elif sub_choice in tools and tools[sub_choice][1]:
            tools[sub_choice][1]()
        else:
            print("Invalid choice. Try again.\n")


# Main menu
def main_menu():
    print("\n=== CFA level 1 Toolkit ===")
    chapters = {
        "1": "Quantitative Methods",
        "2": "Economics",
        "3": "Corporate Issuers",
        "4": "Financial Statement Analysis",
        "5": "Equity Investments",
        "6": "Fixed Income",
        "7": "Derivatives",
        "8": "Alternative Investments",
        "9": "Portfolio Management",
        "10": "Ethics",
        "0": "Exit"
    }
    for k, value in chapters.items():
        print(f"{k}. {value}")

    choice = input("\nSelect a chapter (1-10) or 0 to exit: ")
    return choice


if __name__ == "__main__":
    while True:
        user_choice = main_menu()
        if user_choice == "0":
            print("Exiting...")
            break
        elif user_choice == "1":
            quantitative_method_submenu()
        else:
            print("Invalid choice. Try again.")
