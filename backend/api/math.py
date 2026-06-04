from fastapi import APIRouter
from pydantic import BaseModel

from backend.math.math_service import (
    solve_expression,
    differentiate,
    integrate,
    solve_equation
)

router = APIRouter()


class MathRequest(BaseModel):
    expression: str


@router.post("/math/evaluate")
def evaluate(req: MathRequest):

    result = solve_expression(
        req.expression
    )

    return {
        "answer": result
    }


@router.post("/math/differentiate")
def diff(req: MathRequest):

    result = differentiate(
        req.expression
    )

    return {
        "answer": result
    }


@router.post("/math/integrate")
def integ(req: MathRequest):

    result = integrate(
        req.expression
    )

    return {
        "answer": result
    }


@router.post("/math/solve")
def solve(req: MathRequest):

    result = solve_equation(
        req.expression
    )

    return {
        "answer": result
    }