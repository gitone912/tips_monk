import ai21
import requests

res = requests.post(
    "https://api.ai21.com/studio/v1/j1-jumbo/complete",
    headers={"Authorization": 'Bearer UbNRnwAaMn4WrDxgGvtMIAOM63yEuYFQ'},
    json={
        "prompt": " how to lose weight ",
        "numResults": 1,
        "maxTokens": 2048,
        "temperature": 0.97,
        "topKReturn": 0,
        "topP": 1,
        "countPenalty": {
            "scale": 0,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False,
        },
        "frequencyPenalty": {
            "scale": 185,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False,
        },
        "presencePenalty": {
            "scale": 0.4,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False,
        },
        "stopSequences": ["##"],
    },
)
print(res.json())