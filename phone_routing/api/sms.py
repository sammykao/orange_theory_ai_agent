from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.email_service import send_email
from services import a2a_agent_service

router = APIRouter()

class SMSPayload(BaseModel):
    sender: str # Expecting an email-able address like 1234567890@carrier.com
    message: str

@router.post("/incoming-sms")
async def incoming_sms(payload: SMSPayload):
    # Query the a2a agent with the incoming message
    agent_response = a2a_agent_service.query_agent(payload.message)

    # The 'sender' from the payload should be the address to reply to.
    # Zapier should be configured to provide the sender's full email-to-sms address.
    to_address = payload.sender
    subject = ""
    
    if send_email(to_address, subject, agent_response):
        return {"status": "Response sent successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to send response")

# Encoding fix 