import boto3
translate_client = boto3.client('translate')
def lambda_handler(event, context): 
    review_text = event['text']
    translate_response = translate_client.translate_text(
        Text=review_text,
        SourceLanguageCode='en',
        TargetLanguageCode='ko'
    )
    print(translate_response)    
    return translate_response['TranslatedText']
