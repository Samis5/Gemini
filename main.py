from google import genai

client = genai.Client(api_key= "AQ.Ab8RN6KBeVn-xZlltKEKXSALat1106sEnwWrNgY-KTk5iS4aSw")

while True:
    question = input("You:  ")

    if question.lower() =="exit" : break

    response = client.models.generate_content(
            model ="gemini-3.6-flash",
            contents=question
    )

    print("Gemini:",response.text)

