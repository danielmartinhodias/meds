import streamlit as st
from datetime import datetime

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# from docx import Document
# from docx.shared import Pt
# from docx.enum.text import WD_ALIGN_PARAGRAPH


# from docx2pdf import convert

from datetime import datetime

# Get current timestamp
timestamp = datetime.now()


st.subheader ("Pedido de medicação")

# st.button("**Declaração de doença**", use_container_width=True)
with st.form("my_form"):
    left, right=st.columns(2)

    nome = left.text_input("**Nome completo**")
    sns = right.text_input("Número de SNS")

    left, right=st.columns(2)
    queixa = left.text_input("Refira de forma sucinta os seus sintomas ou queixas")
    telefone = right.text_input("Contacto telefónico")

    agree = st.checkbox("Confirmo, sob compromisso de honra, ter já previamente informado o médico do motivo de doença e ter sido avaliado pelo mesmo")
    submitted = st.form_submit_button("Submeter pedido")

# After form submission
if submitted:
  if not nome or not sns or not queixa or not telefone or not agree:
    st.error("Pf preencher todos os campos prévios")
  else:
    try:
        # Email credentials
      sender_email = "danielmartinhodias@gmail.com"
      receiver_email = "danielmartinhodias@gmail.com"
      app_password = "dsxxuvwybaevopdu"

      # Email content
      subject = f"Pedido de medicação de_{nome}"
      body = f"Para prescrever por causa de {queixa} para {telefone}"

      # Create the email
      msg = MIMEMultipart()
      msg["From"] = sender_email
      msg["To"] = receiver_email
      msg["Subject"] = subject

      mensagem = f"Para prescrever por causa de {queixa} para {telefone}, submetida em {timestamp}"
      msg.attach(MIMEText(mensagem, 'plain'))

      # anexos = [f"./issued/declaracoes/dec_doenca{nome}.docx", f"./issued/declaracoes/dec_doenca{nome}.pdf"]

      # Anexar arquivos
      # for ficheiro in anexos:
      #     with open(ficheiro, 'rb') as f:
      #         parte = MIMEBase('application', 'octet-stream')
      #         parte.set_payload(f.read())
      #         encoders.encode_base64(parte)
      #         parte.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(ficheiro)}"')
      #         msg.attach(parte)

      # Enviar e-mail

      with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
          smtp.login(sender_email, app_password)
          smtp.send_message(msg)

      print("Email enviado com sucesso para o médico para validação. Aguarde contacto e resposta.")

    except:
      pass