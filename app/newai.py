import requests
import json
def tips(question):
    
    r = requests.post("https://api.ai21.com/studio/v1/experimental/j1-grande-instruct/complete",
        headers={"Authorization": "Bearer UbNRnwAaMn4WrDxgGvtMIAOM63yEuYFQ"},
        json={
            "prompt": question,
            "numResults": 1,
            "maxTokens": 974,
            "temperature": 0.84,
            "topKReturn": 0,
            "topP":1,
            "countPenalty": {
                "scale": 0,
                "applyToNumbers": False,
                "applyToPunctuations": False,
                "applyToStopwords": False,
                "applyToWhitespaces": False,
                "applyToEmojis": False
            },
            "frequencyPenalty": {
                "scale": 185,
                "applyToNumbers": False,
                "applyToPunctuations": False,
                "applyToStopwords": False,
                "applyToWhitespaces": False,
                "applyToEmojis": False
            },
            "presencePenalty": {
                "scale": 0.4,
                "applyToNumbers": False,
                "applyToPunctuations": False,
                "applyToStopwords": False,
                "applyToWhitespaces": False,
                "applyToEmojis": False
        },
        "stopSequences":["##"]
        }
    )
    assert r.status_code == 200, r.json()
    return(r.json()['completions'][0]['data']['text'])

