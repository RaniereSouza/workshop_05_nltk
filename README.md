# Workshop 05 - Processamento de Linguagem Natural em Python com NLTK
*MATC96 2021.1 - Raniere de Souza Santos - 209102498*

___

## Requisitos básicos do ambiente
* Python 3 (compatível com a versão 3.6.9)
* *pip* (compatível com a versão 9.0.1)
* *venv* (ou *virtualenv* para Python 2.x) 
* *nltk* (compatível com a versão 3.6.2)
* *numpy* (compatível com a versão 1.19.5; necessário para o subpacote *nltk.chunk*)

___

## Instalando o Python 3
[Siga as instruções daqui](https://www.python.org/downloads/) para instalar a versão adequada para seu sistema, Windows ou Linux/MacOS.

___

## Instalando o *pip*
Normalmente, ao instalar o Python na sua máquina, o *pip* já vem como parte dele. Para garantir que a versão mais recente do *pip* está instalada, use o comando `python -m pip install --user --upgrade pip`.

___

## Não há instalação do *venv*, o mesmo é imbuído no Python a partir da versão 3.6
Caso você vá usar o Python numa versão 2.x, o equivalente do *venv* é o pacote *virtualenv*, que vai precisar ser instalado globalmente e manualmente.
### Por quê o *venv*?
Para manipular projetos em Python sem a necessidade de instalar pacotes globalmente. O *venv* permite que os pacotes usados no seu projeto sejam persistidos apenas localmente, num ambiente virtual.

___

## Criando e ativando um ambiente virtual do Python
* Primeiramente, navegue para a pasta do projeto
* O comando `python -m venv venv` vai criar uma pasta chamada "venv" dentro do projeto, que vai representar o ambiente virtual utilizado
* Para ativar o ambiente virtual, utilize o comando `source ./venv/bin/activate` (existe um comando alternativo no Windows, [mais detalhes aqui](https://docs.python.org/3/library/venv.html#module-venv))
* Para desativar o ambiente virtual, basta usar o comando `deactivate` dentro do diretório com o ambiente ativo

___

## Instalando o *nltk* (e o *numpy*) no ambiente virtual do Python
* Com o ambiente virtual ativo, use o comando `pip install nltk numpy`, que vai instalar o *nltk* (e também o *numpy*) e suas dependências
* Após a instalação, use o comando `pip freeze > requirements.txt`, para salvar a lista de dependências do projeto e suas versões num arquivo chamado "requirements.txt"
### **Detalhe importante:** caso seu projeto já contenha um arquivo "requirements.txt", ao invés de instalar as dependências manualmente no seu ambiente, apenas use o comando `pip install -r requirements.txt` (como é o caso do projeto neste repositório)

___

## Rodando a demonstração do projeto
(em breve)
