RAG Backend


"Instructions for .env file"
--"
GEMINI_API_KEY=your_key_here

QDRANT_HOST=localhost
QDRANT_PORT=6333

REDIS_HOST=localhost
REDIS_PORT=6379

DATABASE_URL=sqlite:///./rag.db
"  --

Running process:
 -Run Qdrant and Redis using docker:
    "docker run -p 6333:6333 qdrant/qdrant"
    "docker run -p 6379:6379 redis"
 -Requirements(if needed):
   " pip install -r requirements.txt "
 -Run Backend:
   "uvicorn app.main:app --reload"
  -Server running at: http://127.0.0.1:8000/
                    : http://127.0.0.1:8000/docs




  PROFF (Also in the folder "Screenshots" above):
  -Custom RAG Backend
  <img width="1900" height="913" alt="1" src="https://github.com/user-attachments/assets/6c8410e1-3a2a-4e8c-944e-65709dbb71bf" />

  -Uploading files:
  <img width="1903" height="1015" alt="2" src="https://github.com/user-attachments/assets/4313f642-0fe4-4773-8537-51ce8e2dd88a" />
  <img width="1886" height="1013" alt="3" src="https://github.com/user-attachments/assets/4005ffa2-26ef-491b-a30b-0dfa7276a7d2" />

  -Chat and chat history:
  <img width="1918" height="1078" alt="4" src="https://github.com/user-attachments/assets/5d79e664-d2d6-4c21-be38-2f897bd6758a" />
  <img width="1916" height="1078" alt="5" src="https://github.com/user-attachments/assets/c71725a1-92cb-4c62-9eb6-3a4783c22333" />
  <img width="1903" height="967" alt="6" src="https://github.com/user-attachments/assets/fcbe2f87-fb03-4307-a77c-c08f9f094e12" />
  <img width="1918" height="1078" alt="7" src="https://github.com/user-attachments/assets/ffdf9331-309c-4cf0-a56d-c7ea4424ef2b" />

  -Booking and save booking:
  <img width="1905" height="1078" alt="8" src="https://github.com/user-attachments/assets/c3026eae-1ab4-4bd0-85cf-ee7841c6a6e5" />
  <img width="1525" height="647" alt="9" src="https://github.com/user-attachments/assets/7d048675-a34d-481e-87b1-0ae35254dbe5" />
  <img width="1918" height="1077" alt="10" src="https://github.com/user-attachments/assets/9715219e-4b6b-42da-80c7-1acb4bcf5fd9" />



  
