from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from oled.display import create_display
from utils.logger_factory import create_logger
from web.fast_resp import CommonResponse



app = FastAPI()
display = create_display()
logger = create_logger('api')

class TextLine(BaseModel):
    text: str
    x: int = 0
    y: int = 0
    font_size: Optional[int] = None

@app.exception_handler(Exception)
async def universal_exception_handler(request, exc: Exception):
    return CommonResponse(code=1, message=str(exc))

# curl -X POST  -H 'Content-Type: application/json' http://localhost:8003/display/reset
@app.post("/display/reset")
async def display_reset():
    logger.info("display_reset")
    try:
        display.reset()
        result_data = {}
        return CommonResponse(code=0, message="OK", data=result_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

# curl -X POST  -H 'Content-Type: application/json' -d '{"text":"Hello, SSD1306!", "x":10, "y":10}' http://localhost:8003/display/line
@app.post("/display/text/line")
async def display_text_line(item: TextLine):
    logger.info("display_text: {}".format(item))
    try:
        display.display_text_line(item.text, item.x, item.y, font_size=item.font_size)
        result_data = {}
        return CommonResponse(code=0, message="OK", data=result_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/display/text/multiline")
async def display_text_multiline(lines: List[TextLine]):
    logger.info("display_multiline_text: {}".format(lines))
    try:
        display_data = [{"text": line.text, "x": line.x, "y": line.y, "font_size": line.font_size} for line in lines]
        display.display_text_multiline(display_data)
        result_data = {}
        return CommonResponse(code=0, message="OK", data=result_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/display/clear")
async def display_clear():
    logger.info("display_clear")
    try:
        display.clear()
        result_data = {}
        return CommonResponse(code=0, message="OK", data=result_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))