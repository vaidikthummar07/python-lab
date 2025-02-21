for a in range(1, 31):
    for b in range(a, 31):  # Start b from a to avoid duplicate triplets
        for c in range(b, 31):  # Start c from b to avoid duplicates
            if a**2 + b**2 == c**2:
                print(f"({a}, {b}, {c})")
