import json
import re
from sqlalchemy.orm import Session

from app.models.models import Booking
from app.prompts.booking_prompt import BOOKING_PROMPT
from app.services.gemini_service import ask_gemini


def create_booking(
    db: Session,
    name: str,
    email: str,
    date: str,
    time: str
):
    booking = Booking(
        name=name,
        email=email,
        date=date,
        time=time
    )

    db.add(booking)
    db.commit()
    db.refresh(booking)

    return booking


def extract_and_save_booking(db: Session, message: str):
    """
    Extract booking information from user message and save to database.
    Returns: (success: bool, booking_data: dict, message: str)
    """
    try:
        # Get booking extraction from LLM
        booking_prompt = BOOKING_PROMPT.format(message=message)
        response = ask_gemini(booking_prompt)
        
        print(f"DEBUG: LLM Response: {response}")
        
        # Try to find JSON in response
        json_match = re.search(r'\{.*\}', response, re.DOTALL)
        if json_match:
            json_str = json_match.group()
            booking_data = json.loads(json_str)
        else:
            booking_data = json.loads(response.strip())
        
        print(f"DEBUG: Parsed booking data: {booking_data}")
        
        # Check if we have at least name and email
        if not booking_data.get("name") or not booking_data.get("email"):
            return False, None, "Could not extract booking details. Please provide name and email."
        
        # Save to database
        booking = create_booking(
            db,
            name=booking_data.get("name"),
            email=booking_data.get("email"),
            date=booking_data.get("date"),
            time=booking_data.get("time")
        )
        
        print(f"DEBUG: Booking saved with ID: {booking.id}")
        
        confirmation = f"✅ Booking confirmed! Interview scheduled for {booking_data.get('name')} ({booking_data.get('email')}) on {booking_data.get('date')} at {booking_data.get('time')}."
        return True, booking_data, confirmation
        
    except json.JSONDecodeError as e:
        print(f"DEBUG: JSON Decode Error: {e}")
        print(f"DEBUG: Response was: {response}")
        return False, None, "Error processing booking response. Please try again."
    except Exception as e:
        print(f"DEBUG: Unexpected error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False, None, f"Error saving booking: {str(e)}"