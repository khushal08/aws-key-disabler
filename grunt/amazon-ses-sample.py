import boto3
from yattag import Doc
from botocore.exceptions import ClientError

# Replace sender@example.com with your "From" address.
# This address must be verified with Amazon SES.
SENDER = "KK <khushal08@yahoo.com>"

# Replace recipient@example.com with a "To" address. If your account
# is still in the sandbox, this address must be verified.
RECIPIENT = "khushal08@yahoo.com"

# Specify a configuration set. If you do not want to use a configuration
# set, comment the following variable, and the
# ConfigurationSetName=CONFIGURATION_SET argument below.
# CONFIGURATION_SET = "ConfigSet"

# If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
AWS_REGION = "us-west-2"
doc, tag, text = Doc().tagtext()
a1 = [1, 2, 3]
a2 = [4, 5, 6]
d = {'a1': a1, 'a2': a2}
with tag('html'):
    with tag('body'):
        with tag('p', id = 'main'):
            for key in d.keys():
                if key == 'a1':
                    with tag('p'):
                        text('a1 = %s' % d[key])
                elif key == 'a2':
                    with tag('p'):
                        text('a2 = %s' % d[key])
                else:
                    text('someother test')

result = doc.getvalue()
# print result

BODY_HTML = result

# The subject line for the email.
SUBJECT = "Amazon SES Test (SDK for Python)"

# The HTML body of the email.
# BODY_HTML = """<html>
# <head></head>
# <body>
#   <h1>Amazon SES Test (SDK for Python)</h1>
#   <p>This email was sent with
#     <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
#     <a href='https://aws.amazon.com/sdk-for-python/'>
#       AWS SDK for Python (Boto)</a>.</p>
# </body>
# </html>
#             """

# The character encoding for the email.
CHARSET = "UTF-8"

# Create a new SES resource and specify a region.
client = boto3.client('ses',region_name=AWS_REGION)

# Try to send the email.
try:
    #Provide the contents of the email.
    response = client.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER,
        # If you are not using a configuration set, comment or delete the
        # following line
        # ConfigurationSetName=CONFIGURATION_SET,
    )
# Display an error if something goes wrong.
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    print("Email sent! Message ID:"),
    print(response['ResponseMetadata']['RequestId'])
