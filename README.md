Projeto de Análise de Dados - Insights
Descrição

Este projeto consiste em uma aplicação em Python que processa dados de vendas de diversos arquivos CSV, agrega informações e gera relatórios significativos sobre o desempenho das vendas. O objetivo principal é fornecer uma análise clara e acessível dos dados de vendas, permitindo a tomada de decisões informadas para estratégias de negócios.
Funcionalidades

    Leitura de Dados: O sistema utiliza a biblioteca pandas para ler múltiplos arquivos CSV de um diretório especificado, detectando automaticamente o país de origem dos dados com base no nome do arquivo.

    Processamento e Limpeza de Dados: Os dados são combinados em um único DataFrame, onde colunas como sale_date, customer, brand, model, price, payment_method e country são extraídas e formatadas para garantir a integridade dos dados.

    Análise de Dados:
        O projeto realiza agregações estatísticas para calcular a soma, média, mínimo e máximo dos preços de venda, agrupando os resultados por país.
        Também contabiliza a frequência de métodos de pagamento utilizados nas transações, permitindo uma visão detalhada do comportamento do consumidor.

    Exportação de Dados: Os dados processados podem ser exportados para um arquivo JSON, facilitando a integração com outras ferramentas e sistemas.
    Exportação de Dados para o Banco de Dados SQL, facilitando a integração com outras ferramentas e sistemas.

Tecnologias Utilizadas

    Python: Linguagem principal utilizada para desenvolvimento do projeto.
    Pandas: Biblioteca poderosa para manipulação e análise de dados.
    PyODBC: Utilizado para conexão e interação com bancos de dados SQL Server, permitindo a inserção de dados processados em tabelas específicas.
    JSON: Formato utilizado para armazenamento e exportação dos dados processados.

Resultados

Este projeto não apenas simplifica o processo de análise de dados, mas também proporciona insights valiosos sobre o comportamento de vendas, permitindo uma melhor compreensão das tendências do mercado e das preferências dos consumidores.
Como Usar

    Preparar os Dados: Coloque os arquivos CSV em um diretório chamado raw.
    Executar o Script: Execute o script principal para processar os dados e gerar as análises desejadas.
    Visualizar Resultados: Os resultados agregados são exibidos no console, e os dados processados são salvos em um arquivo JSON na pasta clean.
