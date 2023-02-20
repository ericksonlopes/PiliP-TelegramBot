FROM python:3.11

# Defina o diretório de trabalho no container
WORKDIR /pilip

# Copie o conteúdo do seu projeto para o container
COPY . .

# Instale as dependências do seu projeto
RUN pip install -r requirements.txt

# Execute o comando quando o container for iniciado
CMD [ "python", "main.py" ]