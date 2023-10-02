import pytest
from my_module import get_phone_number_info, enviar_mensagem_twilio

# Teste para a função get_phone_number_info
def test_get_phone_number_info():
    # Número de telefone válido no Brasil
    valid_number = "+5511999999999"
    valid, possible, region = get_phone_number_info(valid_number)
    assert valid
    assert possible
    assert region == "Brazil"

    # Número de telefone inválido
    invalid_number = "12345"
    valid, possible, region = get_phone_number_info(invalid_number)
    assert not valid

# Teste para a função enviar_mensagem_twilio
def test_enviar_mensagem_twilio():
    # Substitua pelos valores reais da sua conta Twilio
    TWILIO_ACCOUNT_SID = 'AC980fa6c34a19b3aa52654c38b3ab5a3d'
    TWILIO_AUTH_TOKEN = 'f9f8ecdb909ed2a0d3e72551e3ad0095'

    # Número de telefone válido no formato E.164
    destinatario = "+17695532761"
    mensagem = "Teste de mensagem Twilio"

    status_code = enviar_mensagem_twilio(destinatario, mensagem)
    assert status_code == 201  # Verifique se a resposta é 201 (Created)

    # Teste com número de telefone inválido
    destinatario_invalido = "12345"
    status_code = enviar_mensagem_twilio(destinatario_invalido, mensagem)
    assert status_code != 201  # A resposta não deve ser 201 para um número inválido

if __name__ == "__main__":
    pytest.main()