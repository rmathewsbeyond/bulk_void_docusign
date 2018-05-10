# Bulk Void Docusign Envelopes using Docusign for Salesforce

This script uses selenium to impersonate a user who is voiding the docusign status object records in salesforce.

How to use this bad boy:
- Set up a selenium driver (Chrome or Firefox)
- Create a credentials.py file and set the variables 'sf_username' and 'sf_password' to your salesforce credentials
- Create a list of all of the urls of the docusign status objects in salesforce  in the 'urls' variable (should look something like 'https://na8.salesforce.com/a45C0000000F3fh')
- The void_message is sent to the signer by default, so be aware
- You may have to adjust the xpaths based on your instance - just find the void button, the void message text box, and the final void button on your layout, right click and 'Inspect element', then right click the highlighted section and 'Copy Xpath'
- The final void click at the end of the try loop is commented out for testing - uncomment to actually void

NOTE - the salesforce user you login as must be associated with a docusign user that has permission to void all the envelopes you are attempting to void.
You can find a user in docusign.com and select the option "share users envelopes" and select yourself or alternatively find yourself and select "share envelopes with user" and select the users
