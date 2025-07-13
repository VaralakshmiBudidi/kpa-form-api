from pydantic import BaseModel
from datetime import date

class WheelFields(BaseModel):
    treadDiameterNew: str
    lastShopIssueSize: str
    condemningDia:str
    wheelGauge:str
    variationSameAxle:str
    variationSameBogie:str
    variationSameCoach:str
    wheelProfile:str
    intermediateWWP:str
    bearingSeatDiameter:str
    rollerBearingOuterDia:str
    rollerBearingBoreDia:str
    rollerBearingWidth:str
    axleBoxHousingBoreDia:str
    wheelDiscWidth:str
    class Config:
        from_attributes=True

class Wheel(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields:WheelFields
    class Config:
        from_attributes=True
