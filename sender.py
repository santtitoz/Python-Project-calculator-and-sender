import phonenumbers
from phonenumbers import geocoder
import requests

# Função para obter informações do número de telefone
def get_phone_number_info(phone_number):
    phoneNumber = phonenumbers.parse(phone_number)
    
    valid = phonenumbers.is_valid_number(phoneNumber)
    possible = phonenumbers.is_possible_number(phoneNumber)
    region = geocoder.description_for_number(phoneNumber, 'pt-br')
    
    return valid, possible, region

# Configurações da API do Twilio
TWILIO_ACCOUNT_SID = 'AC980fa6c34a19b3aa52654c38b3ab5a3d'
TWILIO_AUTH_TOKEN = 'f9f8ecdb909ed2a0d3e72551e3ad0095'
TWILIO_PHONE_NUMBER = '+17695532761'

def enviar_mensagem_twilio(destinatario, mensagem):
    url = f'https://api.twilio.com/2010-04-01/Accounts/{TWILIO_ACCOUNT_SID}/Messages.json'
    
    payload = {
        'To': destinatario,
        'From': TWILIO_PHONE_NUMBER,
        'Body': mensagem
    }

    response = requests.post(url, auth=(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN), data=payload)

    return response.status_code

if __name__ == "__main__":
    user_input = input("Digite um número de telefone: ")
    phone_number_info = get_phone_number_info(user_input)

    valid, possible, region = phone_number_info

    if valid:
        print("O número de telefone é válido.")
        mensagem = input("Digite a mensagem que deseja enviar: ")
        destinatario = user_input

        status_code = enviar_mensagem_twilio(destinatario, mensagem)

        if status_code == 201:
            print("Mensagem enviada com sucesso!")
        else:
            print("Ocorreu um erro ao enviar a mensagem.")
    else:
        print("O número de telefone é inválido.")