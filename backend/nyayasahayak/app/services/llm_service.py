"""LLM service for generating simplified explanations in Marathi and Hindi.

# TODO: Integrate with a real LLM API (OpenAI, Gemini, or local model):
#
# Example with OpenAI:
#   import openai
#   client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])
#   response = client.chat.completions.create(
#       model="gpt-4",
#       messages=[
#           {"role": "system", "content": "You are a legal expert. Explain in simple Marathi."},
#           {"role": "user", "content": f"Simplify this legal text: {text}"}
#       ]
#   )
#
# Example with Google Gemini:
#   import google.generativeai as genai
#   genai.configure(api_key=os.environ["GEMINI_API_KEY"])
#   model = genai.GenerativeModel("gemini-pro")
#   response = model.generate_content(prompt)
"""
import logging
from typing import Dict

logger = logging.getLogger(__name__)


def generate_explanation(text: str, risk_score: str) -> Dict[str, str]:
    """
    Generate simplified explanations in Marathi and Hindi.
    Falls back to predefined responses when no LLM API is configured.
    
    # TODO: Replace with actual LLM API call for dynamic generation
    """
    logger.info(f"Generating explanation for risk level: {risk_score}")

    # --- Fallback predefined explanations based on risk level ---
    explanations = {
        "High": {
            "marathi": (
                "या करारामध्ये काही अत्यंत कठोर अटी आहेत ज्या तुमच्यासाठी गंभीर "
                "धोका निर्माण करू शकतात. यामध्ये दंड, करार समाप्ती, आणि जबाबदारीच्या "
                "कलमांचा समावेश आहे. कृपया कायदेशीर सल्लागाराचा सल्ला घ्या. "
                "या कराराच्या अटी तुमच्या हक्कांवर गंभीर परिणाम करू शकतात."
            ),
            "hindi": (
                "इस अनुबंध में कुछ बहुत सख्त शर्तें हैं जो आपके लिए गंभीर जोखिम "
                "पैदा कर सकती हैं। इसमें जुर्माना, अनुबंध समाप्ति, और देयता की "
                "धाराएं शामिल हैं। कृपया कानूनी सलाहकार से परामर्श करें। "
                "इस अनुबंध की शर्तें आपके अधिकारों पर गंभीर प्रभाव डाल सकती हैं।"
            ),
        },
        "Medium": {
            "marathi": (
                "या करारामध्ये काही अटी आहेत ज्या तुम्हाला काळजीपूर्वक वाचणे आवश्यक "
                "आहे. काही कलमांमध्ये निर्बंध आणि अटी आहेत ज्या तुमच्या अधिकारांवर "
                "परिणाम करू शकतात. सावधगिरीने पुढे जा."
            ),
            "hindi": (
                "इस अनुबंध में कुछ शर्तें हैं जिन्हें आपको ध्यान से पढ़ना चाहिए। "
                "कुछ धाराओं में प्रतिबंध और शर्तें हैं जो आपके अधिकारों को "
                "प्रभावित कर सकती हैं। सावधानी से आगे बढ़ें।"
            ),
        },
        "Safe": {
            "marathi": (
                "या करारामध्ये कोणत्याही मोठ्या जोखमीच्या अटी आढळल्या नाहीत. "
                "हा करार सामान्यतः सुरक्षित दिसतो. तरीही, संपूर्ण करार वाचण्याची "
                "शिफारस केली जाते."
            ),
            "hindi": (
                "इस अनुबंध में कोई बड़ी जोखिम वाली शर्तें नहीं पाई गईं। "
                "यह अनुबंध सामान्यतः सुरक्षित प्रतीत होता है। फिर भी, पूरा "
                "अनुबंध पढ़ने की सिफारिश की जाती है।"
            ),
        },
    }

    return explanations.get(risk_score, explanations["Safe"])
