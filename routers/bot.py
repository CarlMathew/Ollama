from . import chatbot
from fastapi import FastAPI, status, HTTPException, Depends, APIRouter, Request
from schemas import *



router = APIRouter(tags=["Posts"])


@router.get("/test", status_code =  status.HTTP_200_OK)

async def HellWorld(
    query_params: Params = Depends(Params),
    request: Request = None
):
    bot = chatbot.OllamaChat()
    data = bot.message(query_params.question)
    message, input_data, output_data =  data

    try:
        return [{
            "message": message,
            "input": input_data,
            "output": output_data
        }] 
    except:
        return {"message": "Sorry there's been a problem internally."}
    

 
