from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.chat_schema import (
    ChatRequest,
    ChatResponse
)

from app.services.redis_service import (
    save_chat,
    get_chat_history
)

from app.services.retrieval_service import (
    retrieve_context
)

from app.services.gemini_service import (
    ask_gemini
)

from app.services.booking_service import (
    extract_and_save_booking
)

from app.db.database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


def is_booking_request(message: str) -> bool:
    """Check if the message is requesting a booking"""
    booking_keywords = ["book", "schedule", "appointment", "interview", "meeting", "reserve"]
    message_lower = message.lower()
    result = any(keyword in message_lower for keyword in booking_keywords)
    print(f"DEBUG: is_booking_request('{message}') = {result}")
    return result


@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):
    # Check if this is a booking request
    if is_booking_request(request.message):
        success, booking_data, message = extract_and_save_booking(db, request.message)
        if success:
            save_chat(request.session_id, request.message)
            save_chat(request.session_id, message)
            return ChatResponse(answer=message)
    
    # Normal chat flow
    history = get_chat_history(
        request.session_id
    )

    context = retrieve_context(
        request.message
    )

    prompt = f"""
    Previous Chat:
    {history}

    Context:
    {context}

    User:
    {request.message}

    Answer professionally.
    """

    answer = ask_gemini(prompt)

    save_chat(
        request.session_id,
        request.message
    )

    save_chat(
        request.session_id,
        answer
    )

    return ChatResponse(answer=answer)