import ai21
import requests

res = requests.post(
    "https://api.ai21.com/studio/v1/j1-jumbo/complete",
    headers={"Authorization": 'Bearer UbNRnwAaMn4WrDxgGvtMIAOM63yEuYFQ'},
    json={
        "prompt": " i want to open a beetle shop write a description for that\nto paste it in a heading of website in 50 words",
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