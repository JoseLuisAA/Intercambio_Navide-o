from shuffle import seleccion;
from shuffle import integrantes;

import smtplib;
import os;
from dotenv import load_dotenv;
from email.message import EmailMessage;
import ssl;
import smtplib;

load_dotenv();

reparto=seleccion(integrantes);



for i in range(len(reparto)):
    

    email_sender="tucorreo@gmail.com";#<----Modificar con el correo de gmail de donde se enviarán los correos
    password=os.getenv("PASSWORD");
    email_reciver=reparto[i][0]['correo'];

    subject="Intercambio de regalos";#<-----Asunto
    body="Hola " + reparto[i][0]['nombre'] + ",la persona a la que le darás el regalo es: \n" + reparto[i][1]['nombre']+ "\n\nOpciones de regalos:\n" + reparto[i][1]['regalos'];
    #<-----Cuerpo del correo

    em=EmailMessage();
    em["From"]=email_sender;
    em["To"]=email_reciver;
    em["Subject"]=subject;
    em.set_content(body);

    context=ssl.create_default_context();


    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
        smtp.login(email_sender,password);
        smtp.sendmail(email_sender,email_reciver,em.as_string());


'''
"Hola "+reparto[i][0]['nombre']+" esto es una prueba\nLos regalos que elegiste son:\n\n"+reparto[i][0]['regalos'];
'''