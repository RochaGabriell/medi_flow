# MediFlow

## Projeto de Desenvolvimento de Software: Sistema de Gerenciamento de Consultório Médico

**MediFlow** é um sistema de gerenciamento de consultório médico desenvolvido em Django. Este projeto visa proporcionar uma solução completa para a gestão de pacientes, agendamento de consultas, prontuários médicos, faturamento e administração de recursos. O sistema é projetado para ser escalável e flexível, permitindo futuras implementações em diversas tecnologias.

## Descrição do Projeto

O objetivo do MediFlow é fornecer uma plataforma que permita a gestão eficiente de todos os aspectos de um consultório médico. O sistema foi desenvolvido com foco na usabilidade e segurança, visando atender às necessidades tanto de médicos quanto de pacientes, além de possibilitar a administração de recursos e a geração de relatórios importantes.

## Requisitos Funcionais

1. **Cadastro de Pacientes**

   - Permite o cadastro, edição e exclusão de pacientes.
   - Informações dos pacientes incluem nome, idade, sexo, endereço, contato e histórico médico.

2. **Agendamento de Consultas**

   - Permite que pacientes agendem consultas.
   - Exibe uma visualização de calendário com horários disponíveis e ocupados.

3. **Prontuário Eletrônico**

   - Permite que médicos registrem e consultem o histórico médico dos pacientes.
   - Suporta o upload de exames e documentos em formatos diversos (PDF, JPG, PNG, etc.).
   - Acesso seguro ao prontuário de qualquer lugar.

4. **Gestão de Recursos e Estoque**

   - Controle de estoque de medicamentos e outros materiais.

5. **Relatórios e Estatísticas**
   - Geração de relatórios sobre número de consultas, pacientes atendidos, faturamento, etc.

## Requisitos Não Funcionais

1. **Segurança**

   - Implementação de autenticação e autorização de usuários com diferentes níveis de acesso (admin, médico, recepcionista, paciente).

2. **Desempenho**

   - Respostas do sistema devem ter tempo de carregamento inferior a 2 segundos para 95% das interações.

3. **Manutenibilidade**

   - Código-fonte segue boas práticas de programação, com documentação clara, uso de versionamento (Git) e modularização.
   - Plano de manutenção com suporte a atualizações e correções de bugs.

4. **Usabilidade**

   - Interface intuitiva e amigável.
   - Layout responsivo e compatível com dispositivos móveis.

5. **Backup e Recuperação**
   - Sistema deve ter backup dos dados.

## Tecnologias Utilizadas

- **Backend:** Django
- **Frontend:** HTML e Bootstrap

## Como Executar o Projeto

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/mediflow.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd medi-flow
   ```

3. Crie um ambiente virtual e ative-o:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

5. Execute as migrações do banco de dados:

   ```bash
   python manage.py migrate
   ```

6. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

7. Acesse o sistema em: `http://127.0.0.1:8000/`