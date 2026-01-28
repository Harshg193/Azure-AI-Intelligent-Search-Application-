import logging
import json
import azure.functions as func

# Initialize the Function App for Python V2 Model (Required for Flex Consumption)
app = func.FunctionApp()

def predict_category(text):
    """
    Analyzes text to determine urgency keywords.
    """
    text_lower = text.lower()
    if 'urgent' in text_lower or 'deadline' in text_lower:
        return 'High-Priority'
    elif 'archive' in text_lower or 'old' in text_lower:
        return 'Archived'
    else:
        return 'Standard'

@app.route(route="classify_document", auth_level=func.AuthLevel.ANONYMOUS)
def classify_document(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Custom Skill (ML Model) triggered.')

    try:
        body = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid request body", status_code=400)

    # Azure AI Search sends records in a "values" array
    values = body.get('values', [])
    results = {"values": []}

    for value in values:
        record_id = value.get('recordId')
        data = value.get('data', {})
        text = data.get('text', '')

        try:
            # Run the classification logic
            category = predict_category(text)
            results["values"].append({
                "recordId": record_id,
                "data": { "category": category },
                "errors": None,
                "warnings": None
            })
        except Exception as e:
            results["values"].append({
                "recordId": record_id,
                "errors": [{"message": str(e)}]
            })

    return func.HttpResponse(
        json.dumps(results),
        mimetype="application/json"
    )