import sympy as sp


def solve_expression(expression):

    x = sp.symbols("x")

    try:
        result = sp.sympify(expression)

        return str(result)

    except Exception as e:
        return str(e)


def differentiate(expression):

    x = sp.symbols("x")

    try:
        expr = sp.sympify(expression)

        return str(sp.diff(expr, x))

    except Exception as e:
        return str(e)


def integrate(expression):

    x = sp.symbols("x")

    try:
        expr = sp.sympify(expression)

        return str(sp.integrate(expr, x))

    except Exception as e:
        return str(e)


def solve_equation(expression):

    x = sp.symbols("x")

    try:
        expr = sp.sympify(expression)

        return str(sp.solve(expr, x))

    except Exception as e:
        return str(e)