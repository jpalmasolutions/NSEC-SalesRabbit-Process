import json
from src.main.utils.aws import get_execution_item
from src.main.utils.logs import logger
from src.main.rabbit.rabbit import add_lead

def lambda_handler(event,context):
    if event:
        try:
            raw_message = event['Records'][0]['Sns']['Message']
            message = json.loads(raw_message)
            
            execution_id = message['execution_id']
            item = get_execution_item(execution_id)
            logger.info(item)
            add_lead(item['data'])

        except Exception as e:
            logger.error(str(e))