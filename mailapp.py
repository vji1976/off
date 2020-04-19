from exchangelib import Account, Credentials, Configuration, DELEGATE
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
import warnings

smtp_server = 'webmail.olopparish.org'
primary_addr = 'viarocci@olopparish.org'
username = 'olop\\viarocci'
userpass = 'F0rg1ve'

# setup account credentials and configuration for connection
creds = Credentials(username=username, password=userpass)
config = Configuration(server=smtp_server, credentials=creds)

# setup insecure connection and warning suppression because our
# mail server sucks
BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

# create our account and connect
email = Account(primary_smtp_address=primary_addr, config=config,
				autodiscover=False, access_type=DELEGATE)
				
unread_emails = email.inbox.unread_count
all_emails = email.inbox.total_count
email.inbox.refresh()
# first_ten = email.inbox.all().order_by('-subject')[:10]  # Efficient. We only fetch 10 items
unread = email.inbox.filter(is_read=False)   # returns unread emails
print(len(unread))

"""
for i in range(10):
			item = account.inbox.all().order_by('-datetime_received')[i]
			self.emails.append(item)
"""
"""
for msg in a.inbox.filter(datetime_received__gt=emails_since, is_read=False)\
        .only('datetime_received', 'subject', 'text_body')\
        .order_by('datetime_received')[:10]:
    subj = 'New mail: %s' % msg.subject
    clean_body = '\n'.join(l for l in msg.text_body.split('\n') if l)
    notify(subj, clean_body[:200])
"""
