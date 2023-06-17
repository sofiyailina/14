digits = '0123456789ABCDEFGHIFKLMNOP'

for p in range(10, 27):
    for x in digits[:p]:
        for y in digits[:p]:
            n1 = int(f"{x}{x}{x}8", p)
            n2 = int(f"43{x}9", p)
            n3 = int(f"{y}{y}04", p)
            if n1 + n2 == n3:
                result = int(f"{y}{y}{x}", p)
                print(p, result)
                break
