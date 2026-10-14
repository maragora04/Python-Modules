import alchemy.transmutation.recipes


print("=== Transmutation 0 ===")
print("Using file alchemy/transmutation/recipes.py directly")
print("Testing lead to gold: "
    f"{alchemy.transmutation.recipes.lead_to_gold()}")


# Paths !!
# Absolute is explicit and works from anywhere 
# relative is compact and survives renaming 
# Use relative inside the package and absolute to reach things outside it