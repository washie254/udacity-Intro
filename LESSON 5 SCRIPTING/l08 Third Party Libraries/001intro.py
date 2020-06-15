#pip install pytz
from datetime import datetime 
import pytz

utc = pytz.utc
ist = pytz.timezone('Asia/Kolkata')

now = datetime.now(tz=utc)
ist_now = now.astimezone(ist)

print(now)
print(ist_now)

# installing packages from requirements file
# pip install -r requirements.txt