def newton_raphson(f, df, p0, TOL=1e-6, N0=50):
    """Algoritmo 2.3. Devuelve (p, historia), con historia = [p0, p1, ..., p]."""
    historia = [p0]
    i = 1
    while i <= N0:
        d = df(p0)
        if d == 0:
            raise ZeroDivisionError(f"f'(p0) = 0 en p0 = {p0}: la tangente es horizontal")
        p = p0 - f(p0) / d
        historia.append(p)
        if abs(p - p0) < TOL:
            return p, historia
        i = i + 1
        p0 = p
    raise RuntimeError(f"El método fracasó después de {N0} iteraciones")

# Prueba e impresión Ejercicio 1
f1 = lambda x: x**3 + 4*x**2 - 10
df1 = lambda x: 3*x**2 + 8*x
sol1, hist1 = newton_raphson(f1, df1, 1.5, TOL=1e-6)

print("=== EJERCICIO 1 ===")
print(f"Solución p: {sol1:.6f}")
print(f"p1, p2, p3: {hist1[1]:.6f}, {hist1[2]:.6f}, {hist1[3]:.6f}\n")