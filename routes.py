from fastapi import APIRouter, HTTPException, status, Request
# from models import ExpressionRequest
from models import EvalResponse

from calc import Calculator

eval_router = APIRouter()


def check_phrase_format(phrase: str) -> bool:
    for sym in phrase:
        if sym not in [
            '0',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '-',
            '+',
            '/',
            '*',
            '(',
            ')',
            # '.',
        ]:
            return False

        # if 39 < ord(sym) < 44 or 44 < ord(sym) < 58:
        #     continue
        # else:
        #     return False
    return True


async def calculate_expression(expression: str) -> EvalResponse:
    if not check_phrase_format(expression.get('phrase', '')):
        return EvalResponse(full_response = "Wrong syntax!")
    
    try:
        calc_obj = Calculator()
        result = calc_obj.parse(expression.get('phrase', ''))

    except ZeroDivisionError:
        return EvalResponse(full_response = "Zero division error!")

    except SyntaxError:
        return EvalResponse(full_response = "Wrong syntax!")

    return EvalResponse(value=result, full_response=f"{expression.get('phrase', '')} = {result}")



@eval_router.get("/eval/calc")
async def get_eval(request: Request) -> str:
    response = await calculate_expression(request.query_params)

    if response.value is None:
        raise HTTPException(status_code = 400, detail = response.full_response)

    return response


@eval_router.post(
    "/eval/calc", 
    status_code = status.HTTP_201_CREATED,
)
async def post_eval(request: Request):
    response = await calculate_expression(request.query_params)

    if response.value is None:
        raise HTTPException(status_code=400, detail=dict(response))
    
    return response
