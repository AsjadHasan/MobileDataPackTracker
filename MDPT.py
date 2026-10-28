"""Track mobile data usage and prevent exceeding the data limit."""
class DataPack:
    """Represent a mobile data pack for a user."""
    def __init__(self, owner, total_gb):
        """Initialize the owner and total data allowance."""
        self.owner = owner
        self.total_gb = total_gb
        self.used_gb = 0
    def remaining(self):
        """Return the amount of data remaining."""
        return self.total_gb - self.used_gb
    def use(self, gb):
        """Use data only if it does not exceed the remaining limit."""
        if gb <= 0:
            print("Please enter a data amount greater than 0 GB.")
            return
        if gb > self.remaining():
            print(
                f"Not enough data left. "
                f"Only {self.remaining()} GB remaining."
            )
            return
        self.used_gb += gb
        print(f"{self.owner} used {gb} GB")
    def display_remaining(self):
        """Display the remaining data allowance."""
        print(f"Remaining: {self.remaining()} GB")
# Get data pack information from the user.
owner = input("Enter owner's name: ")
while True:
    try:
        total_gb = float(input("Enter total data pack (GB): "))
        if total_gb <= 0:
            print("Total data must be greater than 0.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")
pack = DataPack(owner, total_gb)
# Repeatedly accept data usage until the user exits.
while True:
    usage = input("\nEnter data to use in GB (or 'done' to finish): ")

    if usage.lower() == "done":
        break
    try:
        gb = float(usage)
        pack.use(gb)
    except ValueError:
        print("Please enter a valid number or 'done'.")
# Display final remaining data.
pack.display_remaining()