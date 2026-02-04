import langchain
from dotenv import load_dotenv
load_dotenv()

print(langchain.__version__)

import os
print(os.getenv("GOOGLE_API_KEY"))
