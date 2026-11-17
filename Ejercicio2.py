def secante(f, p0, p1, TOL=1e-6, N0=50):
    """Algoritmo 2.4. Devuelve (p, historia), con historia = [p0, p1, p2, ..., p]."""
    i = 2
    q0 = f(p0)
    q1 = f(p1)
    historia = [p0, p1]

    while i <= N0:
        if q1 == q0:
            raise ZeroDivisionError(f"q1 == q0 ({q1}) en iteración {i}: la secante es horizontal")

        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        historia.append(p)

        if abs(p - p1) < TOL:
            return p, historia

        i = i + 1
        p0, q0 = p1, q1
        p1, q1 = p, f(p)

    raise RuntimeError(f"El método fracasó después de {N0} iteraciones")

# Prueba e impresión Ejercicio 2 (con contador de llamadas)
llamadas = []
def f2(x):
    llamadas.append(x)
    return x**3 + 4*x**2 - 10

sol2, hist2 = secante(f2, 1, 2, TOL=1e-6)

print("=== EJERCICIO 2 ===")
print(f"p2, p3, p4, p5: {hist2[2]:.6f}, {hist2[3]:.6f}, {hist2[4]:.6f}, {hist2[5]:.6f}")
print(f"Evaluaciones de f: {len(llamadas)}\n")